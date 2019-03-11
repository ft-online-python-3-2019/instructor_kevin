from flask import Flask, render_template, session, redirect
# 1. What do I need to import in order to make this project work?
app =  Flask(__name__)

app.secret_key = "ThisIsSuperSecret"
# 2. What information do I need to save in session. In this case it was the number of times a user accessed the site. We should save this info in a intuitively named key ('count')
@app.route('/')
def index():
    if 'count' in session:
        # What do I do if the key is in session (aka this is not the user's first time on this site?)
        print('*'*50)
        print('key exists!')
        session['count'] = session['count'] + 1
    else:
        # What do I do if the key is NOT in session (aka this is the user's first time on this site?)
        print('*'*50)
        print("key 'count' does NOT exist")
        session['count'] = 1
    return render_template('counter.html', count = session['count'])

# 3. Understand that if I redirect to a route, I am invoking the function related to that route AGAIN.
# EX: redirecting to '/' will invoke its related function 'index' again!
@app.route('/destroy_session')
def destroy_session():
    print('*'*50)
    print('hit the route /destroy_session')
    session.clear()
    return redirect('/')

@app.route('/add_two', methods=["POST"])
def add_two():
    print('*'*50)
    print('hit the route /add_two')
    session['count'] += 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)