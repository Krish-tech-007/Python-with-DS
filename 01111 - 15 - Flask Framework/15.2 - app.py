### Simple Flask Web Application
from flask import Flask

## Initializing the flask app
app = Flask(__name__) ## It creates an instance of the Flask class, which will be our WSGI (Web Server Gateway Interface) application.

# Decorator
@app.route("/") # / basically means it becomes the homepage
def welcome(): #Whenever we go to this route, this function will be called
    return "Welcome to the flask lesson. Hope I learn alot."

#welcome() function becomes a parameter for the app.route() function

## We can create any number of routs
@app.route("/index")
def index():
    return "List of contents"
## Whenver we try to visit the particular url, the function associated with it will get executed.

## Running the Flask app
if __name__ == '__main__': ## Entry point of any .py file
    app.run(debug=True) #Suppose we make any changes, it won't be reflected unless the server is restarted
    # However if debug parameter is kept True, reloading the website will reflect the changes without having to restart the server.
    # Provided the changes in the source code are saved.
    # As soon as we save it, the server will get restarted automatically.
