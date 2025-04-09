# Quora Clone

A Django-based web application that replicates the core functionality of Quora, allowing users to ask questions, provide answers, and interact with content through likes.

## Features

### User Authentication
- User registration and login system
- Secure password handling
- User-specific content management

### Questions
- Create new questions with title and content
- View all questions on the home page
- View detailed question pages
- Edit questions (author only)
- Delete questions (author only)
- View question author and creation date

### Answers
- Post answers to questions
- View all answers for a question
- Edit answers (author only)
- Delete answers (author only)
- View answer author and creation date

### Social Features
- Like/unlike answers
- View who liked an answer
- See like counts for answers
- Real-time like updates without page refresh

## Technology Stack

- **Backend**: Django
- **Frontend**: Basic HTML/CSS
- **Database**: PostGresSQL
- **Authentication**: Django's built-in authentication system

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd quora_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at `http://127.0.0.1:8000/`

## Project Structure

```
quora_project/
├── manage.py
├── quora_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quora_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates/
    ├── base.html
    ├── home.html
    ├── post_question.html
    ├── question_detail.html
    ├── edit_question.html
    ├── delete_question.html
    ├── edit_answer.html
    └── delete_answer.html
```

## Usage

1. **Registration and Login**
   - New users can register through the registration page
   - Existing users can log in using their credentials

2. **Questions**
   - Click "Post Question" to create a new question
   - View all questions on the home page
   - Click on a question to view its details and answers
   - Edit or delete your own questions using the respective buttons

3. **Answers**
   - On a question's detail page, scroll down to post an answer
   - View all answers for the question
   - Edit or delete your own answers using the respective buttons

4. **Likes**
   - Click the like button on any answer to like/unlike it
   - View who liked an answer below the like count
   - Like counts update in real-time without page refresh

## Security Features

- CSRF protection on all forms
- User authentication required for all actions
- Author-only access to edit and delete functionality
- Secure password handling
- Session-based authentication

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django framework
- Bootstrap for frontend styling
- Font Awesome for icons 