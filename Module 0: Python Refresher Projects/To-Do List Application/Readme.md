# 📝 To-Do List Application

A simple command-line **To-Do List Application** built with Python. This project demonstrates the use of Python fundamentals such as data structures, functions, loops, conditionals, file handling, and exception handling.

---

## 📌 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 Automatically save tasks to a JSON file
* 📂 Load saved tasks when the application starts
* ⚠️ Handle invalid user input using exception handling

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)

---

## 📁 Project Structure

```
todo-list/
│
├── main.py          # Main application
├── tasks.json       # Stores tasks (created automatically)
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your computer.

### Run the Application

1. Clone the repository:

```bash
git clone https://github.com/your-username/todo-list.git
```

2. Navigate to the project folder:

```bash
cd todo-list
```

3. Run the program:

```bash
python main.py
```

---

## 📖 How to Use

When you run the program, you will see the following menu:

```
========= TO-DO LIST =========
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
==============================
```

Choose one of the available options by entering its corresponding number.

### Example

```
Choose an option: 1
Enter task: Complete Python assignment
Task added successfully.

Choose an option: 2

------ TO-DO LIST ------
1. [✘] Complete Python assignment
------------------------
```

---

## 💾 Data Storage

Tasks are stored in a file named **`tasks.json`**.

Each task is saved in the following format:

```json
[
    {
        "title": "Complete Python assignment",
        "done": false
    }
]
```

The application automatically loads existing tasks when it starts and saves changes whenever tasks are added, updated, or deleted.

---

## 📚 Python Concepts Used

* Variables and Data Types
* Lists and Dictionaries
* Functions
* Loops (`while`, `for`)
* Conditional Statements (`if`, `elif`, `else`)
* Exception Handling (`try` / `except`)
* File Handling
* JSON Serialization

---

## 🎯 Future Improvements

* Edit existing tasks
* Set task priorities
* Add due dates
* Search for tasks
* Filter completed and pending tasks
* Build a graphical user interface (GUI)
* Add colored terminal output

---

## 👨‍💻 Author

Developed as a Python fundamentals project to practice programming concepts and build a simple, user-friendly command-line application.
