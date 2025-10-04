📝 Django To-Do List App

A simple and elegant To-Do List web app built with Django, allowing users to efficiently manage daily tasks.
Includes authentication, task CRUD operations, and a clean, responsive design.

🚀 Features

🔐 User Registration & Login

➕ Add, ✏️ Edit, ❌ Delete Tasks

✅ Mark tasks as complete/incomplete

🔍 Search tasks by title

👤 Each user has their own private task list

🎨 Minimal, responsive UI using Flexbox

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS (Flexbox)

Database: SQLite

Authentication: Django’s built-in auth system

⚙️ Installation & Setup

# 1️⃣ Clone this repository
git clone https://github.com/<your-username>/django-todo-list.git
cd django-todo-list

# 2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # (Windows)
# or
source venv/bin/activate     # (Mac/Linux)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run migrations
python manage.py migrate

# 5️⃣ Start the development server
python manage.py runserver
Now open your browser and visit http://127.0.0.1:8000/
 🎉


 todo_list/
│
├── base/
│   ├── migrations/
│   ├── templates/
│   │   ├── base/
│   │   │   ├── task_list.html
│   │   │   ├── task_form.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── delete_task.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── todo_list/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt



🤝 Contributing

Pull requests are welcome!
If you find a bug or have an idea to improve the project, open an issue or submit a PR.
