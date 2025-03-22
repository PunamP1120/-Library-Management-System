# -Library-Management-System
## Features
- Admin can **add, update, delete, and view** books.
- Students can **view available books**.
- RESTful API with MySQL database.

## Setup Instructions

1. **Clone the repository**
   ```bash
  git clone https://github.com/yourusername/library-management.git
cd library-management

2. **Create and Activate a Virtual Environment**
   python -m venv venv
   .\venv\Scripts\activate
   
3. **Install Dependencies**
   pip install -r requirements.txt

4.**Install MySQL and Configure Database**
 Ensure MySQL is installed.
 Open MySQL and create a new database:
CREATE DATABASE library_management;

5. **Update settings.py with your MySQL credentials:**
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_management',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6.**Run Migration**
  python manage.py makemigrations
  python manage.py migrate

7. **Create a Superuser (Admin)** 
 python manage.py createsuperuser

8. **Start the Server**
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

9.**API Endpoints**

Authentication:
POST /api/register/ - Register a new admin
POST /api/login/ - Login and get token

Book Management (Admin Only):
POST /api/books/ - Add a book
GET /api/books/ - List all books
PUT /api/books/<id>/ - Update a book
DELETE /api/books/<id>/ - Delete a book

Student View:
GET /api/students/books/ - View all books (Read-only)

