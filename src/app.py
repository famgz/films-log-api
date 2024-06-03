from flask import Flask, request, jsonify
from pathlib import Path
from mysql.connector import connect

source_dir = Path(__file__).resolve().parent


app = Flask(__name__)

HOST = "localhost"
USER = "root"
PASSWORD = "admin"
DATABASE = "films_log"


def get_db_connection():
    return connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
    )


def run_sql_script(script_path):
    script_path = Path(source_dir, "database", script_path)
    with open(script_path, "r") as file:
        sql_commands = file.read().split(";")

    conn = connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
    )

    cursor = conn.cursor()
    for command in sql_commands:
        if command.strip():
            cursor.execute(command)

    conn.commit()
    cursor.close()
    conn.close()


def is_database_empty():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM film")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count == 0


def init_db():
    # Criar database caso não exista
    try:
        run_sql_script("setup.sql")
        print("Database inicializado")
    except Exception as e:
        print(str(e))

    # Preencher table film caso esteja vazio
    if is_database_empty():
        try:
            run_sql_script("seed.sql")
            print("Filmes adicionados com sucesso")
        except Exception as e:
            print(str(e))


def run_query(query):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
    except Exception as e:
        return str(e)


def fetch_on_from_query(query):
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                return cursor.fetchone()

    except Exception as e:
        return {"error": str(e)}


# User CRUD
@app.route("/user", methods=["POST"])
def create_user():
    data = request.form
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    res = run_query(
        f"INSERT INTO user (username, email, password) VALUES ('{username}', '{email}', '{password}')"
    )

    if res:
        return jsonify(res), 500
    return jsonify({"message": "User criado com sucesso"}), 201


@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = fetch_on_from_query(f"SELECT * FROM user WHERE id = {id}")

    if user:
        return jsonify(user)
    return jsonify({"message": "User não encontrado"}), 404


@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.form
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    run_query(
        f"UPDATE user SET username = '{username}', email = '{email}', password = '{password}' WHERE id = {id}"
    )

    return jsonify({"message": "User atualizado com sucesso"})


@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    run_query(f"DELETE FROM user WHERE id = {id}")

    return jsonify({"message": "User excluído com sucesso"})


# Film CRUD
@app.route("/film", methods=["POST"])
def create_film():
    data = request.form
    title = data.get("title")
    year = data.get("year")
    director = data.get("director")
    duration = data.get("duration")

    run_query(
        f"INSERT INTO film (title, year, director, duration) VALUES ('{title}', '{year}', '{director}', '{duration}')"
    )

    return jsonify({"message": "Filme criado com sucesso"}), 201


@app.route("/film/all", methods=["GET"])
def get_films():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM film")
    film = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(film)


@app.route("/film/<int:id>", methods=["GET"])
def get_film(id):
    film = fetch_on_from_query(f"SELECT * FROM film WHERE id = {id}")
    if film:
        return jsonify(film)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404


@app.route("/film/<int:id>", methods=["PUT"])
def update_film(id):
    data = request.form
    title = data.get("title")
    year = data.get("year")
    director = data.get("director")
    duration = data.get("duration")

    run_query(
        f"UPDATE film SET title = '{title}', year = '{year}', director = '{director}', duration = '{duration}' WHERE id = {id}"
    )

    return jsonify({"message": "Filme atualizado com sucesso"})


@app.route("/film/<int:id>", methods=["DELETE"])
def delete_film(id):
    run_query(f"DELETE FROM film WHERE id = {id}")

    return jsonify({"message": "Filme excluído com sucesso"})


# Review CRUD
@app.route("/review", methods=["POST"])
def create_review():
    data = request.form
    user_id = data.get("user_id")
    film_id = data.get("film_id")
    review_text = data.get("review")

    run_query(
        f"INSERT INTO review (user_id, film_id, review) VALUES ('{user_id}', '{film_id}', '{review_text}')"
    )

    return jsonify({"message": "Review criado com sucesso"}), 201


@app.route("/review/<int:id>", methods=["GET"])
def get_review(id):
    review = fetch_on_from_query(f"SELECT * FROM review WHERE id = {id}")

    if review:
        return jsonify(review)
    else:
        return jsonify({"message": "Review não encontrado"}), 404


@app.route("/review/<int:id>", methods=["PUT"])
def update_review(id):
    data = request.form
    user_id = data.get("user_id")
    film_id = data.get("film_id")
    review_text = data.get("review")

    run_query(
        f"UPDATE review SET user_id = {user_id}, film_id = {film_id}, review = '{review_text}' WHERE id = {id}"
    )

    return jsonify({"message": "Review atualizado com sucesso"})


@app.route("/review/<int:id>", methods=["DELETE"])
def delete_review(id):
    run_query(f"DELETE FROM review WHERE id = {id}")

    return jsonify({"message": "Review excluído com sucesso"})


# Rating CRUD
@app.route("/rating", methods=["POST"])
def create_rating():
    data = request.form
    user_id = data.get("user_id")
    film_id = data.get("film_id")
    rating = data.get("rating")

    run_query(
        f"INSERT INTO rating (user_id, film_id, rating) VALUES ({user_id}, {film_id}, {rating})"
    )

    return jsonify({"message": "Rating criado com sucesso"}), 201


@app.route("/rating/<int:id>", methods=["GET"])
def get_rating(id):
    rating = fetch_on_from_query(f"SELECT * FROM rating WHERE id = {id}")

    if rating:
        return jsonify(rating)
    else:
        return jsonify({"message": "Rating não encontrado"}), 404


@app.route("/rating/<int:id>", methods=["PUT"])
def update_rating(id):
    data = request.form
    user_id = data.get("user_id")
    film_id = data.get("film_id")
    rating = data.get("rating")

    run_query(
        f"UPDATE rating SET user_id = {user_id}, film_id = {film_id}, rating = {rating} WHERE id = {id}"
    )

    return jsonify({"message": "Rating atualizado com sucesso"})


@app.route("/rating/<int:id>", methods=["DELETE"])
def delete_rating(id):
    run_query(f"DELETE FROM rating WHERE id = {id}")

    return jsonify({"message": "Rating excluído com sucesso"})


# Watchlist CRUD
@app.route("/watchlist", methods=["POST"])
def create_watchlist():
    data = request.form
    user_id = data.get("user_id")
    film_id = data.get("film_id")

    run_query(f"INSERT INTO watchlist (user_id, film_id) VALUES ({user_id}, {film_id})")

    return jsonify({"message": "Watchlist criado com sucesso"}), 201


@app.route("/watchlist/<int:id>", methods=["GET"])
def get_watchlist(id):
    watchlist = fetch_on_from_query(f"SELECT * FROM watchlist WHERE id = {id}")

    if watchlist:
        return jsonify(watchlist)
    else:
        return jsonify({"message": "Watchlist não encontrado"}), 404


@app.route("/watchlist/<int:id>", methods=["PUT"])
def update_watchlist(id):
    data = request.form
    user_id = data.get("user_id")
    film_id = data.get("film_id")

    run_query(
        f"UPDATE watchlist SET user_id = {user_id}, film_id = {film_id} WHERE id = {id}"
    )

    return jsonify({"message": "Watchlist atualizado com sucesso"})


@app.route("/watchlist/<int:id>", methods=["DELETE"])
def delete_watchlist(id):
    run_query(f"DELETE FROM watchlist WHERE id = {id}")
    return jsonify({"message": "Watchlist excluído com sucesso"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8081, debug=True)
