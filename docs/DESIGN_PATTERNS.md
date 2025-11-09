# Design Patterns in Car-Bon Project

## Table of Contents

- [Introduction](#introduction)
- [Creational Patterns](#creational-patterns)
- [Structural Patterns](#structural-patterns)
- [Behavioral Patterns](#behavioral-patterns)
- [Architectural Patterns](#architectural-patterns)
- [Cloud Design Patterns](#cloud-design-patterns)
- [Code Examples](#code-examples)

## Introduction

This document details all design patterns implemented in the Car-Bon IoT monitoring system. Each pattern is explained with its purpose, implementation, and benefits.

## Creational Patterns

### 1. Singleton Pattern

**Location**: `src/API/app/services/*.py`

**Purpose**: Ensure only one instance of service classes exists throughout the application lifecycle.

**Implementation**:

```python
# services/dynamo.py
class dynamo:
    _instance = None
    
    def __new__(cls, table_name):
        if cls._instance is None:
            cls._instance = super(dynamo, cls).__new__(cls)
            cls._instance.dynamodb = boto3.resource("dynamodb")
            cls._instance.table = cls._instance.dynamodb.Table(table_name)
        return cls._instance
```

**Benefits**:
- Reduces resource consumption (single DB connection)
- Maintains consistent state across requests
- Simplifies dependency management

**Usage in Project**:
- `dynamo_class` - Single DynamoDB client instance
- `twilio_class` - Single Twilio client instance
- `user_service_class` - Single user service instance

---

### 2. Factory Pattern

**Location**: `src/API/app/services/graph_service.py`

**Purpose**: Create different types of graphs without specifying exact classes.

**Implementation**:

```python
class graph_types(Enum):
    Line: str = "Line"
    Bar: str = "Bar"

def generate_graph(Data, graph_type: graph_types = 'Line', BASE_PATH = "."):
    # Factory method to create appropriate graph type
    if graph_type.value in pygal.CHARTS_BY_NAME.keys():
        graph_function: pygal.Graph = eval(f"pygal.{graph_type.value}")
    else:
        graph_function: pygal.Graph = pygal.Line  # Default
    
    c = graph_function(
        title="Carbon monoxide Data",
        style=custom_style,
        y_title='CO level',
        width=1200,
        x_label_rotation=315,
    )
    return c
```

**Benefits**:
- Flexible graph type selection
- Easy to add new graph types
- Encapsulates object creation logic

---

### 3. Builder Pattern

**Location**: `src/API/app/services/user_service.py`

**Purpose**: Construct complex user objects step by step.

**Implementation**:

```python
class user_class(BaseModel):
    id: str = str(ULID())  # Auto-generated
    name: str
    registered_device_id: str
    personal_contact: str
    secondary_contacts: Optional[List[str]]
    emergency_contacts: dict = emergency_contacts().model_dump()

def create_user(self, name: str, device_id: str, 
                personal_contact: str, secondary_contacts: List = None):
    new_user = user_class(
        name=name,
        registered_device_id=device_id,
        personal_contact=personal_contact,
        secondary_contacts=secondary_contacts,
    )
    self.table.put_item(Item=new_user.model_dump())
    return new_user
```

**Benefits**:
- Separates construction from representation
- Default values for optional fields
- Validation through Pydantic models

---

## Structural Patterns

### 4. Adapter Pattern

**Location**: `src/API/app/index.py`

**Purpose**: Convert ASGI FastAPI application to AWS Lambda handler format.

**Implementation**:

```python
from mangum import Mangum

app = FastAPI(
    title="Car-Bon-service",
    version=app_version,
)

# Adapter: Converts ASGI to Lambda handler
handler = Mangum(app)
```

**Benefits**:
- Enables FastAPI to run on AWS Lambda
- No code changes required for deployment
- Maintains standard ASGI interface

---

### 5. Facade Pattern

**Location**: `src/API/app/index.py`, Router Layer

**Purpose**: Provide simplified interface to complex subsystem operations.

**Implementation**:

```python
# Complex subsystem operations hidden behind simple router endpoints
@dynamo_router.get("/items/latest", status_code=status.HTTP_200_OK)
def get_latest_item(item_id: str):
    # Facade hides complexity of:
    # - DynamoDB connection
    # - Query construction
    # - Data transformation
    # - Error handling
    response = dynamo_class.get_last_Updated_value(item_id)
    return response

@twilio_router.post("/send_sms", status_code=status.HTTP_200_OK)
def send_sms(user_id: str, message: str):
    # Facade hides complexity of:
    # - User lookup
    # - Contact retrieval
    # - Twilio API calls
    # - Response formatting
    contacts = get_contacts(user_id)
    receiver = contacts["personal_contact"]
    message_resp = twilio_class.send_message(message, receiver)
    return message_resp
```

**Benefits**:
- Simplifies client code
- Reduces coupling between layers
- Easier testing and maintenance

---

### 6. Decorator Pattern

**Location**: `src/API/app/index.py`, FastAPI Routers

**Purpose**: Add behavior to functions dynamically without modifying their structure.

**Implementation**:

```python
# FastAPI route decorators add HTTP handling capabilities
@dynamo_router.get("/items/{item_id}/{timestamp}", status_code=status.HTTP_200_OK)
def get_item(item_id: str, timestamp: int, q: Union[str, None] = None):
    response = dynamo_class.get_dynamo_data(device_id=item_id, timestamp=timestamp)
    return response

# Middleware decorators add cross-cutting concerns
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Benefits**:
- Adds functionality without inheritance
- Follows Open/Closed Principle
- Composable decorators

---

### 7. Proxy Pattern

**Location**: `src/API/app/services/secret_manager.py`

**Purpose**: Control access to AWS Secrets Manager with caching and error handling.

**Implementation**:

```python
class SecretManagerProxy:
    def __init__(self):
        self.client = boto3.client('secretsmanager')
        self._cache = {}
    
    def get_secret(self, secret_name):
        # Proxy adds caching layer
        if secret_name in self._cache:
            return self._cache[secret_name]
        
        # Access real service
        response = self.client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        
        # Cache for future requests
        self._cache[secret_name] = secret
        return secret
```

**Benefits**:
- Reduces AWS API calls through caching
- Adds security layer
- Controls resource access

---

## Behavioral Patterns

### 8. Strategy Pattern

**Location**: `src/API/app/services/graph_service.py`

**Purpose**: Define family of algorithms (graph types) and make them interchangeable.

**Implementation**:

```python
class graph_types(Enum):
    Line: str = "Line"
    Bar: str = "Bar"

# Strategy: Different algorithms for same task
def generate_graph(Data, graph_type: graph_types = 'Line', BASE_PATH = "."):
    # Select strategy at runtime
    if graph_type.value in pygal.CHARTS_BY_NAME.keys():
        graph_function = eval(f"pygal.{graph_type.value}")
    else:
        graph_function = pygal.Line
    
    # Execute selected strategy
    chart = graph_function(...)
    return chart.render_data_uri()
```

**Benefits**:
- Runtime algorithm selection
- Easy to add new graph types
- Eliminates conditional statements

---

### 9. Observer Pattern

**Location**: IoT to Cloud communication

**Purpose**: Notify cloud services when sensor readings change.

**Implementation**:

```python
# Conceptual implementation (IoT device code)
class SensorObserver:
    def __init__(self):
        self.subscribers = []
    
    def attach(self, observer):
        self.subscribers.append(observer)
    
    def notify(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)

# When CO level exceeds threshold
if co_reading > THRESHOLD:
    notify_cloud_service(co_reading)
    trigger_alerts(co_reading)
```

**Benefits**:
- Loose coupling between sensor and cloud
- Multiple observers can be notified
- Async notification support

---

### 10. Template Method Pattern

**Location**: `src/API/app/services/twilio_service.py`

**Purpose**: Define skeleton of notification algorithm, letting subclasses override specific steps.

**Implementation**:

```python
class twilio_service:
    def send_notification(self, user_id, notification_type):
        # Template method defines algorithm structure
        contacts = self._get_contacts(user_id)
        receiver = self._select_receiver(contacts)
        message = self._prepare_message(notification_type)
        response = self._send(receiver, message, notification_type)
        return response
    
    # Steps that can be overridden
    def _send(self, receiver, message, type):
        if type == "SMS":
            return self.send_message(message, receiver)
        elif type == "CALL":
            return self.call_person(receiver)
```

**Benefits**:
- Defines common algorithm structure
- Allows customization of specific steps
- Promotes code reuse

---

### 11. Command Pattern

**Location**: `src/API/app/index.py`, API Routers

**Purpose**: Encapsulate requests as objects, allowing parameterization and queuing.

**Implementation**:

```python
# Each endpoint is a command that encapsulates an action
class WriteSensorDataCommand:
    def __init__(self, device_id, temp, hum, co):
        self.device_id = device_id
        self.temp = temp
        self.hum = hum
        self.co = co
    
    def execute(self):
        return dynamo_class.update_table(
            device_id=self.device_id,
            Temp=self.temp,
            Hum=self.hum,
            CO=self.co
        )

# FastAPI endpoint acts as command invoker
@dynamo_router.post("/item", status_code=status.HTTP_201_CREATED)
def write_item(item_id: str, Temp: str, Hum: str, CO: str):
    command = WriteSensorDataCommand(item_id, Temp, Hum, CO)
    return command.execute()
```

**Benefits**:
- Decouples sender from receiver
- Supports undo/redo operations
- Easy to add new commands

---

## Architectural Patterns

### 12. Layered Architecture Pattern

**Location**: Entire application structure

**Purpose**: Separate concerns into distinct layers.

**Implementation**:

```
┌─────────────────────────────┐
│   Presentation Layer        │  ← React UI, Dash Dashboard
├─────────────────────────────┤
│   API Layer (Routers)       │  ← FastAPI routes, validators
├─────────────────────────────┤
│   Business Logic Layer      │  ← Service classes
├─────────────────────────────┤
│   Data Access Layer         │  ← DynamoDB, External APIs
└─────────────────────────────┘
```

**Benefits**:
- Clear separation of concerns
- Independent layer testing
- Parallel development possible

---

### 13. Microservices Pattern

**Location**: Service layer organization

**Purpose**: Structure application as collection of loosely coupled services.

**Services**:
1. **DynamoDB Service** - Data persistence
2. **User Service** - User management
3. **Notification Service** - Alerts
4. **Graph Service** - Visualization
5. **Secret Manager Service** - Configuration

**Benefits**:
- Independent deployment
- Technology diversity
- Fault isolation

---

### 14. Repository Pattern

**Location**: `src/API/app/services/dynamo.py`, `user_service.py`

**Purpose**: Abstract data access logic and provide collection-like interface.

**Implementation**:

```python
class dynamo:
    """Repository for sensor data"""
    
    def get_dynamo_data(self, device_id, timestamp):
        """Get single item"""
        pass
    
    def get_data_between_timestamps(self, device_id, from_ts, to_ts):
        """Get collection of items"""
        pass
    
    def update_table(self, device_id, Temp, Hum, CO):
        """Add item to repository"""
        pass

class user_service:
    """Repository for user data"""
    
    def create_user(self, name, device_id, contact, secondary):
        """Add user"""
        pass
    
    def get_user(self, user_id):
        """Get user by ID"""
        pass
```

**Benefits**:
- Abstracts data source details
- Centralizes data access logic
- Easy to switch data stores

---

### 15. Dependency Injection Pattern

**Location**: `src/API/app/index.py`

**Purpose**: Provide dependencies from outside rather than creating them internally.

**Implementation**:

```python
# Dependencies injected via environment/configuration
TABLE_NAME = os.environ["TABLE_NAME"]
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]

# Services receive dependencies
dynamo_class = dynamo(table_name=TABLE_NAME)
twilio_class = twilio_service(
    account_sid_var=ACCOUNT_SID, 
    auth_token_var=AUTH_TOKEN, 
    number=NUMBER
)

# FastAPI automatic dependency injection
@dynamo_router.get("/items/{item_id}/{timestamp}")
def get_item(item_id: str, timestamp: int, q: Union[str, None] = None):
    # Dependencies automatically injected by FastAPI
    response = dynamo_class.get_dynamo_data(device_id=item_id, timestamp=timestamp)
    return response
```

**Benefits**:
- Loose coupling
- Easier testing (mock injection)
- Configuration flexibility

---

## Cloud Design Patterns

### 16. Serverless Pattern

**Location**: AWS Lambda deployment

**Purpose**: Run code without managing servers.

**Implementation**:
- FastAPI app runs on AWS Lambda
- Auto-scaling based on demand
- Pay-per-invocation pricing

**Benefits**:
- Zero server management
- Automatic scaling
- Cost optimization

---

### 17. Event-Driven Pattern

**Location**: IoT sensor triggers

**Purpose**: React to events asynchronously.

**Flow**:
```
Sensor Reading → API Event → DynamoDB Write → 
Threshold Check → Alert Event → Notification
```

**Benefits**:
- Loose coupling
- Scalability
- Real-time response

---

### 18. Circuit Breaker Pattern

**Location**: External API calls (Twilio, AWS)

**Purpose**: Prevent cascading failures in distributed systems.

**Implementation**:

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            raise CircuitBreakerOpenError()
        
        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except Exception as e:
            self.on_failure()
            raise e
```

**Benefits**:
- Prevents resource exhaustion
- Fails fast
- Automatic recovery

---

### 19. CQRS (Command Query Responsibility Segregation)

**Location**: DynamoDB operations

**Purpose**: Separate read and write operations.

**Implementation**:

```python
# Command (Write) operations
def write_item(item_id: str, Temp: str, Hum: str, CO: str):
    return dynamo_class.update_table(...)

# Query (Read) operations
def get_items(item_id: str, from_timestamp: int, to_timestamp: int):
    return dynamo_class.get_data_between_timestamps(...)

def get_latest_item(item_id: str):
    return dynamo_class.get_last_Updated_value(...)
```

**Benefits**:
- Optimized read/write paths
- Better scalability
- Clear separation of concerns

---

### 20. Retry Pattern

**Location**: AWS SDK operations

**Purpose**: Automatically retry failed operations.

**Implementation**:

```python
from botocore.config import Config
import boto3

# Boto3 with automatic retries
config = Config(
    retries={
        'max_attempts': 3,
        'mode': 'adaptive'
    }
)

dynamodb = boto3.resource('dynamodb', config=config)
```

**Benefits**:
- Handles transient failures
- Improves reliability
- Exponential backoff

---

## Code Examples

### Pattern Combination Example

**Scenario**: Sending alert notification

```python
# 1. Facade Pattern - Simple interface
@twilio_router.post("/send_sms")
def send_sms(user_id: str, message: str):
    
    # 2. Repository Pattern - Data access
    contacts = user_service_class.get_user(user_id)
    
    # 3. Strategy Pattern - Choose notification method
    if is_emergency(message):
        notification_strategy = twilio_class.call_person
    else:
        notification_strategy = twilio_class.send_message
    
    # 4. Template Method - Execute notification
    response = notification_strategy(
        contacts["personal_contact"],
        message
    )
    
    # 5. Adapter Pattern - Format response
    return format_response(response)
```

### Anti-Patterns Avoided

**God Object**: Avoided by separating concerns into services
**Spaghetti Code**: Prevented by layered architecture
**Hard Coding**: Configuration externalized to environment variables
**Tight Coupling**: Dependency injection and interfaces used

---

## Pattern Selection Guidelines

### When to Use Each Pattern

**Creational**:
- Singleton: Shared resources (DB connections)
- Factory: Multiple related types (graph types)
- Builder: Complex object construction (user creation)

**Structural**:
- Adapter: Interface incompatibility (Lambda/ASGI)
- Facade: Simplify complex subsystems (API routes)
- Proxy: Control resource access (secrets)

**Behavioral**:
- Strategy: Runtime algorithm selection (graphs)
- Observer: Event notifications (alerts)
- Template Method: Standardized workflows (notifications)

**Architectural**:
- Layered: Separation of concerns (entire app)
- Microservices: Independent services
- Repository: Data access abstraction

---

## Summary

The Car-Bon project employs **20+ design patterns** across different categories:

- **Creational (3)**: Singleton, Factory, Builder
- **Structural (4)**: Adapter, Facade, Decorator, Proxy
- **Behavioral (4)**: Strategy, Observer, Template Method, Command
- **Architectural (5)**: Layered, Microservices, Repository, DI, CQRS
- **Cloud (4)**: Serverless, Event-Driven, Circuit Breaker, Retry

These patterns work together to create a:
- **Maintainable** codebase
- **Scalable** architecture
- **Testable** components
- **Extensible** design

---

*Last Updated: 2025-11-09*
*Version: 1.6.8*
