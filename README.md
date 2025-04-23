# Task Management System

A FastAPI-based Task Management System that allows users to create, fetch, update, and delete tasks. It uses SQLAlchemy with PostgreSQL for data persistence and follows standard REST API practices.

## Features

- **Create Tasks**: Add new tasks to the system.
- **Fetch Tasks**: List all tasks with pagination.
- **Update Tasks**: Modify existing task details.
- **Delete Tasks**: Remove tasks from the system.
- **Health Check**: Endpoint to check if the database is reachable.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQL toolkit for Python.
- **PostgreSQL**: Relational database used to store task data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI server for FastAPI.

## Getting Started

### Prerequisites

- Python 3.7+
- PostgreSQL

### Clone the Repository

```bash
git clone https://github.com/arpitbabbar/task-manager.git
cd task-manager
```

### Install Dependencies

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the root directory and add the following:

```env
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database_name>
```

Example for local development:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/task_db
```

### Run the Application

You can run the application using Uvicorn:

```bash
uvicorn src.main:app --reload
```

This will start the FastAPI development server on `http://127.0.0.1:8000`.

## API Endpoints

### Health Check

- **GET** `/api/v1/health`

Checks if the database is reachable.

**Response:**

```json
{
  "status": "healthy",
  "status_code_message": "Database is reachable",
  "data": []
}
```

### Create Task

- **POST** `/api/v1/tasks`

Creates a new task.

**Request Body:**

```json
{
  "title": "task 1",
  "description": "something",
  "status": "pending"
}
```

**Response:**

```json
{
  "status": "success",
  "status_code_message": "Task created successfully",
  "data": {
    "id": "bd454eb3-878e-4e93-bf66-d2632155efd5",
    "title": "task 1",
    "description": "something",
    "status": "pending",
    "created_at": "2025-04-22T18:57:16.310204",
    "updated_at": "2025-04-22T18:57:16.310208"
  }
}
```

### Get Tasks

- **GET** `/api/v1/tasks`

Fetches a list of tasks with pagination.

**Query Parameters:**
- `skip`: Number of items to skip (for pagination).
- `limit`: Number of items to return (for pagination).

**Response:**

```json
{
  "status": "success",
  "status_code_message": "Tasks fetched successfully",
  "data": [
    {
      "id": "bd454eb3-878e-4e93-bf66-d2632155efd5",
      "title": "task 1",
      "description": "something",
      "status": "pending",
      "created_at": "2025-04-22T18:57:16.310204",
      "updated_at": "2025-04-22T18:57:16.310208"
    }
  ]
}
```

### Get Task by ID

- **GET** `/api/v1/tasks/{task_id}`

Fetch a task by its `task_id`.

**Response:**

```json
{
  "status": "success",
  "status_code_message": "Task fetched successfully",
  "data": {
    "id": "bd454eb3-878e-4e93-bf66-d2632155efd5",
    "title": "task 1",
    "description": "something",
    "status": "pending",
    "created_at": "2025-04-22T18:57:16.310204",
    "updated_at": "2025-04-22T18:57:16.310208"
  }
}
```

### Update Task

- **PUT** `/api/v1/tasks/{task_id}`

Updates a task by its `task_id`.

**Request Body:**

```json
{
  "title": "updated task",
  "status": "in-progress"
}
```

**Response:**

```json
{
  "status": "success",
  "status_code_message": "Task updated successfully",
  "data": {
    "id": "bd454eb3-878e-4e93-bf66-d2632155efd5",
    "title": "updated task",
    "description": "something",
    "status": "in-progress",
    "created_at": "2025-04-22T18:57:16.310204",
    "updated_at": "2025-04-22T18:57:16.310208"
  }
}
```

### Delete Task

- **DELETE** `/api/v1/tasks/{task_id}`

Deletes a task by its `task_id`.

**Response:**

```json
{
  "status": "success",
  "status_code_message": "Task deleted successfully",
  "data": []
}
```

## Database

The application uses PostgreSQL as its database. You can configure the database connection in the `.env` file.

