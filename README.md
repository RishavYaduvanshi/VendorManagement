# Python Virtual Environment Setup

This guide will walk you through setting up a Python virtual environment, activating it, and installing all the dependencies specified in a `requirements.txt` file.

## Prerequisites

- Python must be installed on your machine. Ensure you have Python 3 installed.
- A `requirements.txt` file with a list of Python dependencies is available in the same directory as your Python project.

## Steps

### 1. Create a Python Virtual Environment

First, create a virtual environment using the following command:

```shell
python -m venv env
```

### 2. Activate the Virtual Environment

Next, activate the virtual environment using the appropriate command for your operating system:

```shell
.\env\Scripts\activate
```
### 3. Install Dependencies from requirements.txt

With the virtual environment activated, you can install all the dependencies specified in the requirements.txt file using the following command:

```shell
pip install -r requirements.txt
```

### 4. Navigate to the vendormetric Directory

```shell
cd vendormetric
```
### 4. Run the server
```shell
python manage.py runserver
```
### There are three endpoints
##### 1. "vendors": "http://localhost:8000/api/vendors/"
##### 2. "purchase_orders": "http://localhost:8000/api/purchase_orders/"
##### 3. "Doumnents "http://localhost:8000/api/docs/swagger-ui/