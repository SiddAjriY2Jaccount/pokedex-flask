# pokedex-flask
This repository contains all the files and instructions to get your very own PokeDex up and running using Flask

Pre-requisites: python3.6+, pip, venv (recommended)

Demo can be found [here](http://pokedex-flask.herokuapp.com/)

![image info](./img/preview.png)

## Installation

- Clone this repository: `git clone https://www.github.com/SiddAjriY2Jaccount/pokedex-flask`
- Install all the required dependencies: `pip install -r requirements.txt`
- Run the flask app from root of the directory: `flask run`
- Go to `localhost:5000` on your browser to see your PokeDex up and running!

## Querying PokeAPI

- Refer the script `caching-pokeapi-data.py` 
- It is used to cache data by querying the PokeAPI, thereby reducing load time by eliminating the need to query the API for each Pokemon each time the web app reloads
- The web app only displays the details of the Pokemon whose details have been cached
- To change the number of Pokemon to be displayed, simply change the `max_pokemon` value to your desired number 
- Finally run: `python3 caching-pokeapi-data.py`
