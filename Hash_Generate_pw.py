import hashlib


# Function to hash a password using hashlib
def hash_password(plain_password):
    password_bytes = plain_password.encode('utf-8')
    # Create a hash object
    hash_object = hashlib.sha256(password_bytes)

    hashed_password = hash_object.hexdigest()
    return hashed_password


# Function to store hashed password
def store_password(user_id, email, plain_password, storage):
    hashed_password = hash_password(plain_password)
    storage[user_id] = {'email': email, 'password': hashed_password}
    print(f"Password for user ID '{user_id}' stored successfully!")


# Function to delete a user by ID
def delete_user(user_id, storage):
    if user_id in storage:
        del storage[user_id]
        print(f"User ID '{user_id}' deleted successfully!")
    else:
        print(f"User ID '{user_id}' not found.")


def display_stored_passwords(storage):
    print("\n+\t\t+-\t\t\t\t\t\t\t\t\t+")
    print("| Id | Email\t\t\t| Password\t\t\t\t|")
    print("+\t\t+-\t\t\t\t\t\t\t\t\t+")
    for user_id, details in storage.items():
        print(f"| {user_id:<2} | {details['email'][:12]:<14} | {details['password']} |")
    print("+\t\t+-\t\t\t\t\t\t\t\t\t+")


def main():
    # In-memory storage for demonstration purposes
    password_storage = {}

    while True:
        print("\nOptions:")
        print("1. Add a user")
        print("2. Delete a user")
        print("3. Display stored passwords")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            user_id = input("\nEnter user ID: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            store_password(user_id, email, password, password_storage)
        elif choice == '2':
            user_id = input("\nEnter user ID to delete: ")
            delete_user(user_id, password_storage)
        elif choice == '3':
            display_stored_passwords(password_storage)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

