# Garbage Collection System 🗑️

This project is a web application designed to facilitate garbage management in urban areas by allowing users to report garbage locations with images and location data, which are then received by the nearest garbage management admin for collection scheduling.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Design](#system-design)
- [Schema Diagram](#schema-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
This system aims to improve urban cleanliness by creating a bridge between citizens and garbage management admins, enabling citizens to report garbage locations with images and real-time GPS locations. The admin dashboard receives reports and organizes them by proximity to optimize garbage collection routes.

---

## Features
- **User Submission**: Users can report garbage spots by uploading an image and their location.
- **Admin Dashboard**: Admins can view a list of garbage reports sorted by proximity.
- **Map Integration**: Real-time GPS data enables accurate location tagging.
- **Task Scheduling**: Admins can update the status as each garbage report is addressed.
- **UI Design**: Responsive and interactive using Bootstrap, CSS animations, and Django templates.

---

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap, JavaScript (for dynamic UI), DTL (Django Templating Language)
- **Database**: SQLite (or any other Django-supported DB)
- **APIs**: GeoLocation API for real-time location data

---

## System Design

### System Components
1. **User Module**: Enables image upload and location sharing.
2. **Admin Module**: Manages and tracks garbage reports in real-time.
3. **Geo-Location System**: Captures real-time GPS data for accurate reporting.
4. **Notifications System**: Updates the admin dashboard when new reports arrive.

### User Flow Diagram

User -> Uploads Garbage Report -> System Captures Image and Location
     -> Report sent to Admin Dashboard -> Admin views Reports and schedules collection
## Entity Relationship Diagram (ERD)
- **User**: (UserID, Name, Location, Contact)
- **Report**: (ReportID, Image, Location, Timestamp, Status)
- **Admin**: (AdminID, Name, Managed Area)

---

## Schema Diagram

### User Table
- **user_id**: Unique identifier
- **name**: User’s name
- **location**: Location of the user
- **contact**: User contact information

### Report Table
- **report_id**: Unique identifier for each garbage report
- **image**: Image of the garbage location
- **location**: GPS coordinates for the location
- **timestamp**: Date and time of report submission
- **status**: Current status of report (e.g., Pending, In Progress, Completed)

### Admin Table
- **admin_id**: Unique identifier for each admin
- **name**: Admin’s name
- **managed_area**: Area under admin’s supervision

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone [repository link]
    cd garbage-collection-system
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

4. **Run Server**
    ```bash
    python manage.py runserver
    ```
## Usage

- **User Registration**: Users can register and submit garbage reports with images and location data.
- **Admin Dashboard**: Admins view real-time reports and can update task status.

---

## Screenshots
## Screenshots

1. **User Submission Page**  
   Users submit images of garbage locations along with real-time location data.  
   ![User Submission Page](https://github.com/vidyansh07/EcoClean/blob/main/screenshots/Screenshot%202024-11-01%20155023.png)

2. **Admin Dashboard**  
   Admins view incoming reports, sorted by proximity, and manage task statuses.  
   ![Admin Dashboard](https://github.com/vidyansh07/EcoClean/blob/main/screenshots/Screenshot%202024-11-01%20155141.png)

3. **Task Management**  
   Admins can update report status to reflect collection progress.  
   ![Task Management](path/to/task_management_image.png)

---

## Contributing

We welcome contributions from the community! Please submit a pull request or open an issue if you would like to contribute or have ideas for improvement.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
