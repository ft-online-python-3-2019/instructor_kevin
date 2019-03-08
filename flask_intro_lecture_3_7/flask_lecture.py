from flask import Flask, render_template # 1. Import flask

app = Flask(__name__) # 2. Instantiate an instance of Flask using __name__

# 3. Define all of your routes
@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/home')
def home():
    all_friends = [
        {'name': 'Alec'},
        {'name': 'Double O'},
    ]
    return render_template('index.html', name="Sam", friends = all_friends)

# 4. Start the flask server
if __name__=="__main__":
    app.run(debug=True)