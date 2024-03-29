function searchTasks() {
    var projectGid = document.getElementById("projectGidInput").value;
    var tagGid = document.getElementById("tagGidInput").value;
    var requestData = {};
    if (projectGid) {
        requestData.project_gid = projectGid;
    }
    if (tagGid) {
        requestData.tag_gid = tagGid;
    }
    $.ajax({
        url: "http://localhost:5000/search",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify(requestData),
        success: function(response) {
            displayTasks(response.tasks);
        },
        error: function(xhr, status, error) {
            alert("An error occurred: " + error);
        }
    });
}

function displayTasks(tasks) {
    var taskList = document.getElementById("taskList");
    taskList.innerHTML = "<h2>Tasks:</h2>";
    if (tasks.length === 0) {
        taskList.innerHTML += "<p>No tasks found.</p>";
    } else {
        tasks.forEach(function(task) {
            var taskLink = "<a href='" + task.url + "' target='_blank'>" + task.name + "</a>";
            taskList.innerHTML += "<p>" + taskLink + "</p>";
        });
    }
}

function getAllTags() {
    $.ajax({
        url: "http://localhost:5000/tags",
        method: "GET",
        success: function(response) {
            displayTags(response.tags);
        },
        error: function(xhr, status, error) {
            alert("An error occurred: " + error);
        }
    });
}

function displayTags(tags) {
    var tagList = document.getElementById("tagList");
    tagList.innerHTML = "<h2>Tags:</h2>";
    if (tags.length === 0) {
        tagList.innerHTML += "<p>No tags found.</p>";
    } else {
        tags.forEach(function(tag) {
            tagList.innerHTML += "<p>" + tag.name + " (GID: " + tag.gid + ")</p>";
        });
    }
}

// Function to send API request to the backend and retrieve tasks
function searchTags(button) {
    var tagGid = button.dataset.tagGid; // Retrieve tag_gid from data-tag-gid attribute of the button
    var requestData = {};
    if (tagGid) {
        requestData.tag_gid = tagGid;
    }
    $.ajax({
        url: "http://localhost:5000/search",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify(requestData),
        success: function(response) {
            displayModal(response.tasks);
        },
        error: function(xhr, status, error) {
            alert("An error occurred: " + error);
        }
    });
}

// Function to display tasks in a modal
function displayModal(tasks) {
    var modal = document.getElementById("myModal");
    var modalContent = document.getElementById("modal-content");
    modal.style.display = "block";
    modalContent.innerHTML = "<h2>Tasks:</h2>";
    if (tasks.length === 0) {
        modalContent.innerHTML += "<p>No tasks found.</p>";
    } else {
        tasks.forEach(function(task) {
            var taskLink = "<a href='" + task.url + "' target='_blank'>" + task.name + "</a>";
            modalContent.innerHTML += "<p>" + taskLink + "</p>";
        });
    }
}

// Close the modal when the user clicks on the close button
var closeModal = document.getElementsByClassName("close")[0];
closeModal.onclick = function() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// Close the modal when the user clicks outside of it
window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}