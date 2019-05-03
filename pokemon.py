from flask import Flask, request, redirect, render_template, url_for
import json, requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pokemon_home.html")

@app.errorhandler(404)
def error_404(Error):
    return render_template("error_pokemon.html")

@app.route('/notfound')
def notfound():
    return render_template("error_pokemon.html")

@app.route("/hasil", methods=['GET', 'POST'])
def hasil():
    name = request.form['nama']
    url = 'https://pokeapi.co/api/v2/pokemon/'+name
    pokemon = requests.get(url)
    # print(type(pokemon))
    # print(str(pokemon))
    if str(pokemon) == '<Response [404]>':
        return redirect('/NotFound')
    file_nama_pokemon = pokemon.json()['forms']
    nama = file_nama_pokemon[0]['name'].replace(file_nama_pokemon[0]['name'][0],file_nama_pokemon[0]['name'][0].upper())
    file_gambar_pokemon = pokemon.json()['sprites']
    gambar_pokemon = file_gambar_pokemon['front_default']
    id_pokemon = pokemon.json()['id']
    berat_pokemon = pokemon.json()['weight']
    tinggi_pokemon = pokemon.json()['height']
    files = [nama, gambar_pokemon, id_pokemon, berat_pokemon, tinggi_pokemon]
    return render_template("hasil_pokemon.html", x = files)

if __name__ == "__main__":
    app.run(debug=True)