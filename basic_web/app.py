from flask import Flask, render_template, request
from db import DatabaseManager
app = Flask(__name__)
name='name'

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/allinfo")
def allinfo():
    return render_template('allinfo.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/show")
def show():
    users = DatabaseManager('users.db')
    ltstuser=users.fetchall("""SELECT * FROM users""")
    print(ltstuser)
    return render_template('show.html', ltstuser=ltstuser)


@app.route('/read-form', methods=['POST'])
def read_form():
    # Get the form data as Python ImmutableDict datatype
    users = DatabaseManager('users.db')
    users.create_tables()
    data = request.form
    userEmail=data['userEmail']
    userNmae = data['name']
    userLastname = data['lastname']
    dictsend=(userEmail, userNmae, userLastname)
    print(*dictsend)
    users.query('INSERT INTO Users VALUES (?, ?, ?)', dictsend)
    # users.query('INSERT INTO Users VALUES (?, ?, ?)', (data['userEmail'], data['userPassword'],data['userContact']))

    ## Return the extracted information
    return render_template('formsub.html')


if __name__=="__main__":
    app.run(debug=True)



