from flask import Flask, render_template #render_template is used to redirect to a html page

app = Flask(__name__)

@app.route("/")
def welcome(): #Integrating HTML tags
    return "<html><title>Flask</title><body><h1>Welcome to the course</h1></body></html>" #Returning html
#Not a good practice, it is recommended to create a separate HTML page instead of returning html tags

@app.route("/index")
def index(): #redirecting to the html page
    return render_template('index.html')
    # In HTML integration
    # Jina 2 template engine works with the help of render_template which is responsible for redirecting to the html page
    # While redirecting it will look for the html file inside a folder called templates
    # If the file is not present, we will be displayed an Error Page for Template Not Found

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)