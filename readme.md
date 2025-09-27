<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ranaahmd/Banking-project">
    <img src="image/bank.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Banking With Python</h3>

<p align="center">
ACME Bank Management System (Python Project)<br>
This project is a terminal-based banking application developed in Python using OOP, file handling, and exception handling. It manages customer accounts stored in a CSV file (`bank.csv`) and provides core banking functionalities including adding new customers, depositing/withdrawing money, transferring funds, and implementing overdraft protection.  
The system follows a test-driven development (TDD) approach and supports automatic/manual customer ID generation, password verification, and transaction logging.
</p>
</div>

---

## Table of Contents
- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Example of Code I'm Proud Of](#example-of-code-im-proud-of)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

---

## About The Project
This project simulates a banking system with the following functionalities:
- Add new customers with checking and/or savings accounts  
- Deposit and withdraw money from accounts  
- Transfer money between accounts or to other customers  
- Overdraft protection with limits, fees, and account activation/deactivation rules  

---

## Built With
- **Python 3** – Core programming language  
- **CSV Module** – For reading/writing customer and transaction data  
- **OOP (Classes & Methods)** – To structure accounts, customers, and transactions  
- **Exception Handling** – For robust error management  
- **Unittest / TDD** – Test-driven development for functionality verification  
- **Git & GitHub** – Version control and project management  

---

## Example of Code I'm Proud Of
I spent a lot of time learning from multiple programming languages and YouTube tutorials to fully understand this concept. I really enjoyed working on it.  

This section handles core account operations for customers, including:  
1. Depositing money into checking or savings accounts  
2. Withdrawing money with error handling if the account type doesn’t exist  
3. Transferring funds between a customer’s own accounts  
4. Transferring money to another customer in the same bank, with verification and proper logging  

It demonstrates my understanding of **OOP principles, method delegation, and safe transaction handling**.

---

## Prerequisites
- Python 3.10 or higher  
- CSV file `bank.csv` with customer data  
- Recommended: virtual environment for dependencies  

---

## Installation
1. **Install Python**  
Make sure Python 3.10 or higher is installed from [python.org](https://www.python.org/).

2. **Open the project in VS Code**  
- Open VS Code  
- Go to **File → Open Folder** and select the project folder  

3. **(Optional) Set up a virtual environment**  
```bash
python -m venv venv
# Activate environment:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
