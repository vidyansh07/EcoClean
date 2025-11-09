# API Schema Documentation

## Overview

Complete API reference for Car-Bon IoT Monitoring System. All endpoints use JSON format for requests and responses.

**Base URL**: `https://your-lambda-url.amazonaws.com/` or `http://localhost:8080`

**API Documentation (Swagger)**: `/docs`  
**ReDoc Documentation**: `/redoc`

## Authentication

Currently using public access. Future versions will implement:
- API Key authentication
- JWT tokens
- OAuth 2.0

## Common Response Codes

- `200 OK` - Successful GET request
- `201 Created` - Successful POST request
- `400 Bad Request` - Invalid parameters
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Routers

### 1. DynamoDB Router (`/Dynamo`)

Operations for sensor data management.

#### 1.1 Get All Tables

```http
GET /Dynamo/tables
```

**Response**:
```json
[
  "CarBon_Data",
  "user_table"
]
```

---

#### 1.2 Get Single Item

```http
GET /Dynamo/items/{item_id}/{timestamp}
```

**Path Parameters**:
- `item_id` (string, required): Device identifier (e.g., "ESP32")
- `timestamp` (integer, required): Unix timestamp

**Query Parameters**:
- `q` (string, optional): Additional query parameter

**Response**:
```json
{
  "device_id": "ESP32",
  "timestamp": 1593541800,
  "sensor_values": {
    "CO": "0.57",
    "temperature": 0,
    "humidity": 0,
    "CO_PPM": 47.5
  }
}
```

---

#### 1.3 Get Items by Date Range

```http
GET /Dynamo/items?item_id={device_id}&from_timestamp={start}&to_timestamp={end}
```

**Query Parameters**:
- `item_id` (string, required): Device identifier
- `from_timestamp` (integer, required): Start timestamp
- `to_timestamp` (integer, required): End timestamp

**Response**:
```json
{
  "Results": [
    {
      "device_id": "ESP32",
      "timestamp": 1593541800,
      "sensor_values": {
        "CO": "0.57",
        "temperature": 0,
        "humidity": 0,
        "CO_PPM": 47.5
      }
    }
  ],
  "Metadata": {
    "count": 150
  }
}
```

---

#### 1.4 Get Latest Reading

```http
GET /Dynamo/items/latest?item_id={device_id}
```

**Query Parameters**:
- `item_id` (string, required): Device identifier

**Response**: Same as Get Single Item

---

#### 1.5 Write Sensor Data

```http
POST /Dynamo/item?item_id={id}&Temp={temp}&Hum={humidity}&CO={co_value}
```

**Query Parameters**:
- `item_id` (string, required): Device identifier
- `Temp` (string, required): Temperature reading
- `Hum` (string, required): Humidity reading
- `CO` (string, required): Carbon monoxide reading

**Response**:
```json
{
  "message": "Item written successfully",
  "timestamp": 1593541800
}
```

---

### 2. User Router (`/user`)

User management operations.

#### 2.1 Create New User

```http
POST /user/new
```

**Query Parameters**:
- `name` (string, required): User's full name
- `registered_device_id` (string, required): IoT device ID
- `personal_contact` (string, required): Phone number (without country code)
- `country` (enum, required): Country code (e.g., "IN", "US")

**Request Example**:
```http
POST /user/new?name=John%20Doe&registered_device_id=ESP32_001&personal_contact=9876543210&country=IN
```

**Response**:
```json
{
  "Item": {
    "id": "01HANV3Y7Z8QZXJW2K3P4M5N6",
    "name": "John Doe",
    "registered_device_id": "ESP32_001",
    "personal_contact": "+919876543210",
    "secondary_contacts": null,
    "emergency_contacts": {
      "primary_sos": "100",
      "primary_fire": "101",
      "primary_health": "102",
      "secondary_health": "108",
      "primary_NHH": "1033",
      "primary_DM": "1078",
      "primary_NHAI": "1800-11-6062"
    }
  },
  "write_successful": true
}
```

