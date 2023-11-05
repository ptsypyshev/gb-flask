from flask import Flask, redirect, render_template, request, url_for, make_response

app = Flask(__name__)

@app.route('/')
def html_index():
    context = {
        'title': 'Main page',
    }
    return render_template('index.html', **context)

@app.route('/sign-in/', methods=['GET', 'POST'])
def sign_in():    
    context = {
        'title': 'Sign-in page',
    }
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if not (name and email):
            context['bad_req'] = "You should send username and email"
            return render_template('sign-in.html', **context), 400
        
        response = make_response(redirect(url_for('profile')))
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        return response
    return render_template('sign-in.html', **context)

@app.route('/sign-out/')
def sign_out():
    response = make_response(redirect(url_for('sign_in')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response

@app.route('/profile/')
def profile():

    context = {
        'title': 'Profile page',
        'name': request.cookies.get('username')
    }
    return render_template('profile.html', **context)

if __name__ == '__main__':
    app.run()