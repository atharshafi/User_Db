import mysql.connector

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="14941",
        database="user_db"
    )

# Create a new user
def create_user(username, password, active=True):
    db = connect_to_db()
    cursor = db.cursor()
    query = "INSERT INTO users (username, password, active) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, active))
    db.commit()
    print(f"User '{username}' created with ID: {cursor.lastrowid}")
    cursor.close()
    db.close()

# Read user details
def read_user(user_id):
    db = connect_to_db()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user

# Update user details
# Update user details and return the updated user
def update_user(user_id, username=None, password=None, active=None):
    db = connect_to_db()
    cursor = db.cursor()
    query = "UPDATE users SET "
    values = []

    if username is not None:
        query += "username = %s, "
        values.append(username)
    if password is not None:
        query += "password = %s, "
        values.append(password)
    if active is not None:
        query += "active = %s, "
        values.append(active)

    query = query.rstrip(', ')  # Remove the trailing comma
    query += " WHERE id = %s"
    values.append(user_id)

    cursor.execute(query, tuple(values))
    db.commit()

    # Retrieve and return the updated user details
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    updated_user = cursor.fetchone()

    cursor.close()
    db.close()

    print(f"User with ID: {user_id} updated.")
    return updated_user


# Delete a user
def delete_user(user_id):
    db = connect_to_db()
    cursor = db.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    db.commit()
    print(f"User with ID: {user_id} deleted.")
    cursor.close()
    db.close()

# Example usage
if __name__ == "__main__":
    # Create a new user
    create_user("user1", "userpswd121")
    print("User Created")

    # Read user details
    user = read_user(11)
    print("User Details:", user)

    # Update user details
    update_user(11, username="User11", active=True)
    user = read_user(11)
    print("User Details:", user)

# Delete a user
    delete_user(1)

