active_users = set()

while True:
    print("===== Chat Room Menu =====")
    print("1. Join Chat")
    print("2. Leave Chat")
    print("3. Show Active Users")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    match choice:
        case '1':
            username = input("Enter username to join: ")
            if username in active_users:
                print(f"3User '{username}' is already in the chat!")
            else:
                active_users.add(username)
                print(f"User '{username}' joined the chat.")

        case '2':
            username = input("Enter username to leave: ")
            if username in active_users:
                active_users.remove(username)
                print(f"User '{username}' left the chat.")
            else:
                print(f"User '{username}' is not in the chat!")

        case '3':
            if active_users:
                print("Active Users:", ", ".join(active_users))
            else:
                print("No active users in the chat.")

        case '4':
            print("Exiting chat room. Goodbye!")
            break

        case _:
            print("Invalid choice! Please enter a number between 1 and 4.")
