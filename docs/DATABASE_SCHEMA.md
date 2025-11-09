# Database Schema Documentation

## Overview

Car-Bon uses a hybrid database approach:
- **AWS DynamoDB**: Primary NoSQL database for real-time IoT data
- **SQL Schema**: Legacy/backup relational database schema

## DynamoDB Tables

### 1. CarBon_Data Table

**Purpose**: Store time-series sensor data from IoT devices

**Table Configuration**:
```yaml
Table Name: CarBon_Data
Billing Mode: ON_DEMAND
Capacity: Auto-scaling enabled
Region: us-east-1
Encryption: AWS KMS
Point-in-Time Recovery: Enabled
```

**Primary Key Structure**:
```
Partition Key: device_id (String)
Sort Key: timestamp (Number)
```

**Schema**:

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| device_id | String (S) | Yes | Unique device identifier (e.g., "ESP32") |
| timestamp | Number (N) | Yes | Unix timestamp (epoch seconds) |
| CO | String (S) | Yes | Carbon monoxide sensor reading (raw value) |
| temperature | Number (N) | No | Temperature in Celsius (placeholder, currently 0) |
| humidity | Number (N) | No | Humidity percentage (placeholder, currently 0) |

**Example Item**:
```json
{
  "device_id": "ESP32",
  "timestamp": 1593541800,
  "CO": "0.57",
  "temperature": 0,
  "humidity": 0
}
```

**Indexes**:

Global Secondary Index (GSI):
```yaml
Index Name: timestamp-index (planned)
Partition Key: timestamp
Projection: ALL
Purpose: Query data by time range across all devices
```

**Access Patterns**:

1. **Get latest reading for device**
```python
Query(
  KeyConditionExpression: device_id = :deviceId,
  ScanIndexForward: False,
  Limit: 1
)
```

2. **Get readings by time range**
```python
Query(
  KeyConditionExpression: 
    device_id = :deviceId AND 
    timestamp BETWEEN :startTime AND :endTime
)
```

3. **Write new reading**
```python
PutItem(
  Item: {
    device_id: "ESP32",
    timestamp: 1699529400,
    CO: "0.57",
    temperature: 25,
    humidity: 60
  }
)
```

**Capacity Planning**:
- Average item size: ~100 bytes
- Write frequency: 1 per minute per device
- Read frequency: Variable (dashboard updates)
- Estimated monthly cost: $5-10 for 10 devices

---

### 2. user_table Table

**Purpose**: Store user profiles and device registrations

**Table Configuration**:
```yaml
Table Name: user_table
Billing Mode: ON_DEMAND
Capacity: Auto-scaling enabled
Region: us-east-1
Encryption: AWS KMS
```

**Primary Key Structure**:
```
Partition Key: id (String - ULID format)
```

**Schema**:

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| id | String (S) | Yes | ULID (Universally Unique Lexicographically Sortable ID) |
| name | String (S) | Yes | User's full name |
| registered_device_id | String (S) | Yes | Associated IoT device ID |
| personal_contact | String (S) | Yes | Primary phone number (E.164 format) |
| secondary_contacts | List (L) | No | List of additional phone numbers |
| emergency_contacts | Map (M) | Yes | Map of emergency service numbers |

**Example Item**:
```json
{
  "id": "01HANV3Y7Z8QZXJW2K3P4M5N6",
  "name": "John Doe",
  "registered_device_id": "ESP32_001",
  "personal_contact": "+919876543210",
  "secondary_contacts": [
    "+919876543211",
    "+919876543212"
  ],
  "emergency_contacts": {
    "primary_sos": "100",
    "primary_fire": "101",
    "primary_health": "102",
    "secondary_health": "108",
    "primary_NHH": "1033",
    "primary_DM": "1078",
    "primary_NHAI": "1800-11-6062"
  }
}
```

**Access Patterns**:

1. **Get user by ID**
```python
Query(
  KeyConditionExpression: id = :userId
)
```

2. **Create new user**
```python
PutItem(
  Item: {
    id: generateULID(),
    name: "John Doe",
    registered_device_id: "ESP32_001",
    personal_contact: "+919876543210",
    ...
  }
)
```

3. **Get users by device (requires GSI)**
```python
Query(
  IndexName: "device-index",
  KeyConditionExpression: registered_device_id = :deviceId
)
```

---

## SQL Schema (Legacy/Backup)

### Database: pet_adoption_portal

**Note**: The SQL schema appears to be from a different project or legacy system. Current Car-Bon implementation uses DynamoDB exclusively.

### Table: users

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('admin', 'user') DEFAULT 'user'
);
```

### Table: pets

```sql
CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    species VARCHAR(50) NOT NULL,
    breed VARCHAR(50),
    age INT,
    description TEXT,
    image_path VARCHAR(255),
    status ENUM('available', 'adopted') DEFAULT 'available'
);
```

### Table: adoptions

```sql
CREATE TABLE adoptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    pet_id INT NOT NULL,
    adoption_date DATE NOT NULL,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);
```

**Note**: These tables are not currently used in the Car-Bon system.

---

## Proposed Car-Bon SQL Schema (Future Enhancement)

For hybrid database architecture or backup purposes:

### Table: devices

```sql
CREATE TABLE devices (
    device_id VARCHAR(50) PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50) NOT NULL DEFAULT 'ESP32',
    firmware_version VARCHAR(20),
    last_seen TIMESTAMP,
    status ENUM('active', 'inactive', 'maintenance') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_last_seen (last_seen)
);
```

### Table: sensor_readings

```sql
CREATE TABLE sensor_readings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    timestamp BIGINT NOT NULL,
    co_level DECIMAL(10, 4) NOT NULL,
    co_ppm DECIMAL(10, 4) NOT NULL,
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES devices(device_id),
    INDEX idx_device_timestamp (device_id, timestamp),
    INDEX idx_timestamp (timestamp),
    INDEX idx_co_ppm (co_ppm)
);
```

### Table: users

```sql
CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY,  -- ULID
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    personal_contact VARCHAR(20) NOT NULL,
    country_code VARCHAR(5) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_contact (personal_contact)
);
```

### Table: user_devices

```sql
CREATE TABLE user_devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    device_id VARCHAR(50) NOT NULL,
    is_primary BOOLEAN DEFAULT TRUE,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (device_id) REFERENCES devices(device_id),
    UNIQUE KEY unique_user_device (user_id, device_id)
);
```

### Table: secondary_contacts

```sql
CREATE TABLE secondary_contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    contact_name VARCHAR(100),
    priority INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_user_priority (user_id, priority)
);
```

### Table: alerts

```sql
CREATE TABLE alerts (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    alert_type ENUM('sms', 'call', 'email') NOT NULL,
    co_level DECIMAL(10, 4) NOT NULL,
    message TEXT,
    status ENUM('pending', 'sent', 'failed') DEFAULT 'pending',
    sent_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES devices(device_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_device_created (device_id, created_at),
    INDEX idx_user_created (user_id, created_at),
    INDEX idx_status (status)
);
```

### Table: notification_logs

```sql
CREATE TABLE notification_logs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    alert_id BIGINT NOT NULL,
    provider VARCHAR(20) NOT NULL,  -- 'twilio', 'aws_sns', etc.
    provider_sid VARCHAR(100),
    recipient VARCHAR(20) NOT NULL,
    status VARCHAR(50),
    error_code VARCHAR(20),
    error_message TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (alert_id) REFERENCES alerts(id),
    INDEX idx_alert (alert_id),
    INDEX idx_sent_at (sent_at)
);
```

---

## Data Types & Formats

### ULID Format
```
01HANV3Y7Z8QZXJW2K3P4M5N6
└─┬─┘└────────┬───────────┘
  │          │
  │          └─ Random component (80 bits)
  └─ Timestamp component (48 bits)

Length: 26 characters
Encoding: Base32 (Crockford)
```

### Phone Number Format (E.164)
```
+[country code][subscriber number]
Example: +919876543210

Components:
- + (plus sign)
- 91 (country code for India)
- 9876543210 (subscriber number)
```

### Timestamp Format
```
Unix Epoch: Seconds since 1970-01-01T00:00:00Z
Example: 1699529400
Conversion: datetime.fromtimestamp(1699529400)
```

---

## Data Retention Policies

### DynamoDB Tables

**CarBon_Data**:
- Retention: 90 days (hot data)
- Archive: Move to S3 Glacier after 90 days
- Backup: Daily backups, 7-day retention

**user_table**:
- Retention: Indefinite
- Backup: Daily backups, 30-day retention
- Deletion: Manual only (GDPR compliance)

---

## Migration Scripts

### DynamoDB to SQL

```python
import boto3
import pymysql

def migrate_sensor_data(device_id, from_timestamp, to_timestamp):
    # Query DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CarBon_Data')
    
    response = table.query(
        KeyConditionExpression=Key('device_id').eq(device_id) & 
                               Key('timestamp').between(from_timestamp, to_timestamp)
    )
    
    # Insert into MySQL
    connection = pymysql.connect(...)
    cursor = connection.cursor()
    
    for item in response['Items']:
        cursor.execute("""
            INSERT INTO sensor_readings 
            (device_id, timestamp, co_level, temperature, humidity)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            item['device_id'],
            int(item['timestamp']),
            float(item['CO']),
            item.get('temperature', 0),
            item.get('humidity', 0)
        ))
    
    connection.commit()
```

---

## Performance Optimization

### DynamoDB

1. **Use Batch Operations**
```python
# Batch write (up to 25 items)
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
```

2. **Conditional Writes**
```python
# Prevent overwriting existing data
table.put_item(
    Item=item,
    ConditionExpression='attribute_not_exists(device_id)'
)
```

3. **Projection Expressions**
```python
# Fetch only required attributes
response = table.get_item(
    Key={'device_id': 'ESP32', 'timestamp': 1699529400},
    ProjectionExpression='device_id, CO'
)
```

### Indexing Strategies

**For Time-Range Queries**:
- Primary: (device_id, timestamp)
- GSI: (timestamp) for cross-device queries

**For User Lookups**:
- Primary: (id)
- GSI: (registered_device_id) for device-to-user mapping

---

## Backup & Recovery

### Automated Backups

```bash
# Create on-demand backup
aws dynamodb create-backup \
  --table-name CarBon_Data \
  --backup-name CarBon_Data_$(date +%Y%m%d)

# Enable PITR
aws dynamodb update-continuous-backups \
  --table-name CarBon_Data \
  --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
```

### Export to S3

```bash
# Export table to S3
aws dynamodb export-table-to-point-in-time \
  --table-arn arn:aws:dynamodb:us-east-1:123456789:table/CarBon_Data \
  --s3-bucket carbon-backups \
  --s3-prefix exports/ \
  --export-format DYNAMODB_JSON
```

---

*Last Updated: 2025-11-09*
*Schema Version: 1.6.8*
