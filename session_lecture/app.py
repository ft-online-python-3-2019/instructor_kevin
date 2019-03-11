from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "AlecAnsweredTheQuestion"

@app.route('/')
def index():
    if 'team_list' not in session:
        session['team_list'] = []
    session['my_name'] = "Kevin"
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html', the_name=session['my_name'], team_list = session['team_list'])

@app.route('/process_form', methods=["POST"])
def process_form():
    my_list = session['team_list']
    my_list.append(request.form['team_name'])
    session['team_list'] = my_list
    print('*'*50)
    print(session['team_list'])
    return redirect('/home')

if __name__=="__main__":
    app.run(debug=True)