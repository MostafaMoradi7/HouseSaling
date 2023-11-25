# House Selling API

This Django Rest Framework (DRF) project provides an API for managing and selling houses. It includes functionality for creating, updating, and deleting house listings, as well as handling user registration.

## Installation

1. **Clone the Repository:**
   ```bash
   https://github.com/MostafaMoradi7/HouseSaling.git
   ```

2. **Create a Virtual Environment:** (NOT necessary but recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a .env File:**

In the root directory of the project, create a file named .env
Copy the contents of the provided .env.sample file and paste them into .env
Update Environment Variables:

Open the .env file and provide values for each environment variable.
Update database credentials, secret key, and any other necessary configuration.

6. **Database Setup:**
   - Set up a PostgreSQL database.
   - Update the database configuration in `config/settings.py`.

7. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```


8. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the API:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


## API Documentation

- **API Schema (JSON):** [http://127.0.0.1:8000/schema/](http://127.0.0.1:8000/schema/)
- **Swagger UI:** [http://127.0.0.1:8000/schema/swagger-ui/](http://127.0.0.1:8000/schema/swagger-ui/)

## House Listing Operations

- **Create a House Listing:** Send a POST request to `/api/houses/` with the required data.
- **Update a House Listing:** Send a PUT request to `/api/houses/<unique_id>/` with the updated data.
- **Buy a House:** Send a PATCH request to `/api/houses/<unique_id>/` with the buyer's information.
- **Delete a House Listing:** Send a DELETE request to `/api/houses/<unique_id>/`.

## User Registration

- **Register a User:** Send a POST request to `/user/register/` with the user's information.

## Authentication

The API uses JWT (JSON Web Token) authentication. Include the token in the Authorization header of your requests with the format `Bearer <token>`.
