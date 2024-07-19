
from db.operations import MySQLDB

def main():
    db = MySQLDB()

    # Create a user
    db.create_user("Ivan Ivanov", "ivan.ivanov@example.com")

    # Read users
    print("Users:")
    db.get_users()

    # Update a user's email
    user_id = int(input("Enter user ID to update: "))
    db.update_user_email(user_id, "ivan.newemail@example.com")

    # Read users again to see the update
    print("Updated Users:")
    db.get_users()

    # Delete a user
    user_id = int(input("Enter user ID to delete: "))
    db.delete_user(user_id)

    # Read users again to see the deletion
    print("Users after deletion:")
    db.get_users()

    # Close the connection
    db.close_connection()

if __name__ == "__main__":
    main()

