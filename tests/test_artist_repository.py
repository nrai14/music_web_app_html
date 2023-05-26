from lib.artist_repository import ArtistRepository 
from lib.artist import Artist

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/artist_table.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists == [
        Artist(1, "Pixies", "Indie"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Country"),
        Artist(4, "Nina Simone", "Jazz")
    ]

def test_create_artist(db_connection):
    db_connection.seed("seeds/artist_table.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Wild Nothing", "Indie"))

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Indie"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Country"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Wild Nothing", "Indie")
    ]

def test_find_by_artist_id(db_connection):
    db_connection.seed("seeds/artist_table.sql")
    repository = ArtistRepository(db_connection)

    result = repository.findbyartistID(1)
    assert result == [
        Artist(1, "Pixies", "Indie")
    ]
    