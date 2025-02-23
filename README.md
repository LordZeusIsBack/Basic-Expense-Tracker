# Basic Expense Tracker

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)

## Overview

The **Basic Expense Tracker** is a Django-based web application designed to help users manage and track their expenses efficiently. With a user-friendly interface and robust backend, it offers features such as:

- Recording daily expenses
- Categorizing expenditures
- Viewing detailed expense reports
- Managing budgets

## Features

- **User Authentication**: Secure login and registration system.
- **Expense Management**: Add, edit, and delete expenses with ease.
- **Categorization**: Organize expenses into predefined or custom categories.
- **Reporting**: Visualize spending habits through dynamic charts and summaries.
- **Responsive Design**: Accessible on various devices, including desktops, tablets, and smartphones.

## Getting Started

Follow these steps to set up the project locally:

### Prerequisites

Ensure you have the following installed:

- Python 3.11
- pip (Python package installer)
- virtualenv (for creating isolated Python environments)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/LordZeusIsBack/Basic-Expense-Tracker.git
   cd Basic-Expense-Tracker
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Project Structure

```
Basic-Expense-Tracker/
├── expense_tracker/      # Main application directory
├── tracker/              # Project configuration directory
├── manage.py             # Django management script
├── requirements.txt      # List of dependencies
├── .gitignore            # Git ignore file
└── LICENSE               # License information
```

## Dependencies

The project relies on the following Python packages:

- Django==4.2.2
- djangorestframework==3.14.0
- pytz==2023.3
- sqlparse==0.4.4
- tzdata==2023.3

These are specified in the `requirements.txt` file.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Developed by [Anubhav Sharma](https://github.com/LordZeusIsBack).
