from lib.album_repository import AlbumRepository
from lib.album import Album 

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_albums(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/album_table.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository

    albums = repository.all() # Get all books

    # Assert on the results
    assert albums == [
        Album(1, "Hypnotised", 1980, 1),
        Album(2, "Rumours", 1977, 2)
    ]

"""
When we call AlbumRepository#create
We get a new album in the database.
"""
def test_create_album(db_connection):
    db_connection.seed("seeds/album_table.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Divide", 2017, 3))

    result = repository.all()
    assert result == [
        Album(1, "Hypnotised", 1980, 1),
        Album(2, "Rumours", 1977, 2),
        Album(3, "Divide", 2017, 3)
    ]

def test_find_by_id(db_connection):
    db_connection.seed("seeds/album_table.sql")
    repository = AlbumRepository(db_connection)

    result = repository.getbyID(2)
    print(result)
    assert result == [
        Album(2, "Rumours", 1977, 2)
    ]
    
    