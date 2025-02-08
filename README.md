# Basic CRUD Application

A simple CRUD (Create, Read, Update, Delete) application built with Flask. This project is designed to be deployed on an OpenStack VM and serves as a basic example of how to implement a CRUD application in a server environment.

## Description

This is a pretty basic items list application. I created this CRUD to demonstrate how to install and run a CRUD application on a server using OpenStack. The application is written in Spanish, so if you intend to use it for the same purpose, make sure to change the language or modify it as needed.

## Features

- **Create**: Add new items with a name and description.
- **Read**: View a list of all items.
- **Update**: Edit existing items.
- **Delete**: Remove items from the list.
- **Validation**: Ensures the name field is not empty.
- **Flash Messages**: Success and error messages for user feedback.
- **Confirmation Dialog**: Confirmation before deleting an item.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/FOXYTHEPIRATE21/Basic-CRUD.git
   cd Basic-CRUD
   ```

2. Install the required dependencies. **If you're working in a VM, it's recommended to create a virtual environment first**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to view the application.

## Usage

- **Create Item**: Fill out the form with the item's name and description to add a new item to the list.
- **Edit Item**: Click the "Editar" button next to an item to modify its name and description.
- **Delete Item**: Click the "Eliminar" button next to an item to remove it from the list.

## Recommendations for Working with CRUD in a VM

When deploying or working with CRUD applications in a VM, consider the following tips:

1. **Use Virtual Environments**: Always create a virtual environment to isolate dependencies and avoid conflicts with the system's Python installation.
2. **Secure Your Application**: Ensure your Flask app is running in a secure environment, especially if it's exposed to the internet. Use environment variables for sensitive data like `SECRET_KEY`.
3. **Persistent Storage**: For production, avoid storing data in memory (like the `items` dictionary in this example). Use a database like SQLite, PostgreSQL, or MySQL.
4. **Automate Deployment**: Use tools like Ansible, Docker, or shell scripts to automate the deployment process on your VM.
5. **Monitor Resources**: Keep an eye on the VM's resource usage (CPU, memory, etc.) to ensure the application runs smoothly.

## Contributing

If you're interested in exploring a basic CRUD application or want to implement it with the same focus as I did (deploying it in a VM), feel free to use this project as a starting point. Enjoy the journey into the world of virtual machines and technology! 🚀

## Acknowledgments

- Flask for providing a simple and flexible framework.
- OpenStack for the VM environment.