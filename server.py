from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key="secret key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    # Map form inputs to session values
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['language'] = request.form['language']

    if 'stack' not in request.form:
        session['stack'] = 'None selected'
    else:
        if len(request.form.getlist('stack')) == 2: # both selected
            session['stack'] = 'Full Stack'
        else:
            session['stack'] = request.form.getlist('stack')[0] # just one selected

    if 'wage' not in request.form: # in case nothing is selected
        session['wage'] = 'None selected'
    else:
        session['wage'] = request.form['wage']

    session['comments'] = request.form['comments']

    # After processing, we want to use the values we save in the session 
    # dictonary and redirect to the results route
    return redirect('/result')

@app.route('/result')
def result():
    # plug in session values into the results template with render_template 
    # render_template lets inject the session values into results.html
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)