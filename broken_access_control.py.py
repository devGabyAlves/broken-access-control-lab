from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

resources = {
    1: {"owner": "admin", "data": "Dados secretos do admin"},
    2: {"owner": "user", "data": "Dados do usuário comum"}
}

def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]
    return None

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = authenticate(username, password)
    if user:
        return redirect(url_for('dashboard', username=username))
    else:
        return "Login failed", 401

@app.route('/dashboard/<username>')
def dashboard(username):
    user = users.get(username)
    if not user:
        return redirect(url_for('home'))
    return render_template('dashboard.html', user=user, resources=resources)

@app.route('/resource/<int:resource_id>')
def resource(resource_id):
    resource = resources.get(resource_id)
    if not resource:
        return "Resource not found", 404

    if resource["owner"] != "admin" and resource["owner"] != "user":
        return "Access denied", 403

    return render_template('resource.html', resource=resource)

if __name__ == '__main__':
    app.run(debug=True)
