from flask import Flask, abort, redirect, render_template, request
from pokedex import pokedex
import pokebase as pb
import json

app = Flask(__name__)
pokedex = pokedex.Pokedex(version='v1', user_agent='ExampleApp (https://example.com, v2.0.1)')

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("error.html", top=code, bottom=escape(message)), code



@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        querry = request.form.get("pokemon")
        if len(querry) == 0:
            return apology("Enter name")
        pokemon = pokedex.get_pokemon_by_name(querry)
        print(pokemon)
        if pokemon['error']:
            return apology("No Pokemon found")
        return render_template("pokemon.html",pokemon=pokemon)
    return render_template('index.html')

