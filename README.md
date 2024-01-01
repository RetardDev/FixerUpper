## FixerUpper Setup Guide for Windows Users

### Running the Application
To initiate the application, follow these steps:

1. Open any terminal application on your system. Note: Visual Studio Code terminal is also viable.
2. Ensure you're within the correct file directory, which is ##/FixerUpper.
3. Activate the virtual environment (venv) with the following commands:
    ```
    cd venv/Scripts
    activate.bat
    ```
   After activation, you should see the "(venv)" keyword at the beginning of each line in your terminal.

4. Navigate back to the file directory by executing these commands:
    ```
    cd ..
    cd ..
    ```

### Running the Server
Now, let's start the server. Follow these steps:

1. Access the project directory:
    ```
    cd fixerupper
    ```

2. Launch the server using the command:
    ```
    py manage.py runserver
    ```

If the setup proceeds without errors, you should see the server URL, typically displayed as 127.0.0.1:8000.

### Important Notes
- Most of the data, such as images, names, and prices, resides within the database. For modifications, access the Django admin portal.
  
  Django Admin Portal: [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
  - Credentials: 
    - Username: cryptic 
    - Password: 1234
  
- The `info.txt` file contains userprofile model credentials, also accessible through the Django admin panel.

- To make purchases on the site, create a user account or use the provided 'jamal' credentials for testing purposes.

- HSBC serves as a provider. Note: The provider portal has not been developed and may remain unfinished.