---

#### 2.2 Get User Contacts

```http
GET /user/contacts?user_id={user_id}
```

**Query Parameters**:
- `user_id` (string, required): User's ULID

**Response**:
```json
{
  "personal_contact": "+919876543210",
  "secondary_contacts": [
    "+919876543211",
    "+919876543212"
  ]
}
```

---

### 3. Notification Router (`/notify`)

Alert and notification operations.

#### 3.1 Send SMS

```http
POST /notify/send_sms?user_id={id}&message={message}
```

**Query Parameters**:
- `user_id` (string, required): User's ULID
- `message` (string, required): SMS message content

**Response**:
```json
{
  "message_body": "Alert: CO levels exceeded threshold",
  "sender": "+12345678900",
  "receiver": "+919876543210",
  "date_updated": "2025-11-09T10:30:00Z",
  "error_message": null,
  "status": "sent",
  "sid": "SM1234567890abcdef",
  "date_sent": "2025-11-09T10:30:00Z",
  "date_created": "2025-11-09T10:30:00Z",
  "error_code": null,
  "api_version": "2010-04-01"
}
```

---

#### 3.2 Make Voice Call

```http
POST /notify/make_call?user_id={user_id}
```

**Query Parameters**:
- `user_id` (string, required): User's ULID

**Response**:
```json
{
  "account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "sid": "CAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "status": "queued",
  "to": "+919876543210",
  "from_formatted": "+1 (234) 567-8900",
  "date_created": "2025-11-09T10:30:00Z",
  "duration": null,
  "uri": "/2010-04-01/Accounts/ACxxxx/Calls/CAxxxx.json"
}
```

---

### 4. Graph Router (`/graph`)

Data visualization operations.

#### 4.1 Generate Graph

```http
GET /graph/generate?start_date={date}&end_date={date}&graph_type={type}&device={id}
```

**Query Parameters**:
- `start_date` (string, required): ISO 8601 datetime (e.g., "2025-11-01T00:00:00")
- `end_date` (string, required): ISO 8601 datetime
- `graph_type` (string, optional): "Line" or "Bar" (default: "Line")
- `device` (string, optional): Device ID (default: "ESP32")

**Response**:
```json
{
  "base64_data": "data:image/svg+xml;charset=utf-8;base64,PD94bWwgdmVyc2lvbj0i..."
}
```

**Response Headers**:
```http
start_date: 1698796800
end_date: 1699401600
device_type: ESP32
Content-Type: application/json
```

---

## Data Models

### sensor_data

```python
{
  "temperature": int,      # Temperature in Celsius
  "CO": float,             # CO sensor raw reading
  "humidity": int,         # Humidity percentage
  "CO_PPM": float          # CO in Parts Per Million
}
```

### dynamo_result

```python
{
  "sensor_values": sensor_data,
  "device_id": str,        # Device identifier
  "timestamp": int         # Unix timestamp
}
```

### get_all_results_out

```python
{
  "Results": List[dynamo_result],
  "Metadata": {
    "count": int           # Total results count
  }
}
```

### user_class

```python
{
  "id": str,                          # ULID format
  "name": str,
  "registered_device_id": str,
  "personal_contact": str,            # E.164 format
  "secondary_contacts": List[str] | null,
  "emergency_contacts": {
    "primary_sos": str,
    "primary_fire": str,
    "primary_health": str,
    "secondary_health": str,
    "primary_NHH": str,
    "primary_DM": str,
    "primary_NHAI": str
  }
}
```

### twilio_sms_response_out

```python
{
  "message_body": str | null,
  "sender": str | null,
  "receiver": str | null,
  "date_updated": datetime | null,
  "error_message": str | null,
  "status": str | null,
  "sid": str | null,
  "date_sent": datetime | null,
  "date_created": datetime | null,
  "error_code": str | null,
  "api_version": str | null
}
```

