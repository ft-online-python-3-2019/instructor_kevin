from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "CRUUUUUUUUUUSUPERSECRETKEY"

# Routes:
# GET “/” => Home page, shows all pets and a form to add a new pet
@app.route('/')
def index():
    db = connectToMySQL('cru_pets_validations')
    query = "SELECT * FROM pets;"
    # No data dictionary necessary
    pets = db.query_db(query)
    print("*"*50)
    print(pets)
    # pets is a: list of dictionaries
    return render_template('all_pets.html', most_pets = pets)
    # db.query_db("")

# POST “/add_pet” => Add information into the database, redirect back to “/”
@app.route('/add_pet', methods=["POST"])
def add_pet():
    # 1. Validation
    is_valid = True
    if len(request.form['pet_name']) < 3:
        is_valid = False
        flash("Get the hell out of here, make your name longer than 3 characters")
    if len(request.form['type']) < 3:
        is_valid = False
        flash("Get on outta here boi, make your type longer than 3 characters")
    if is_valid == True:
        # Run the query
        db = connectToMySQL('cru_pets_validations')
        query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW())"
        data = {
            'name': request.form['pet_name'],
            'type': request.form['type'],
        }
        new_pet_id  = db.query_db(query, data)
        return redirect('/')
    else:
        return redirect('/')
# GET “/pets/<id>/edit” => Gets the information using <id> and renders a form with that information
@app.route('/pets/<id>/edit')
def edit_pet(id):
    db = connectToMySQL('cru_pets_validations')
    query = "SELECT * FROM pets WHERE pet_id=%(id)s;"
    data = {'id': id}
    pets = db.query_db(query,data)
    print("EDIT EDIT EDIT")
    print('*'*50)
    pet = pets[0]
    return render_template('edit.html', edit_pet = pet)

# POST “/pets/<id>/update” => Runs an update query using the form information and the <id> in the url, redirect back to “/“
@app.route('/pets/<id>/update', methods=["POST"])
def update(id):
    # 1. Validate
    is_valid = True
    if len(request.form['pet_name']) < 3:
        is_valid = False
        flash("Get the hell out of here, make your name longer than 3 characters")
    if len(request.form['type']) < 3:
        is_valid = False
        flash("Get on outta here boi, make your type longer than 3 characters")
    if is_valid == True:
        # run the update query
        db = connectToMySQL('cru_pets_validations')
        query = "UPDATE pets SET name=%(name)s, type=%(type)s, updated_at = NOW() WHERE pet_id= %(id)s"
        data = {
            'name': request.form['pet_name'],
            'type': request.form['type'],
            'id': id,
        }
        result = db.query_db(query,data)
        print(result)
        return redirect('/')
    else:
        return redirect(f"/pets/{id}/edit")
if __name__ == "__main__":
    app.run(debug=True)
