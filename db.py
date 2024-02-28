from flask import Flask, render_template, g, request, flash, redirect, url_for
import sqlite3


app = Flask(__name__)
app.secret_key = b'secret tunnel through the mountain'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    users = cursor.execute("SELECT * from Users").fetchall()
    print(users)
    return render_template('index.html', users=users)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['username']
        uid = request.form['uid']
        points = request.form['points']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        all_ids = cursor.execute('SELECT Id FROM Users').fetchall()
        print(all_ids)

        # define in a more global scope as no error. may change with the following conditionals.
        error = None

        if not name:
            error = "Username is required"
        elif not uid:
            error = "ID is required"
        elif not points:
            error = "Point value is required"
        elif (int(uid),) in all_ids:
            error = "ID is already taken"
        
        if not error:
            cursor.execute('INSERT INTO Users VALUES (?, ?, ?)', (name, uid, points))
            connection.commit()
            return redirect(url_for('index'))
        flash(error)
    return render_template('create.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    target = None
    if request.method == 'POST':
        uid = request.form['uid']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        all_ids = cursor.execute('SELECT Id FROM Users').fetchall()
        print(all_ids)

        # define in a more global scope as no error. may change with the following conditionals.
        error = None

        if (int(uid),) not in all_ids:
            error = f"User with ID {uid} does not exist"
        
        if not error:
            target = cursor.execute('SELECT * FROM Users WHERE Id = ?', (uid,)).fetchall()[0]
            print(target)
        else:
            flash(error)
    return render_template('search.html', target=target)
        

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        uid = request.form['uid']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        all_ids = cursor.execute('SELECT Id FROM Users').fetchall()
        print(all_ids)

        # define in a more global scope as no error. may change with the following conditionals.
        error = None

        if (int(uid),) not in all_ids:
            error = f"User with ID {uid} does not exist"
        
        if not error:
            cursor.execute('DELETE FROM Users WHERE Id = ?', (uid,))
            connection.commit()
            return redirect(url_for('index'))
        flash(error)
    return render_template('delete.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        uid = request.form['uid']
        name = request.form['username']
        points = request.form['points']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        all_ids = cursor.execute('SELECT Id FROM Users').fetchall()
        print(all_ids)

        # define in a more global scope as no error. may change with the following conditionals.
        error = None

        if (int(uid),) not in all_ids:
            error = f"User with ID {uid} does not exist"
        
        if not error:
            if not name:
                # User did not specify a new name. Keep the user's existing name.
                name = cursor.execute('SELECT Username FROM Users WHERE Id = ?', (uid,)).fetchall()[0][0]
        
            if not points:
                # User did not specify new point value. Keep their existing point value.
                points = cursor.execute('SELECT Points FROM Users WHERE Id = ?', (uid,)).fetchall()[0][0]
            print(f"Username: {name}\nID: {uid}\nPoints: {points}")
            cursor.execute('UPDATE Users SET Username = ?, Points = ? WHERE Id = ?', (name, points, uid))
            connection.commit()
            return redirect(url_for('index'))
        flash(error)
    return render_template('update.html')


if __name__ == "__main__":
    app.run(debug=True)