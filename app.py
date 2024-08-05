from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
      "id":1,
      "nome": "A Viagem de Chihiro",
      "imagem": "https://br.web.img3.acsta.net/pictures/210/527/21052756_20131024195513383.jpg"
    },
    {
      "id": 2,
      "nome": "Ponyo",
      "imagem": "https://m.media-amazon.com/images/I/61ry7KsRfIS._AC_SL1000_.jpg"
    },  
    {
      "id": 3,
      "nome": "Meu Amigo Totoro",
      "imagem": "https://i0.wp.com/studioghibli.com.br/wp-content/uploads/2020/04/meu-amigo-totoro-dvd-vers%C3%A1til.jpg"
    },  
    {
      "id": 4,
      "nome": "Princesa Mononoke",
      "imagem": "https://i0.wp.com/studioghibli.com.br/wp-content/uploads/2020/04/Princesa-Mononoke-DVD-capa-vers%C3%A1til.jpg"
    },  
    {
      "id": 5,
      "nome": "Castelo Animado",
      "imagem": "https://capas.nyc3.cdn.digitaloceanspaces.com/650-5000245618508.jpg"
    },  
    {
      "id": 6,
      "nome": "As Memórias de Marnie",
      "imagem": "https://www.itaucinemas.com.br/_img/_filmes/1859_capa.jpg"
    }
]

@app.route("/movies", methods= ["GET"])
def get_movie():
    return jsonify(movies)

@app.route("/movies/<int:id>", methods=["GET"])
def get_movie_by_id(id: int):
    for movie in movies:
        if movie.get("id") == id:    
            return jsonify(movie)
        
    return jsonify({"error": "Movie not found"}), 404

@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie_by_id(id: int):
    changed_movie = request.get_json()

    for index, movie in enumerate(movies):
        if movie.get("id") == id:
            movies[index].update(changed_movie)
            return jsonify(movies[index])
    
    return jsonify({"error": "Movie not found"}), 404
        
@app.route("/movies", methods=["POST"])        
def add_movie():
    new_movie = request.get_json()

    movies.append(new_movie)

    return jsonify(movies), 201

@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id: int):
    for index, movie in enumerate(movies):
        if movie.get("id") == id:
            del movies[index]
            return jsonify({"message": "Movie deleted successfully"}), 200
        
    return jsonify({"error": "Movie not found"}), 404

app.run(port=5000, host="localhost", debug=True)