### chart_types (Enum)

```python
{
  "Bar_graph": "Bar",
  "Line_graph": "Line"
}
```

---

## Error Responses

### 400 Bad Request

```json
{
  "detail": "Invalid parameter format"
}
```

### 404 Not Found

```json
{
  "detail": "User not found"
}
```

### 500 Internal Server Error

```json
{
  "error": "Unable to process request",
  "message": "Detailed error message"
}
```

---

## Rate Limiting

**Current**: No rate limiting  
**Planned**: 
- 100 requests per minute per IP
- 1000 requests per hour per API key

---

## Pagination

For large datasets, use offset and limit:

```http
GET /Dynamo/items?item_id=ESP32&from_timestamp=0&to_timestamp=9999999999&limit=100&offset=0
```

**Planned Parameters**:
- `limit` (int): Records per page (default: 100, max: 1000)
- `offset` (int): Starting record (default: 0)

---

## WebSocket Support

**Planned**: Real-time sensor data streaming

```javascript
ws://your-domain.com/ws/sensor-data/{device_id}

// Client message
{
  "action": "subscribe",
  "device_id": "ESP32"
}

// Server message
{
  "device_id": "ESP32",
  "timestamp": 1593541800,
  "co_level": 47.5,
  "alert": false
}
```

---

## Best Practices

### 1. Date/Time Format
- Use ISO 8601 format: `2025-11-09T10:30:00Z`
- Or Unix timestamp: `1699529400`

### 2. Phone Numbers
- Use E.164 format: `+919876543210`
- Include country code

### 3. Device IDs
- Use consistent naming: `ESP32_001`, `ESP32_002`
- Avoid special characters

### 4. Error Handling
- Always check response status code
- Parse error messages from response body

### 5. Retries
- Implement exponential backoff
- Max 3 retry attempts

---

## Code Examples

### Python (requests)

```python
import requests

# Write sensor data
response = requests.post(
    "http://localhost:8080/Dynamo/item",
    params={
        "item_id": "ESP32",
        "Temp": "25",
        "Hum": "60",
        "CO": "0.57"
    }
)
print(response.json())

# Get latest reading
response = requests.get(
    "http://localhost:8080/Dynamo/items/latest",
    params={"item_id": "ESP32"}
)
data = response.json()
print(f"CO Level: {data['sensor_values']['CO_PPM']} PPM")
```

### JavaScript (fetch)

```javascript
// Create user
const createUser = async () => {
  const response = await fetch(
    'http://localhost:8080/user/new?' + new URLSearchParams({
      name: 'John Doe',
      registered_device_id: 'ESP32_001',
      personal_contact: '9876543210',
      country: 'IN'
    }),
    { method: 'POST' }
  );
  const data = await response.json();
  console.log('User created:', data);
};

// Generate graph
const getGraph = async () => {
  const response = await fetch(
    'http://localhost:8080/graph/generate?' + new URLSearchParams({
      start_date: '2025-11-01T00:00:00',
      end_date: '2025-11-09T23:59:59',
      graph_type: 'Line',
      device: 'ESP32'
    })
  );
  const data = await response.json();
  document.getElementById('graph').src = data.base64_data;
};
```

### cURL

```bash
# Write sensor data
curl -X POST "http://localhost:8080/Dynamo/item?item_id=ESP32&Temp=25&Hum=60&CO=0.57"

# Send SMS alert
curl -X POST "http://localhost:8080/notify/send_sms?user_id=01HANV3Y7Z8QZXJW2K3P4M5N6&message=CO%20Alert"

# Get graph
curl "http://localhost:8080/graph/generate?start_date=2025-11-01T00:00:00&end_date=2025-11-09T23:59:59&graph_type=Line&device=ESP32"
```

---

*Last Updated: 2025-11-09*
*API Version: 1.6.8*
