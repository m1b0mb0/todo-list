# TODO List

A Django web application for managing tasks and tags. The project includes task CRUD, tag CRUD, deadline selection, and a status toggle for marking tasks as completed or not completed.

## Features

- View all tasks
- Create, update, and delete tasks
- Mark tasks as `Done` or return them to `Not done`
- Add optional task deadlines
- Assign multiple tags to tasks
- Create, update, and delete tags
- Manage tasks and tags through the Django admin panel

## Tech Stack

- Python
- Django 6.0.5
- SQLite
- Bootstrap 4
- django-crispy-forms
- crispy-bootstrap4

## Project Structure

```text
todo-list/
|-- tasks/
|   |-- forms.py
|   |-- models.py
|   |-- urls.py
|   `-- views.py
|-- templates/
|   |-- base.html
|   |-- includes/
|   |   `-- sidebar.html
|   `-- tasks/
|       |-- task_form.html
|       |-- task_list.html
|       |-- task_confirm_delete.html
|       |-- tag_form.html
|       |-- tag_list.html
|       `-- tag_confirm_delete.html
|-- static/
|   `-- css/
|       `-- styles.css
|-- todo_list/
|   |-- settings.py
|   `-- urls.py
|-- manage.py
|-- requirements.txt
`-- README.md
```

## Models

### Task

- `content` - task text
- `created_at` - date and time when the task was created
- `deadline` - optional task deadline
- `is_completed` - task status
- `tags` - related tags

### Tag

- `name` - unique tag name

## URLs

| URL | Name | Description |
| --- | --- | --- |
| `/tasks/` | `tasks:task-list` | Task list |
| `/tasks/create/` | `tasks:task-create` | Create task |
| `/tasks/<pk>/update/` | `tasks:task-update` | Update task |
| `/tasks/<pk>/delete/` | `tasks:task-delete` | Delete task |
| `/tasks/<pk>/toggle-status/` | `tasks:task-toggle-status` | Toggle task completion status |
| `/tags/` | `tasks:tag-list` | Tag list |
| `/tags/create/` | `tasks:tag-create` | Create tag |
| `/tags/<pk>/update/` | `tasks:tag-update` | Update tag |
| `/tags/<pk>/delete/` | `tasks:tag-delete` | Delete tag |
| `/admin/` | `admin` | Django admin panel |

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd todo-list
```

### 2. Create and Activate a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open the app at:

```text
http://127.0.0.1:8000/tasks/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```
