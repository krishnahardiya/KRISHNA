from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the HTML registration form
@app.route('/my_club\my_club\app.py')
def home():
    return render_template('reg.html')

# Route to process the form data when submitted
@app.route('/my_club\my_club\app.py', methods=['POST'])
def register():
    # Capture the data from the HTML form using the 'name' attributes
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # For demonstration, we print it to the terminal and show a message
    print(f"New User Registered: {username} | Email: {email}")
    
    # In a real app, you would add database logic here to save the user
    return f"<h3>Registration Successful! Welcome, {username}.</h3>"

if __name__ == '__main__':
    app.run(debug=True)
