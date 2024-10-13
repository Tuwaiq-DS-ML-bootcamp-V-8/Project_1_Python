from flask import Flask, redirect, render_template, request  # Import necessary Flask modules
from Task import Task  # Import the Task class from the Task module

<<<<<<< HEAD
app = Flask(__name__)  # Create a new Flask application instance
task = Task()  # Create a new Task object to manage tasks
=======
app = Flask(__name__)
task = Task()
completed_count = 0
>>>>>>> 7b9b4556b1c088c023cf1a6881fdc508e135d3c8

@app.route("/")  # Define the route for the home page
def home():
<<<<<<< HEAD
    # Render the home template and pass the list of tasks to it
    return render_template("home.html", li=task.display_tasks())
=======
    completed_count = len(list(filter(lambda x: x["is_complated"] == 1, task.li)))
    return render_template("home.html", li = task.display_tasks(), count=completed_count)
>>>>>>> 7b9b4556b1c088c023cf1a6881fdc508e135d3c8

@app.route('/edit/<int:task_id>')  # Define the route to edit a task with a specific ID
def get_edit(task_id):
    ind = task.is_valid(task_id)  # Check if the task ID is valid
    if ind:  # If the task ID is valid
        result = task.display_task(ind - 1)  # Get the task details
        # Render the edit template and pass the task details to it
        return render_template("edit.html", result=result)
    # Redirect to the home page if the task ID is not valid
    return redirect("/", code=303)

@app.route('/add', methods=['POST'])  # Define the route to add a new task
def add():
    data = request.json  # Get the JSON data from the request
    try:  # Attempt to execute the following block of code
        priority = int(data.get('priority'))  # Get the task priority and convert it to an integer
        task.add_task(task=data.get('task'), priority=priority)  # Add the new task
    except:  # Catch any exceptions that occur in the try block
        return "Wrong information", 404  # Return an error message if there was a problem
    return "Succeed", 200  # Return a success message if the task was added

@app.route('/delete', methods=['POST'])  # Define the route to delete a task
def delete():
    data = request.json  # Get the JSON data from the request
    ind = task.is_valid(data.get('id'))  # Check if the task ID is valid
    if ind:  # If the task ID is valid
        task.delete_task(ind - 1)  # Delete the task
        return "Succeed", 200  # Return a success message
    return "Not Found", 404  # Return an error message if the task ID was not found

@app.route('/edit', methods=['POST'])  # Define the route to edit a task
def edit():
    data = request.json  # Get the JSON data from the request
    ind = task.is_valid(data.get('id'))  # Check if the task ID is valid
    if ind:  # If the task ID is valid
        try:  # Attempt to execute the following block of code
            priority = int(data.get('priority'))  # Get the task priority and convert it to an integer
            result = task.edit_task(ind - 1, data.get('task'), priority, data.get('is_completed'))  # Edit the task
            if result:  # If the task was edited successfully
                return "Succeed", 200  # Return a success message
        except:  # Catch any exceptions that occur in the try block
            return "Wrong information", 404  # Return an error message if there was a problem
    return "Not Found", 404  # Return an error message if the task ID was not found

if __name__=="__main__":  # Check if the script is being run directly
    app.run(debug=True)  # Run the Flask application in debug mode
