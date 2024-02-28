# CURD Database App
A web-based application that lets you alter and view a SQL database.

## Tools Used
- **Python 3.10**
- **SQL** - Used to create the default `database.db` file
- **SQLite3** - Used in the back-end to handle SQL query logic as needed
- **HTML 5 & CSS 3** - Used to display the front-end web content
- **Flask** - Used in the back-end to host the app on a local server, and HTTP GET/POST calls made by the user
- **virtualenv** - Used to hold the required dependencies in a concentrated area
- **Spotify** - Used to keep me sane while working on this project 🙃

## How to Run
- Download the code as a .zip
- After extracing it, open a terminal in the directory
- Run the following command to activate the Python virtual environment:
`.venv/Scripts/activate` Your terminal should now have the prefix of `(.venv)`. Doing this gives you access to Flask and its shell commands, which we will now use to host the app on your localhost.
- While the virtual environment is activated, type `flask --app db run` to serve the app. By default, this will serve the app on `127.0.0.1:5000`.
- Using any modern web browser, enter the IP address and port (default `127.0.0.1:5000`) into the address bar to access the web app.
- From here you can interact with the app as you see fit.
- Whenever you wish to finish, use CTRL+C in the terminal to interrupt Flask. Then, type `deactivate` into the shell to leave the virtual environment.

## Resetting the Database
If for some reason you must reset the database back to its initial state, please run the following command in a terminal opened in the activated virtual environment:
`sqlite3.exe database.db ".read database.sql"`
- **IMPORTANT NOTE**: This requires that you have sqlite installed on your machine and available to use in your shell (e.g. setting the proper environmental variables). [Click here for a more detailed guide for installing sqlite3 onto your machine](https://www.linkedin.com/pulse/part-5-how-install-sqlite-your-machine-windows-linux-mac-julles).