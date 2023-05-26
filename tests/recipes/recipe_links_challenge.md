# 03 Using Links Recipe 

```
#USER STORY:


As a music lover,
So I can organise my records,
I want to see a webpage with a list of my favourite artists. 

As a music lover,
So I can organise my records,
I want to be able to see details for a single artist.
```

```
Nouns:

artists, names, genres
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| artists               | name, genre         |

Name of the table (always plural): `artists`

Column names: `name`, `genre`

## 3. Decide the column types

```

id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);


# Plain Route Design Recipe 04.Test-Driving Route with Database: Chalenge

## 1. Design the Route Signature

# Request:
GET /artists 
GET / artists / <id> 


# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

## 2. Create Examples as Tests

# GET /artists
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone
"""

# GET /artists / 1
# Expected response (200 OK):
"""
Name: Pixies, Genre: Indie
"""




## 3. Test-drive the Route


/ artists (all)
/ artists / id (single artist details to show genre)

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/artist_table.sql")
    page.goto(f"http://{test_web_address}/artists")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text([
        'Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone'
    ])
    

def test_get_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/artist_table.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("h1")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h1_tags).to_have_text([
        'Artist details' 
    ])
    expect(h2_tags).to_have_text([
        'Name: Pixies'
    ])
    expect(paragrah_tags).to_have_text([
        'Genre: Indie'
    ])


