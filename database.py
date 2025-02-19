import sqlite3

DB_NAME = "hotel.db"

def create_db():
    """Creates the database and the Rooms table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            is_available BOOLEAN NOT NULL DEFAULT 1,
            is_paid BOOLEAN NOT NULL DEFAULT 0,
            people_inside INTEGER NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

def add_room( is_available=True, is_paid=False, people_inside=0):
    """Adds a new room to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Rooms ( is_available, is_paid, people_inside)
        VALUES ( ?, ?, ?)
    """, ( is_available, is_paid, people_inside))
    

    conn.commit()
    conn.close()

def get_rooms():
    """Fetches all room details."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Rooms")
    rooms = cursor.fetchall()

    conn.close()
    return rooms

def update_room_status(room_id, is_available=None, is_paid=None, people_inside=None):
    """Updates a room's availability, payment status, or number of people inside."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if is_available is not None:
        cursor.execute("UPDATE Rooms SET is_available = ? WHERE room_id = ?", (is_available, room_id))
    
    if is_paid is not None:
        cursor.execute("UPDATE Rooms SET is_paid = ? WHERE room_id = ?", (is_paid, room_id))
    
    if people_inside is not None:
        cursor.execute("UPDATE Rooms SET people_inside = ? WHERE room_id = ?", (people_inside, room_id))
    
    conn.commit()
    conn.close()

def delete_room(room_id):
    """Deletes a room from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Rooms WHERE room_id = ?", (room_id,))

    conn.commit()
    conn.close()

# Run this once to create the database
if __name__ == "__main__":
    create_db()
