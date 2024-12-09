from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Mock user data for validation
users = {
    "test@example.com": "password123"  # email:password
}

@app.route('/')
def home():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate the user
        if email in users and users[email] == password:
            return jsonify({"message": "Sign-in successful!"}), 200
        else:
            return jsonify({"error": "Invalid email or password."}), 401

    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
