# add-favourite-food

## Installation
- Open your terminal.
- Navigate to the project directory.
- Run the following command to create a virtual environment and install the dependencies:pipenv install

## Configuration
- Create a file named .flaskenv in the project directory.
- Open the .flaskenv file and add the following configuration:
- FLASK_APP=app
- FLASK_DEBUG=1
- DATABASE_URL= (Make sure to replace the DATABASE_URL value with your actual PostgreSQL database URL)

## Database Setup
- Activate the virtual environment by running the following command: pipenv shell
- Start the Python shell by running: python3
- Inside the Python shell, import the necessary modules:
from application import db
from application.models import Menu
- To create the database tables, run the following command: db.create_all()
- Exit the Python shell by typing exit().

## Running the Server
To run the server, make sure you are in the project directory and run the following command: pipenv run dev
This command will start the Flask development server, and you should see the server running at the specified address.
Make sure to keep the terminal running while you test or use the server. If you need to stop the server, you can press Ctrl + C in the terminal.

## Features

- Add Your Favorite Food: You can add your favorite food to the system by providing its name. 
- Vote for Favorite Food: Users can vote for their preferred favorite food items. Each vote contributes to the overall popularity of the food item.
- Update Favorite Food: You have the option to update the details of your added favorite food. This allows you to make changes to the name or votes based on your preferences.
- Delete Favorite Food: If you no longer want a food item to be listed as your favorite, you can easily delete it from the system.
- Display in Bar Chart: The system provides a visually appealing representation of the favorite food items in a bar chart. The bar chart displays the popularity of each food item based on the votes it has received. This allows users to quickly identify the most popular food choices.

