from flask import Flask, render_template, request
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


@app.route('/read-form', methods=['POST'])
def read_form():
    # Get the form data as Python ImmutableDict datatype
    data = request.form
    ## Return the extracted information
    return {
        'emailId': data['userEmail'],
        'phoneNumber': data['userContact'],
        'password': data['userPassword'],
        'gender': 'Male' if data['genderMale'] else 'Female',
    }

if __name__=="__main__":
    app.run(debug=True)



