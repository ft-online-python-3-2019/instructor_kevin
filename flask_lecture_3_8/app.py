from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def get_form():
    return render_template('get_form.html') # step 1 happens here

@app.route('/result', methods=["POST"])
def process_form():
    print(request.form['email'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)