from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = "foijweogfhaegiuhseriofh3ur4239rhgfurig43y" #remember, flash needs secret key too!

@app.route("/")
def index():
    mysql = connectToMySQL('flask_mysql_intro_3_2019')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM yellow_belt_champions;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/new")
def new_champion():
    return render_template("new.html")

# Version with validations
@app.route("/create_champion", methods=["POST"])
def create_champion():
    # 1. Validate form information
    is_valid = True
    if len(request.form['first_name']) == 0:
        # If a part is invalid, set boolean to False and add an error message
        is_valid = False
        flash("First name must be present")
    if len(request.form['first_name']) < 3:
        is_valid = False
        flash("First name must be at least three characters")
    if len(request.form['last_name']) == 0:
        is_valid = False
        flash("Last name must be present")
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Last name must be at least three characters long")
    # 2. Go down branching paths based on value of is_valid (boolean)
    if is_valid == True:
        # 2a. if true, run SUCCESS LOGIC
        mysql = connectToMySQL('flask_mysql_intro_3_2019')
        query = 'INSERT INTO yellow_belt_champions (first_name, last_name, created_at, updated_at) VALUES (%(fn)s, %(ln)s, NOW(), NOW())'
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
        }
        result = mysql.query_db(query, data)
        print("created a new user with id:", result)
        return redirect('/')
    else:
        # 2b. if false, redirect back to the form and display error messages
        return redirect('/new')
        # remember to add validation errors to html!
# Version without Validations
# @app.route("/create_champion", methods=["POST"])
# def create_champion():
#     # 1. Connect to the db
#     mysql = connectToMySQL('flask_mysql_intro_3_2019')
#     # 2. Create a string for your query, and a dictionary for data (if necessary)
#     query = 'INSERT INTO yellow_belt_champions (first_name, last_name, created_at, updated_at) VALUES (%(fn)s, %(ln)s, NOW(), NOW())'
#     data = {
#         'fn': request.form['first_name'],
#         'ln': request.form['last_name'],
#     }
#     # 3. run mysql.query_db
#     result = mysql.query_db(query, data)
#     print("created a new user with id:", result)
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)