# Python Virtual Environment Setup

This guide will walk you through setting up a Python virtual environment, activating it, and installing all the dependencies specified in a `requirements.txt` file.

## Prerequisites

- Python must be installed on your machine. Ensure you have Python 3 installed.
- A `requirements.txt` file with a list of Python dependencies is available in the same directory as your Python project.

## Steps

### 1. Clone the Project

First, clone the project repository:

```shell
git clone https://github.com/RishavYaduvanshi/VendorManagement.git
```

### 2. Create a Python Virtual Environment

Navigate to the cloned project directory and create a virtual environment using the following command:

```shell
python -m venv env
```

### 3. Activate the Virtual Environment

Next, activate the virtual environment using the appropriate command for your operating system

- For Windows:

```shell
.\env\Scripts\activate
```

- For macOS and Linux:

```shell
source env/bin/activate
```
### 4. Install Dependencies from "requirements.txt"

With the virtual environment activated, you can install all the dependencies specified in the requirements.txt file using the following command:

```shell
pip install -r requirements.txt
```

### 5. Navigate to the vendormetric Directory

```shell
cd vendormetric
```
### 6. Run the server
```shell
python manage.py runserver
```
### Once the server is running, you can access the following endpoints:
- Vendors: http://localhost:8000/api/vendors/
- Purchase Orders: http://localhost:8000/api/purchase_orders/
- API Documentation (Swagger UI):  http://localhost:8000/api/docs/swagger-ui/