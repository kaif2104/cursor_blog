# Blog System

A simple and elegant blog web application built with Django and Bootstrap. This project demonstrates the implementation of a complete blog system with user authentication, CRUD operations, and a responsive UI.

## Features

### Core Features
- ✅ **User Authentication**: Register, login, and logout functionality
- ✅ **Blog Post Management**: Create, read, update, and delete blog posts
- ✅ **User Authorization**: Only post authors can edit/delete their own posts
- ✅ **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- ✅ **Flash Messages**: Success/error notifications for user actions
- ✅ **Pagination**: Paginated post list for better performance
- ✅ **Template Inheritance**: Clean, maintainable code structure

### Technical Features
- **MVC Pattern**: Proper separation of models, views, and templates
- **Form Handling**: Django forms with validation and error handling
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **SQLite Database**: Lightweight database for development
- **Admin Interface**: Django admin for content management

## Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **Database**: SQLite3
- **Icons**: Font Awesome 6.0.0
- **Language**: Python 3.x

## Project Structure

```
blog_cursor/
├── blog/                    # Main blog application
│   ├── models.py           # Post model
│   ├── views.py            # View functions and classes
│   ├── forms.py            # User registration and post forms
│   ├── urls.py             # URL patterns
│   └── admin.py            # Admin interface configuration
├── blog_system/            # Django project settings
│   ├── settings.py         # Project configuration
│   └── urls.py             # Main URL configuration
├── templates/              # HTML templates
│   ├── base.html           # Base template with navigation
│   └── blog/               # Blog-specific templates
│       ├── home.html       # Home page
│       ├── register.html   # User registration
│       ├── login.html      # User login
│       ├── post_list.html  # List of all posts
│       ├── post_detail.html # Single post view
│       ├── post_form.html  # Create/edit post form
│       └── post_confirm_delete.html # Delete confirmation
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone and Navigate
```bash
cd blog_cursor
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Usage

### For Users
1. **Register**: Create a new account with username, email, and password
2. **Login**: Sign in with your credentials
3. **Create Posts**: Write and publish blog posts
4. **View Posts**: Browse all published posts
5. **Edit/Delete**: Manage your own posts

### For Administrators
1. **Admin Access**: Login to Django admin at `/admin/`
2. **User Management**: Manage users and their permissions
3. **Content Management**: Moderate and manage all blog posts

## Features Breakdown

### Task 1: Project Setup ✅
- Django installation and project creation
- Virtual environment setup
- Git repository initialization
- Basic folder structure

### Task 2: Home Page ✅
- Welcome page with navigation
- Responsive design with Bootstrap
- Call-to-action buttons

### Task 3: User Registration ✅
- User registration form with validation
- Email and password requirements
- Automatic login after registration

### Task 4: User Login & Logout ✅
- Secure authentication system
- Session management
- Logout functionality

### Task 5: Create Blog Post ✅
- Post creation form
- Author association
- Form validation

### Task 6: View Blog Posts ✅
- Post listing with summaries
- Author and date information
- "Read more" links

### Task 7: Edit and Delete Posts ✅
- Author-only edit/delete permissions
- Confirmation dialogs
- Secure access control

### Task 8: UI Enhancement ✅
- Bootstrap 5 styling
- Template inheritance
- Responsive navigation
- Mobile-friendly design

### Task 9: Flash Messages ✅
- Success/error notifications
- User feedback for all actions
- Dismissible alerts

## Optional Bonus Features

The following features can be easily added to extend the functionality:

- **Categories/Tags**: Add categorization to posts
- **Image Upload**: Allow image attachments to posts
- **Comments System**: Enable user comments on posts
- **Like System**: Add post liking functionality
- **Search**: Implement post search functionality
- **User Profiles**: Extended user profile information

## Development

### Running Tests
```bash
python manage.py test
```

### Creating New Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Font Awesome for icons
- Django Community

---

**Built with ❤️ using Django and Bootstrap** 