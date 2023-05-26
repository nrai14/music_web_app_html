from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
import os
from flask import Flask, request, render_template
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#Example:

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

#Exercise:

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     return "\n".join(
#         f"{album}" for album in repository.all()
#     )

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     return render_template('albums.html', album='Hypnotised')

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)

@app.route('/home', methods=['GET'])
def go_home():
    return render_template('home.html', home='Click me to go to albums list!')
# anything albums / something is going to be handled by the method underneath this line
@app.route('/albums/<id>')
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.getbyID(id)
    return render_template("albums.html", albums=album)
    # Return html with album details

# Route for single album details
@app.route('/albums/<id>/released')
def get_single(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.getbyID(id)
    return render_template("single_album.html", albums=album)


@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None, 
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '',200

#Challenge:

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repository.all()
    )
    
@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre'])
    repository.create(artist)
    return '',200






# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

