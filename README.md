# space-tigers

This web application was developed by Nick J. Petrone and Luis Cruz Sanchez as part of the Washington Vets to Tech (WaV2T) program. We developed application over the course of a few weeks utilizing the Django framework, gaining significant insights into web application development in the process.

Luis took the lead on the front-end, implementing the 3D-model display, cart functionality, and most of the theming. Meanwhile, Nick focused on the back-end, handling user accounts, authentication, and profile functionalities.

## Instructions to View

### Setting Up a Virtual Environment

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Virtualenv**: Open your terminal or command prompt and run:
    ```sh
    pip install virtualenv
    ```

3. **Create a Virtual Environment**: Navigate to the project directory and create a virtual environment:
    ```sh
    cd /<PROJECT-PATH>/space-tigers
    virtualenv venv
    ```

4. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

5. **Install Dependencies**: With the virtual environment activated, install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

6. **Run the Application**: Finally, start the Django development server:
    ```sh
    python manage.py runserver
    ```

7. **View the Application**: Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

### Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment by running:
```sh
deactivate
```
