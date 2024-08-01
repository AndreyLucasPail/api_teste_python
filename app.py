from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id":1,
        "titulo" : "livro1",
        "autor" : "joao",
    },
    {
        "id":2,
        "titulo" : "livro2",
        "autor" : "joao2",
    },
    {
        "id":3,
        "titulo" : "livr3",
        "autor" : "joao3",
    }
]

@app.route("/livros", methods= ["GET"])
def get_books():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["GET"])
def get_book_by_id(id: int):
    for book in livros:
        if book.get("id") == id:    
            return jsonify(book)

@app.route("/livros/<int:id>", methods=["PUT"])
def update_books_by_id(id: int):
    changed_book = request.get_json()

    for index, book in enumerate(livros):
        if book.get("id") == id:
            livros[index].update(changed_book)
            return jsonify(livros[index])
        
@app.route("/livros", methods=["POST"])        
def add_book():
    new_book = request.get_json()

    livros.append(new_book)

    return jsonify(livros)

app.route("/livros/<int:id>", methods=["DELETE"])
def delete_book(id: int):
    for index, book in livros:
        if book.get("id") == id:
            del livros[index]
    return jsonify(livros)

app.run(port=5000, host="localhost", debug=True)