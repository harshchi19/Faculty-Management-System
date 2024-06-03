import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Read the image file as binary data
image_path = 'Meera.jpg'
with open(image_path, 'rb') as f:
    image_data = f.read()

# Convert binary data to hexadecimal string
hex_image_data = image_data.hex()

# Update the database with the hexadecimal image data for a specific user
username = 6
cursor.execute("UPDATE faculty SET Profile_Image = x'" + hex_image_data + "' WHERE id = ?", (username,))

# Commit the transaction and close the connection
conn.commit()
conn.close()
