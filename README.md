
# MySQL User Management Script

This Python script allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a MySQL database table for managing user information.

## Features

- **Create a new user**: Add a new user to the `users` table.
- **Read user details**: Retrieve user details by user ID.
- **Update user details**: Update existing user information.
- **Delete a user**: Remove a user from the `users` table by user ID.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` library (can be installed via pip)

## Installation

1. Install Python 3.x if not already installed.
2. Install MySQL Server and set up a database named `user_db`.
3. Install the required Python package using pip:

    ```bash
    pip install mysql-connector-python
    ```

4. Ensure you have a `users` table in your `user_db` database with the following structure:

    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        active BOOLEAN DEFAULT TRUE
    );
    ```

## Usage

1. Modify the `connect_to_db()` function with your MySQL credentials.
2. Run the script:

    ```bash
    python script_name.py
    ```

3. The script provides basic functions:
   - `create_user(username, password, active=True)`: Creates a new user.
   - `read_user(user_id)`: Reads user details by ID.
   - `update_user(user_id, username=None, password=None, active=None)`: Updates user details.
   - `delete_user(user_id)`: Deletes a user by ID.

## Example

Here's an example usage of the script:

```python
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
delete_user(11)
```


