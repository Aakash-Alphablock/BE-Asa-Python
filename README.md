# Nexus

Nexus is a Django project for ASA python backend

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Features
Contains code related to ASA and other services

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. **Clone the repository**:

    ```bash
    git clone git@github.com:Alphablocks-AI/BE-Asa.git
    cd nexus
    ```

2. **Create and activate a virtual environment**:

    ```bash
    cd ..
    python -m venv nexus_backend
    source nexus_backend/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install backend dependencies**:

    ```bash
    cd nexus
    pip install -r requirements-local.txt
    ```

4. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## Usage

- **API Endpoints**: Documentation for API endpoints can be generated using tools like Swagger or Postman.
- **Admin Interface**: Access the Django admin at `/admin`.

## Running Tests

To run tests, use the following command:

```bash
python manage.py test -s
.