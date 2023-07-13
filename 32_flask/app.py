from logging.config import dictConfig
import random
from turtledemo.chaos import g

from flask import Flask, request, redirect, abort, render_template, session

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


# check if the session contains a username before each request
@app.before_request
def check_session():
    g.username = session.get('username')
    if not g.username and request.path != '/login':
        return redirect('/login')


# task 6 Create a GET request handler /
@app.route('/')
def home():
    greeting = f'Hello, {g.username}' if g.username else ''
    html_code = f'''
        <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Welcome to the Home Page</h1>
            <p>{greeting}</p>
            <ul>
                <li><a href="/login">Login</a></li>
                <li><a href="/users">Users</a></li>
                <li><a href="/books">Books</a></li>
                <li><a href="/params">Params</a></li>
            </ul>
        </body>
        </html>
    '''
    return html_code


# Create the /logout endpoint
@app.route('/logout')
def logout():
    # Clear the username from the session
    session.pop('username', None)
    return redirect('/login')


# functions for processing requests task 1 and 7
@app.route('/users')
def get_users():
    global random_names
    names = ['Andrii', 'Natalia', 'Serhiy', 'Vova', 'Mark']
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
            if count <= 0:
                abort(400, 'Invalid count value')
            random_names = random.sample(names, min(count, len(names)))
        except ValueError:
            abort(400, 'Invalid count value')
    else:
        random_names = random.sample(names, random.randint(1, len(names)))
    return render_template('endpoints/users.html', names=random_names)


@app.get('/books')
def get_books():
    global random_books
    books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
            if count <= 0:
                abort(400, 'Invalid count value')
            random_books = random.sample(books, min(count, len(books)))
        except ValueError:
            abort(400, 'Invalid count value')
    else:
        random_books = random.sample(books, random.randint(1, len(books)))

    html_list = '<ul>'
    for book in random_books:
        html_list += f'<li>{book}</li>'
    html_list += '</ul>'

    return render_template('endpoints/books.html', books=random_books)


@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    if user_id % 2 == 0:
        return render_template('endpoints/user.html', user_id=user_id)
    else:
        return '404 Not Found', 404


@app.get('/books/<string:title>')
def get_book_by_title(title):
    transformed_title = title.capitalize()
    return render_template('endpoints/book.html', title=transformed_title)


# Create a function to handle GET /params requests
@app.get('/params')
def get_params():
    params = request.args
    table = '<table>'
    table += '<tr><th>parameter</th><th>value</th></tr>'
    for key, value in params.items():
        table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    table += '</table>'
    return render_template('endpoints/params.html', params=params)


# Create a function for processing GET, POST /login requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        '''
            <form method="POST" action="/login">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br>
                <input type="submit" value="Submit">
            </form>
        '''
        return render_template('endpoints/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            # Store the username in the session
            session['username'] = username
            return redirect('/users')
        else:
            abort(400, 'Missing username or password')


# Add username and password validation to the POST /login handler function:
def validate_username(username):
    if len(username) >= 5:
        return True
    return False


def validate_password(password):
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return True
    return False


# Create custom 404 and 500 error handlers that should return custom html code for display.
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
