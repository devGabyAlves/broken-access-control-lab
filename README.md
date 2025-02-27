# Broken Access Control Demo

This repository contains a laboratory developed in Python with the **Flask** framework, to demonstrate the exploitation of a **Broken Access Control** vulnerability. The goal of this project is to provide a practical way to understand how this vulnerability can be exploited and how to avoid such security holes.

## 🚀 How to Run the Project

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/devGabyAlves/broken-access-control-lab.git
cd broken-access-control-lab 
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Server
```bash
python broken_access_control.py
```

The server will be available at http://127.0.0.1:5000.

### 4. Access the System
Open your browser and go to http://127.0.0.1:5000. You will see the login page. Use the following example credentials to test:

Username: admin, Password: admin123
Username: user, Password: user123

After logging in, you will be able to test the Broken Access Control vulnerability by accessing another user's resources, demonstrating the vulnerability.

## 🛠️ Project Structure
broken_access_control.py: Main file containing the Flask server and access control logic.
login.html: Login page for the system.
dashboard.html: Main page after user login.
resource.html: Displays data for a specific resource.

## 📚 About the Vulnerability
Broken Access Control occurs when an access control system fails to ensure that users can only access the resources they are authorized to. In this project, any user can access other users' resources without restrictions, simulating this security flaw.

## 🚨 How to Exploit the Vulnerability
After logging in, an unauthorized user can directly access resources from another user by using specific URLs (e.g., /resource/1). This happens because the access control system does not properly verify the user's identity and their permission to access the data.

## 🔒 How to Fix It
A simple solution to fix the vulnerability would be to ensure that the server checks if the user is authorized to access the requested resource. For example:

if resource["owner"] != username:
    return "Access denied", 403