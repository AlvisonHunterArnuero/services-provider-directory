# Service Provider Directory

A lightweight, high-performance web application and RESTful API that serves as a directory for local service professionals (e.g., developers, carpenters, electricians, doctors). It provides a clean, modern user interface for visitors to browse professionals and a robust backend for managing data.

CURRENT UI DEMO
![SERVICE PROVIDER - UI DEMO](https://res.cloudinary.com/alvison-hunter/image/upload/v1777688440/starwars/ccl%20team/SERVICE_PROVIDER_-_UI_DEMO_jd0wjo.jpg "SERVICE PROVIDER - UI DEMO")

## Features

- **Modern UI/UX**: Built with standard HTML, Tailwind CSS, and DaisyUI for a beautiful, responsive, and mobile-friendly experience.
- **Modular Architecture**: Frontend Javascript logic and Jinja UI components are cleanly decoupled for maintainability.
- **Provider Profiles**: Detailed profiles showing trade, contact info, bio, hourly rates, social links (LinkedIn/GitHub), and verification status.
- **Review System**: Users can leave 1-to-5 star reviews with comments.
- **Anti-Spam Protection**: The review system tracks IP addresses to ensure a "one review per provider per person" rule.
- **Interactive API Documentation**: A built-in, OpenAPI-style documentation page mimicking Swagger UI, accessible via `/api-docs`.
- **Database Seeding**: Includes a `seed.py` script to easily reset the database and populate it with realistic dummy data.
- **Automated Testing**: Complete Pytest test suite for backend API routes and models using an isolated in-memory SQLite database.

## Technology Stack

- **Backend**: Python 3, Flask, Flask-SQLAlchemy
- **Database**: PostgreSQL (hosted on Neon Tech)
- **Frontend**: Jinja2 Templates, Tailwind CSS (CDN), DaisyUI (CDN)
- **Environment Management**: python-dotenv

## Local Setup Instructions

Follow these steps to run the application locally:

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd CommentMngr
```

### 2. Create a Virtual Environment
It is highly recommended to use a Python virtual environment.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your PostgreSQL connection string:
```ini
DATABASE_URL=postgresql://user:password@hostname/dbname
```
*(Note: If your Neon connection string starts with `postgres://`, the application will automatically convert it to `postgresql://` as required by SQLAlchemy.)*

### 5. Initialize the Database
Run the provided seeding script. This will drop existing tables, recreate them with the latest schema, and insert dummy service providers and reviews.
```bash
python seed.py
```

### 6. Run the Application
Start the Flask development server:
```bash
python main.py
```
The application will be available at `http://localhost:5001` (or your network IP).

### 7. Run the Test Suite
We enforce testing standards via Pytest. The test suite automatically uses an isolated in-memory SQLite database, guaranteeing that your real database is never touched. To run the tests:
```bash
python -m pytest -v
```

## API Endpoints

The application features a fully documented RESTful JSON API. You can view the interactive documentation by navigating to the **API Docs** link in the application's navigation bar, or by referencing the routes below:

### Providers
- `GET /providers` - Retrieve all service providers.
- `POST /providers` - Create a new provider profile.
- `GET /providers/<pro_id>` - Retrieve details for a specific provider.
- `PUT /providers/<pro_id>` - Update an existing provider.
- `DELETE /providers/<pro_id>` - Delete a provider (cascades to their reviews).

### Reviews
- `GET /providers/<pro_id>/reviews` - Retrieve all reviews for a specific provider.
- `POST /providers/<pro_id>/reviews` - Submit a new review for a provider. (Enforces IP-based uniqueness constraints).

## Project Structure

- `main.py`: The core Flask application, routing, and endpoint logic.
- `models.py`: SQLAlchemy database models (`Provider` and `Review`).
- `seed.py`: Utility script for database initialization and dummy data injection.
- `requirements.txt`: Python package dependencies.
- `templates/`: Directory containing Jinja2 HTML templates and reusable partials.
- `static/`: Directory containing modular Javascript (`func/`) and other static assets.
- `tests/`: Directory containing the Pytest automated testing suite (`conftest.py`, `test_models.py`, `test_routes.py`).

### Proudly created by Alvison Hunter Arnuero
Last updated: Saturday, May 2nd, 2026
