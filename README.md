 # Project Name: Django REST API CRUD Demo

## Description:

This project guides you through building a well-structured and versatile Django REST API that efficiently performs CRUD (Create, Read, Update, Delete) operations on a user-defined model. Designed for both beginners and experienced developers, it provides a solid foundation for exploring more advanced API functionalities.

## Key Features:

- Leverages Django and Django REST for streamlined API development.
- Demonstrates effective CRUD functionality on a custom model.
- Employs serializers for seamless data conversion between JSON and Python objects.
- Offers a clear roadmap for building more intricate APIs.
- Provides practical examples and detailed instructions for easy implementation.

## Target Audience:

- Developers eager to learn Django REST fundamentals.
- Programmers seeking to understand API development using Django.
- Beginners wanting to create CRUD operations with an API interface.

## Getting Started:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Esquire31/Django-Rest.git
   ```

2. **Set Up Your Environment:**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```
   - Install required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

This API provides several endpoints for managing courses:

- **`/` (GET):** Provides an overview of the API and available endpoints.
- **`/courses/` (GET):** Retrieves a list of all courses offered. (Previously named "ViewCourses")
- **`/courses/add/` (POST):** Creates a new course. (Previously named "AddCourse")
- **`/courses/<str:id>/update` (PUT):** Updates an existing course. (Previously named "UpdateCourses")
- **`/courses/<str:id>/delete` (DELETE):** Deletes a specific course. (Previously named "DeleteCourses")

**Path Parameters:**

- `<str:id>`: Represents the unique identifier of a course.

## Project Structure:

- `api`: Contains the application-specific code, including the model and serializers.
- `manage.py`: Django's management script for project operations.
- `requirements.txt`: Lists project dependencies.
- `README.md`: This file.


**Disclaimer:**

This project serves as a foundational example and might require adjustments based on your individual requirements and project complexity.
