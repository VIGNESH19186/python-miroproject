from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# Store users (temporary)
users = {}

movies = [
    {"id": 1, "name": "Avengers", "cinema": "PVR Cineplex", "price": 200},
    {"id": 2, "name": "Inception", "cinema": "INOX", "price": 180},
    {"id": 3, "name": "Interstellar", "cinema": "Cinepolis", "price": 220},
]

def get_movie(movie_id):
    for m in movies:
        if m["id"] == movie_id:
            return m
    return None

# 🌹 COMMON STYLE (ROSE THEME)
style = """
<style>
body {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    font-family: Arial;
    text-align: center;
}

.container {
    background: white;
    padding: 20px;
    width: 40%;
    margin: auto;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

button {
    background: #ff4d6d;
    color: white;
    padding: 8px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #cc0033;
}

input {
    padding: 8px;
    margin: 5px;
    width: 80%;
}
</style>
"""

# ---------------- SIGNUP PAGE ----------------
signup_html = style + """
<div class="container">
<h2>Create Account</h2>
<form method="post">
    <input type="text" name="username" placeholder="Username" required><br>
    <input type="password" name="password" placeholder="Password" required><br>
    <button type="submit">Signup</button>
</form>

<p style="color:red;">{{ msg }}</p>

<p>Already have account? <a href="/">Login</a></p>
</div>
"""

# ---------------- LOGIN PAGE ----------------
login_html = style + """
<div class="container">
<h2>Login</h2>
<form method="post">
    <input type="text" name="username" placeholder="Username" required><br>
    <input type="password" name="password" placeholder="Password" required><br>
    <button type="submit">Login</button>
</form>

<p style="color:red;">{{ error }}</p>

<p>New user? <a href="/signup">Create Account</a></p>
</div>
"""

# ---------------- HOME PAGE ----------------
home_html = style + """
<div class="container">
<h1>🎬 Movie Booking</h1>
<a href="/logout">Logout</a>

{% for movie in movies %}
    <div>
        <h3>{{ movie.name }}</h3>
        <p>{{ movie.cinema }}</p>
        <p>₹{{ movie.price }}</p>

        <form method="post" action="/book">
            <input type="hidden" name="movie_id" value="{{ movie.id }}">
            <input type="number" name="tickets" placeholder="Tickets" required>
            <button type="submit">Book</button>
        </form>
    </div>
    <hr>
{% endfor %}

{% if booking %}
<h2>Booking Summary</h2>
<p>Movie: {{ booking[0] }}</p>
<p>Cinema: {{ booking[1] }}</p>
<p>Tickets: {{ booking[2] }}</p>
<p>Total: ₹{{ booking[3] }}</p>
{% endif %}
</div>
"""

# ---------------- ROUTES ----------------

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""

    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        if u in users and users[u] == p:
            session['user'] = u
            return redirect('/home')
        else:
            error = "Invalid Login!"

    return render_template_string(login_html, error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ""

    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        if u in users:
            msg = "User already exists!"
        else:
            users[u] = p
            msg = "Account created! Go to login."

    return render_template_string(signup_html, msg=msg)


@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/')

    return render_template_string(home_html, movies=movies, booking=None)


@app.route('/book', methods=['POST'])
def book():
    if 'user' not in session:
        return redirect('/')

    movie = get_movie(int(request.form['movie_id']))
    tickets = int(request.form['tickets'])

    booking = (
        movie["name"],
        movie["cinema"],
        tickets,
        tickets * movie["price"]
    )

    return render_template_string(home_html, movies=movies, booking=booking)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)