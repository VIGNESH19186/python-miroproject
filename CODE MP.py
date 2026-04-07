
from flask import Flask, render_template_string, request

app = Flask(__name__)

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

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Movie Booking</title>
    <style>
        body {
            background: linear-gradient(135deg, #ffdde1, #ee9ca7);
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }

        h1 {
            text-align: center;
            color: #b30059;
        }

        .card {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin: 15px auto;
            width: 60%;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        button {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #cc0033;
        }

        input {
            padding: 5px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>🎬 Movie Booking System</h1>

    <h2>Available Movies</h2>

    {% for movie in movies %}
        <div>
            <h3>{{ movie.name }}</h3>
            <p>Cineplex: {{ movie.cinema }}</p>
            <p>Price: ₹{{ movie.price }}</p>

            <form method="post" action="/book">
                <input type="hidden" name="movie_id" value="{{ movie.id }}">
                Tickets: <input type="number" name="tickets" required>
                <button type="submit">Book</button>
            </form>
        </div>
        <hr>
    {% endfor %}

    {% if booking %}
    <h2>Booking Summary</h2>
        <p>Movie: {{ booking[0] }}</p>
        <p>Cineplex: {{ booking[1] }}</p>
        <p>Tickets: {{ booking[2] }}</p>
        <p>Total: ₹{{ booking[3] }}</p>
    {% endif %}

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html, movies=movies, booking=None)

@app.route('/book', methods=['POST'])
def book():
    movie_id = int(request.form['movie_id'])
    tickets = int(request.form['tickets'])

    movie = get_movie(movie_id)

        movie_name = movie["name"]

        booking = (
        movie_name,
        movie["cinema"],
        tickets,
        tickets * movie["price"]
    )

        prices = []
    for m in movies:
        prices.append(m["price"])   

    total_movies = len(movies)       
    highest_price = max(prices)      
    lowest_price = min(prices)       

    print("Total Movies:", total_movies)
    print("Highest Price:", highest_price)
    print("Lowest Price:", lowest_price)

    return render_template_string(html, movies=movies, booking=booking)

if __name__ == '__main__':
    app.run(debug=True)
