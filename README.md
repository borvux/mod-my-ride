# Mod My Ride (MMR)

Mod My Ride is a Python desktop application built with the Flet framework that allows users to select a car model and visualize various modifications. It features user authentication via Firebase and a MySQL backend to store car data and user information.

## Features

* **User Authentication:**
    * Sign up for a new account.
    * Login for existing users.
    * Forgot password functionality.
    * Firebase for secure authentication.
    * Option to continue as a Guest.
* **Car Selection:**
    * Select car by Make, Model, and Year from a dropdown populated from a MySQL database.
* **Car Visualization:**
    * View a gallery of images for the selected car.
    * Display basic information about the selected car model.
* **Modification Categories:**
    * Browse various modification types:
        * Wheels
        * Decals
        * Vinyl Wraps
        * LED Lighting
        * Additional Mods (e.g., CarPlay, Dash Cam)
    * View images of different modification options within each category.
* **User Profile:**
    * View basic user profile information.
    * Logout functionality.
* **Database Backend:**
    * MySQL database stores car makes, models, years, and user details.
    * Includes schema for modification types.

## Technologies Used

* **Python:** Core programming language.
* **Flet:** GUI framework for creating an installable app or web app.
* **flet-route:** For declarative routing within the Flet application.
* **MySQL:** Relational database for storing application data.
* **mysql-connector-python:** Python driver for MySQL.
* **Firebase Authentication:** For user sign-up and login.
* **Pyrebase4:** Python wrapper for the Firebase API.
* **python-dotenv:** For managing environment variables (database credentials).

## Prerequisites

Before you begin, ensure you have the following installed:
* Python (3.9 or higher recommended, as seen from `.pyc` files)
* MySQL Server
* A Firebase Project

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/mod-my-ride.git](https://github.com/your-username/mod-my-ride.git)
    cd mod-my-ride
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install flet flet-route python-dotenv Pyrebase4 mysql-connector-python
    ```

4.  **MySQL Database Setup:**
    * Ensure your MySQL server is running.
    * Connect to your MySQL server (e.g., using MySQL Workbench, DBeaver, or the command-line client).
    * Create a database named `modmyride` (if it doesn't exist):
        ```sql
        CREATE DATABASE IF NOT EXISTS modmyride;
        ```
    * Use the `modmyride` database:
        ```sql
        USE modmyride;
        ```
    * Import the schema and initial data using the provided `MMR_db.sql` file:
        ```bash
        mysql -u your_mysql_username -p modmyride < MMR_db.sql
        ```
        (Replace `your_mysql_username` with your MySQL username. You will be prompted for the password.)

5.  **Environment Variables for MySQL:**
    Create a `.env` file in the root directory of the project and add your MySQL connection details:
    ```env
    host=localhost
    user=your_mysql_username
    passwd=your_mysql_password
    database=modmyride
    ```
    Replace placeholders with your actual MySQL credentials.

6.  **Firebase Setup:**
    * Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project (or use an existing one).
    * In your Firebase project, go to **Authentication** (under Build) -> **Sign-in method** tab and enable **Email/Password** as a sign-in provider.
    * Go to **Project settings** (click the gear icon next to Project Overview) -> **General** tab.
    * Scroll down to "Your apps" and click on the **Web** icon (`</>`) to register a new web app.
    * Give your app a nickname and click "Register app".
    * Firebase will provide you with a configuration object. You'll need these details.

7.  **Firebase Configuration File:**
    Create a `config.py` file in the **root directory** of the project (this file is listed in `.gitignore`, so you'll need to create it manually). Add the following function, replacing the placeholder values with your actual Firebase project credentials obtained in the previous step:
    ```python
    # config.py
    def firebase_config():
        return {
            "apiKey": "YOUR_FIREBASE_API_KEY",
            "authDomain": "YOUR_FIREBASE_AUTH_DOMAIN",
            "databaseURL": "YOUR_FIREBASE_DATABASE_URL", # Often your project ID + .firebaseio.com or can be "" if not using Realtime DB directly
            "projectId": "YOUR_FIREBASE_PROJECT_ID",
            "storageBucket": "YOUR_FIREBASE_STORAGE_BUCKET", # Often your project ID + .appspot.com
            "messagingSenderId": "YOUR_FIREBASE_MESSAGING_SENDER_ID",
            # "serviceAccount": None, # Keep as None or path to service account JSON if needed for admin tasks (not typical for client-side auth)
        }
    ```
    *Note: The `databaseURL` might be an empty string (`""`) if you are only using Firebase for Authentication and not its Realtime Database directly through Pyrebase for this app's core features.*

8.  **CRITICAL - Adjust Asset Paths:**
    The application currently uses **absolute local paths** for images. **These paths will not work on any other machine.**

## How to Run

Once all prerequisites and setup steps are completed:

1.  Ensure your MySQL server is running.
2.  Make sure your virtual environment is activated (if you created one).
3.  Run the main application file from the project's root directory:
    ```bash
    python _0main.py
    ```
    The Flet application window should open.

## Troubleshooting / Known Issues

* **Absolute Image Paths:** As mentioned in the setup, the hardcoded absolute image paths **must be changed** to relative paths for the application to find assets correctly on different machines or when deployed.
* **MySQL Connection:** Ensure your MySQL server is running and the credentials in your `.env` file are correct and have permissions for the `modmyride` database.
* **Firebase Configuration:** Double-check that `config.py` is created correctly with your Firebase project's web app credentials.

## Future Enhancements (Ideas)

* Implement user-specific saved car configurations.
* Allow users to upload their own car images.
* Expand the database of cars and modification parts.
* Add an admin interface for managing cars and modifications.
* Improve UI/UX for selecting and applying mods.
* Package the Flet app for distribution (e.g., as an executable).
