# 📘 Enhanced Calculator Command-Line Application (Midterm Project)

## 📌 Project Overview

This project is an advanced command-line calculator application developed as part of the midterm assignment. The application implements multiple design patterns, robust error handling, configuration management, history persistence, and continuous integration using GitHub Actions.

The calculator supports advanced arithmetic operations, undo/redo functionality, automatic history saving, logging, and comprehensive unit testing with enforced code coverage.

---

## 🏗️ Design Patterns Implemented

This project demonstrates the following software design patterns:

* **Factory Pattern** – Used to dynamically create arithmetic operation objects.
* **Memento Pattern** – Used to implement undo and redo functionality.
* **Observer Pattern** – Used for:

  * Logging calculations
  * Automatically saving history to CSV
* **Modular OOP Design** – Clean separation of concerns using classes and modules.

---

## ✨ Features

### 🔢 Arithmetic Operations

The calculator supports the following operations:

* add
* subtract
* multiply
* divide
* power
* root
* modulus
* int_divide
* percent
* abs_diff

Each operation takes exactly two numerical inputs.

---

### 🔁 History Management

* Stores all calculations in memory
* Supports:

  * `undo`
  * `redo`
  * `history`
  * `clear`

Undo/redo is implemented using the Memento pattern.

---

### 💾 Data Persistence (CSV)

* Automatic save of history after each calculation
* Manual save using `save` command
* Load history from CSV using `load` command
* Uses pandas for serialization and deserialization
* Stores:

  * operation
  * operand1
  * operand2
  * result
  * timestamp

---

### 📝 Logging

* All calculations logged to a file
* Uses Python's `logging` module
* Supports INFO and ERROR levels
* Log file location configured via `.env`

---

### ⚙️ Configuration Management

Application settings are managed using:

* `.env` file
* `python-dotenv`

Configurable parameters include:

* Log directory
* History directory
* Maximum history size
* Auto-save setting
* Calculation precision
* Maximum input value
* Default file encoding

Default values are provided if environment variables are missing.

---

## 📂 Project Structure

```
midterm-enhanced-calculator/
│
├── app/
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── operations.py
│   └── logger.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_operations.py
│   └── test_calculation.py
│
├── .env
├── requirements.txt
├── README.md
└── .github/workflows/python-app.yml
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/midterm-enhanced-calculator.git
cd midterm-enhanced-calculator
```

---

### 2️⃣ Create Virtual Environment (Mac/Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration (.env Setup)

Create a `.env` file in the root directory with the following variables:

```
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
```

The application will create log and history folders automatically if they do not exist.

---

## 🖥️ Running the Calculator

Run the application using:

```bash
python -m app.calculator
```

You will see:

```
Enhanced Calculator (type 'help' for commands, 'exit' to quit)
```

---

## 🧾 Available Commands

| Command        | Description                |
| -------------- | -------------------------- |
| add a b        | Addition                   |
| subtract a b   | Subtraction                |
| multiply a b   | Multiplication             |
| divide a b     | Division                   |
| power a b      | Exponentiation             |
| root a b       | Nth root                   |
| modulus a b    | Remainder                  |
| int_divide a b | Integer division           |
| percent a b    | Percentage calculation     |
| abs_diff a b   | Absolute difference        |
| history        | Show history               |
| clear          | Clear history              |
| undo           | Undo last operation        |
| redo           | Redo last undone operation |
| save           | Manually save history      |
| load           | Load history from CSV      |
| help           | Show commands              |
| exit           | Exit application           |

---

## 🧪 Running Unit Tests

Run all tests:

```bash
pytest -v
```

Run with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

Minimum required coverage:

```
>= 90%
```

Current coverage:

```
91%
```

---

## 🔄 Continuous Integration (CI/CD)

This project uses **GitHub Actions**.

The workflow automatically:

* Installs dependencies
* Runs all unit tests
* Enforces minimum 90% coverage
* Fails if coverage drops below threshold

Workflow file:

```
.github/workflows/python-app.yml
```

CI runs on:

* Every push to `main`
* Every pull request to `main`

---

## 🛡️ Error Handling

Custom exceptions implemented:

* `CalculatorError`
* `ValidationError`
* `OperationError`
* `FileOperationError`

Handles:

* Division by zero
* Invalid operations
* Invalid input
* File errors
* Out-of-range values

---

## 📚 Learning Outcomes Achieved

This project demonstrates:

* GIT version control
* Linux command execution
* Object-oriented programming
* Design pattern implementation
* CSV manipulation with pandas
* REPL-based CLI development
* Automated testing with pytest
* Test coverage enforcement
* CI/CD pipeline integration

---

## 🎯 Conclusion

This enhanced calculator application demonstrates professional software engineering practices, including modular design, automated testing, configuration management, logging, persistence, and CI/CD integration.

The project meets all assignment requirements and exceeds the minimum test coverage threshold.

---

# ✅ After Pasting This

1. Save README.md
2. Commit it:

```bash
git add README.md
git commit -m "Add complete professional README documentation"
git push
```

