from flask import Flask, request, jsonify  # Import Flask framework modules for web development
from flask_cors import CORS  # Import CORS module for Cross-Origin Resource Sharing
from flask_cors import cross_origin  # Import cross_origin decorator for CORS
import asana  # Import Asana library for interacting with Asana API
from asana.rest import ApiException  # Import ApiException from Asana library for handling exceptions
import requests  # Import requests library for sending HTTP requests
import os  # Import os module for interacting with the operating system
from dotenv.main import load_dotenv  # Import load_dotenv function to load environment variables from .env file

app = Flask(__name__)  # Create a Flask application instance
CORS(app)  # Enable CORS for all routes in the Flask app

load_dotenv()  # Load environment variables from .env file
personal_access_token = os.getenv("personal_access_token")  # Retrieve personal access token from environment variables

# URL for Asana API
asana_url = "https://app.asana.com/api/1.0/"

def get_tasks(project_gid=None, tag_gid=None):
    """
    Function to fetch tasks from the Asana API based on project or tag GID.

    Args:
        project_gid (str): GID of the project to fetch tasks from.
        tag_gid (str): GID of the tag to fetch tasks associated with.

    Returns:
        list: List of tasks retrieved from the Asana API.
    """
    headers = {
        "Authorization": f"Bearer {personal_access_token}"
    }
    params = {
        "opt_fields": "name,permalink_url",
        "completed_since": "2020-01-01T21:23:24.000Z"
    }
    if project_gid:
        url = asana_url + f"projects/{project_gid}/tasks"
    elif tag_gid:
        url = asana_url + f"tags/{tag_gid}/tasks"
    else:
        return []

    try:
        response = requests.get(url, headers=headers, params=params)  # Send GET request to Asana API
        response.raise_for_status()  # Raise exception for HTTP errors (e.g., 404, 500)
        tasks = response.json().get("data", [])  # Extract tasks from JSON response
        tasks_data = [{"name": task["name"], "url": task["permalink_url"]} for task in tasks]  # Process tasks data
        return tasks_data
    except requests.exceptions.RequestException as e:
        print("Error fetching tasks:", e)  # Log error fetching tasks
        return []
    except Exception as e:
        print("Error processing tasks:", e)  # Log error processing tasks
        return []

def get_all_tags():
    """
    Function to fetch all tags from the Asana workspace.

    Returns:
        list: List of tags retrieved from the Asana API.
    """
    headers = {
        "Authorization": f"Bearer {personal_access_token}"
    }
    params = {
        "opt_fields": "name,gid"
    }
    url = asana_url + "tags"

    try:
        response = requests.get(url, headers=headers, params=params)  # Send GET request to Asana API
        response.raise_for_status()  # Raise exception for HTTP errors (e.g., 404, 500)
        tags = response.json().get("data", [])  # Extract tags from JSON response
        return tags
    except requests.exceptions.RequestException as e:
        print("Error fetching tags:", e)  # Log error fetching tags
        return []
    except Exception as e:
        print("Error processing tags:", e)  # Log error processing tags
        return []

@app.route('/')
def index():
    """
    Route to serve the index.html file.
    """
    return app.send_static_file('index.html')

@app.route('/search', methods=['POST'])
@cross_origin()
def search():
    """
    Route to handle POST requests for searching tasks.
    """
    project_gid = request.json.get('project_gid')
    tag_gid = request.json.get('tag_gid')
    tasks = get_tasks(project_gid=project_gid, tag_gid=tag_gid)  # Fetch tasks based on project or tag GID
    return jsonify({'tasks': tasks})  # Return JSON response containing tasks data

@app.route('/tags', methods=['GET'])
def get_tags():
    """
    Route to handle GET requests for fetching all tags.
    """
    tags = get_all_tags()  # Fetch all tags from Asana workspace
    return jsonify({'tags': tags})  # Return JSON response containing tags data

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode if executed directly
