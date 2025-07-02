# Library Management System

A simple and modern web application for managing a library's collection of books. Built with Django, this project helps you keep track of books, their categories, and their status (available, rented, or sold). The interface is clean, responsive, and supports right-to-left languages.

## Features

- **Book Management:** Add, edit, and delete books with details like title, author, images, pages, price, and rental information.
- **Category Management:** Organize books into categories for easy browsing.
- **Status Tracking:** Mark books as available, rented, or sold, and see statistics at a glance.
- **Dashboard:** View total books, available, sold, and rented counts, plus earnings from sales and rentals.
- **Search:** Quickly find books by title.
- **Modern UI:** Uses Bootstrap, FontAwesome, and Chart.js for a smooth user experience.
- **Admin Panel:** Manage books and categories through Django's built-in admin interface.

## Getting Started

### Prerequisites
- Python 3.8+
- Django 5.x
- (Optional) Virtual environment tool like `venv` or `virtualenv`

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd library_system
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   - Open your browser and go to `http://127.0.0.1:8000/` for the main site.
   - Visit `http://127.0.0.1:8000/admin/` for the admin panel.

## Usage
- Add new books and categories from the homepage.
- Edit or delete books using the action buttons next to each book.
- Use the search bar to find books by title.
- View statistics and earnings on the dashboard.
- Manage all data from the Django admin panel if needed.

## Notes
- The UI is designed for right-to-left languages and includes Arabic labels.
- Images for books and authors are optional but recommended for a better experience.
- This project is intended for educational or small library use. For production, review Django's deployment checklist and security best practices.

## License
This project is open source and available under the MIT License.
