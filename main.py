from src.core import MusicManager, Artist, Song

def main():
    manager = MusicManager()
    
    the_weeknd = Artist("The Weeknd")
    manager.all_songs.append(Song("Blinding Lights", the_weeknd, 3.2, "After Hours", "Synthwave"))
    manager.all_songs.append(Song("Save Your Tears", the_weeknd, 3.6, "After Hours", "Synthpop"))

    current_user = None

    print("--- Melodix ---")

    while True:
        if not current_user:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            
            choice = input("\nSelect an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                manager.register_user(username, password)
                print("User registered successfully!")

            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                user = manager.login(username, password)
                if user:
                    current_user = user
                    print(f"\nSuccessfully logged in! Welcome, {current_user.username}!")
                else:
                    print("\nInvalid credentials!")

            elif choice == "3":
                print("Goodbye!")
                break
        else:
            print(f"\n--- User Menu ({current_user.username}) ---")
            print("1. Search songs")
            print("2. Create Playlist")
            print("3. View my Playlists")
            print("4. Logout")

            user_choice = input("\nSelect an option: ")

            if user_choice == "1":
                title = input("Enter song title to search: ")
                results = manager.search_by_title(title)
                if results:
                    for i, item in enumerate(results):
                        print(f"{i+1}. {item.get_details()}")
                else:
                    print("Nothing found.")

            elif user_choice == "2":
                p_name = input("Enter playlist name: ")
                current_user.create_playlist(p_name)
                print(f"Playlist '{p_name}' created!")

            elif user_choice == "4":
                current_user = None
                print("Logged out.")

if __name__ == "__main__":
    main()