from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
def test_get_home(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_table.sql")
    page.goto(f"http://{test_web_address}/home")
    h1_tags = page.locator("h1")
    a_tags = page.locator("a")
    expect(h1_tags).to_have_text([
        'Albums'
    ])
    expect(a_tags).to_have_text([
        'Click me to go to albums list!'
    ])

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    # page.screenshot(path="screenshot.png", full_page=True)
    expect(h2_tags).to_have_text([
        'Hypnotised','Rumours'
    ])
    

def test_get_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_table.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        'Rumours'
    ])

def test_get_by_release(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_table.sql")
    page.goto(f"http://{test_web_address}/albums/2/released")
    h1_tags = page.locator("h1")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text([
        'Album details'
    ])
    expect(h2_tags).to_have_text([
        'Rumours'
    ])
    expect(p_tags).to_have_text([
        'Released: 1977'
    ])