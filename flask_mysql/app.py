from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('flask_mysql_intro_3_2019')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM yellow_belt_champions;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/new")
def new_champion():
    return render_template("new.html")

@app.route("/create_champion", methods=["POST"])
def create_champion():
    # 1. Connect to the db
    mysql = connectToMySQL('flask_mysql_intro_3_2019')
    # 2. Create a string for your query, and a dictionary for data (if necessary)
    query = 'INSERT INTO yellow_belt_champions (first_name, last_name, created_at, updated_at) VALUES (%(fn)s, %(ln)s, NOW(), NOW())'
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
    }
    # 3. run mysql.query_db
    result = mysql.query_db(query, data)
    print("created a new user with id:", result)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)