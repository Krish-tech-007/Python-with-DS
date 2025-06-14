from flask import Flask, render_template, request

app = Flask('__name__')

#By default all routes are get
#Get is when we just hit the url and get a response
#Post is when we provide some input and we get a response based on our input to the web server which interacts with the web app which interacts with the database
@app.route('/')
def welcome():
    return '<html><h1>Welcome</h1></html>'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=["GET","POST"])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)