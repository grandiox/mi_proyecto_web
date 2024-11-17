from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

BACKEND_URL = 'http://backend:5000'

@app.route('/')
def index():
    return "¡Bienvenido a la aplicación!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        response = requests.post(f'{BACKEND_URL}/api/register', json={
            'username': request.form['username'],
            'password': request.form['password'],
            'email': request.form['email']
        })
        
        if response.status_code == 201:
            return redirect(url_for('login'))
        return f"Error: {response.json()['error']}"
        
    return """
    <form method="post">
        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="submit" value="Register">
    </form>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        response = requests.post(f'{BACKEND_URL}/api/login', json={
            'username': request.form['username'],
            'password': request.form['password']
        })
        
        if response.status_code == 200:
            session['token'] = response.json()['token']
            return redirect(url_for('dashboard'))
        return "Invalid credentials"
        
    return """
    <form method="post">
        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">
    </form>
    """

@app.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect(url_for('login'))
    return "¡Bienvenido al Dashboard!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
