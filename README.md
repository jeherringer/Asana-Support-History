# Asana Task Search Application

## Overview
The Asana Task Search Application is a web-based tool that allows users to search for tasks within their Asana workspace. It provides functionality to search tasks by project or tag, and displays the results in a user-friendly manner.

## Features
- **Search by Project**: Users can search for tasks by specifying a project GID.
- **Search by Tag**: Users can search for tasks by specifying a tag GID.
- **Display Tasks**: The application displays the retrieved tasks, including their names and URLs.
- **Get All Tags**: Users can fetch all tags from the Asana workspace to obtain their GIDs.
- **Responsive Design**: The application is designed to work well on various devices, including desktops, tablets, and mobile phones.

## Technologies Used
- **Flask**: Flask is used as the web framework to handle HTTP requests and responses.
- **Flask-CORS**: Flask-CORS is used to enable Cross-Origin Resource Sharing, allowing the frontend to communicate with the backend.
- **Asana Python Client**: The Asana Python Client library is used to interact with the Asana API.
- **Requests**: The Requests library is used to send HTTP requests to the Asana API.
- **jQuery**: jQuery is used for AJAX requests and DOM manipulation on the frontend.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Create a `.env` file in the project directory and add your Asana Personal Access Token as `personal_access_token`.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## Usage
1. Enter the Project GID or Tag GID in the respective input fields.
2. Click the "Search" button to retrieve tasks based on the provided GID.
3. Click the "Get All Tags" button to fetch all tags from the Asana workspace.
4. The retrieved tasks or tags will be displayed below the input fields.

## Contributors
- Jon Herringer | j.e.herringer@gmail.com
