from flask import Flask, abort, redirect, render_template, request
from pokedex import pokedex
import json

app = Flask(__name__)
pokedex = pokedex.Pokedex(version='v1', user_agent='ExampleApp (https://example.com, v2.0.1)')

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        querry = request.form.get("pokemon")
        pokemon = pokedex.get_pokemon_by_name(querry)
        return redirect("pokemon.htm",pokemon=pokemon)
    return render_template('index.html')
