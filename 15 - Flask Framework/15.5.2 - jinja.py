### Building URL Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja 2 Template Engine
## There are multiple ways to read a data source from the backend in the HTML page
## 1. {{}} - expressions to print output in html
## 2. {%...%} - conditions, for loop
## 3. {#...#} - this is for comments

from flask import Flask, render_template, request, redirect, url_for

app = Flask('__name__')

@app.route('/')
def welcome():
    return '<html><body><h1>Welcome to the Flask lesson</h1></body></html>'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=["GET", 'POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Welcome {name}'
    return render_template('form2.html')

## Variable Rule
## When we are assigning a specific datatype to a variable and restricting the values it can store  
@app.route('/success/<int:score>') #Providing a parameter score
def success(score): #We can acess that parameter inside this function
    res=""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    
    return render_template('result.html',results=res) #Passing the res variable as a parameter by the name results to the html file

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score':score, 'res':res}
    return render_template('result2.html', results=exp)


## if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result3.html',results=score )


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result3.html', results=score)
    

@app.route('/submit2',methods=['GET','POST'])
def submit2():
    total_score = 0
    score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        datascience = float(request.form['datascience'])
        chemistry = float(request.form['chemistry'])

        total_score = chemistry + science + maths + datascience
        score = total_score / 4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=score)) #url_for() is responsible for building dynamic urls



if __name__ == '__main__':
    app.run(debug=True)