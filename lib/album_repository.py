from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

# Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None
    
    # Returns row that corresponds to the whole album 
    # def findbyID(self, id):
    #     self._connection.execute('SELECT * from albums WHERE id = %s', [id])
    #     print("this is the album print")
    #     return f"{self.title}{self.release_year})"

    def getbyID(self, id):
        rows = self._connection.execute(f'SELECT * from albums WHERE id = {id}', [])
        # %s as well 
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums