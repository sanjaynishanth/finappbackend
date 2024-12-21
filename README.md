# finapp-backend

# finapp-backend

This repository contains the **backend** for the finapp.
The backend is built using **FastAPI** and **PostgreSQL** for database management.

---

## Requirements
Ensure you have the following installed before running the project:
- **Python 3.8+**
- **PostgreSQL**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

You can install the necessary Python packages using `pip`.

---

## Installation Steps
Follow these steps to set up and run the backend:

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd finapp-backend
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**
   - Create a database in PostgreSQL.
   - Update the database connection string in the code (e.g., `DATABASE_URL` in `config.py`):
     ```python
     DATABASE_URL = "postgresql://username:password@localhost/dbname"
     ```



5. **Start the FastAPI server**
   Use Uvicorn to serve the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```
   - The backend will be available at `http://127.0.0.1:8000`.

---

## API Endpoints
Here are the available API endpoints for **authentication**:

### User Authentication
| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| POST   | `/signup`          | Register a new user           |
| POST   | `/login`           | Log in a user                 |



---


## Notes
- The backend handles authentication and interacts with the PostgreSQL database.
- The **frontend** is managed by a separate team and will connect to this backend.
