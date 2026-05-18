from src.core import MusicManager, Artist, Song, Podcast
from src.storage import StorageManager

def main():
    manager = MusicManager()
    StorageManager.load_data(manager)
    if not manager.all_content:
        the_weeknd = Artist("The Weeknd")
        manager.all_content.append(Song("Blinding Lights", the_weeknd, 3.2, "After Hours", "Synthwave"))
        manager.all_content.append(Song("Save Your Tears", the_weeknd, 3.6, "After Hours", "Synthpop"))
        manager.all_content.append(Podcast("AI Future", Artist("Tech Talk"), 45.0, 12, "Sam Altman"))
        
    current_user = None
    print("--- Welcome to Melodix ---")

    while True:
        if not current_user:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("\nSelect an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if manager.register_user(username, password):
                    print("User registered successfully!")
                    StorageManager.save_data(manager.users, manager.all_content)

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
            print("1. Search content (Songs/Podcasts)")
            print("2. Create Playlist")
            print("3. View my Playlists & Stream")
            print("4. Logout")

            user_choice = input("\nSelect an option: ")

            if user_choice == "1":
                title = input("Enter title to search: ")
                results = manager.search_by_title(title)
                if results:
                    for i, item in enumerate(results):
                        print(f"{i+1}. {item.get_details()}")
                    
                    add_choice = input("\nWant to add a track to a playlist? (yes/no): ").lower()
                    if add_choice == "yes":
                        if not current_user.playlists:
                            print("You don't have any playlists yet! Create one first.")
                        else:
                            try:
                                track_idx = int(input("Enter track number from search: ")) - 1
                                p_name = input("Enter your playlist name: ")
                                if p_name in current_user.playlists and 0 <= track_idx < len(results):
                                    current_user.playlists[p_name].add_content(results[track_idx])
                                    print(f"Added to '{p_name}'!")
                                    StorageManager.save_data(manager.users, manager.all_content)
                                else:
                                    print("Playlist not found or invalid selection.")
                            except ValueError:
                                print("Invalid input! Please enter a number.")
                else:
                    print("Nothing found.")

            elif user_choice == "2":
                p_name = input("Enter playlist name: ")
                current_user.create_playlist(p_name)
                print(f"Playlist '{p_name}' created!")
                StorageManager.save_data(manager.users, manager.all_content)

            elif user_choice == "3":
                if not current_user.playlists:
                    print("You have no playlists yet.")
                else:
                    for p_name, p_obj in current_user.playlists.items():
                        print(f"\n--- Playlist: {p_name} (Created: {p_obj.created_at}) ---")
                        print(f"Total duration: {p_obj.calculate_total_duration()} mins")
                        if not p_obj.content_items:
                            print("  [Empty]")
                        for item in p_obj.content_items:
                            print(f"  - {item.title} ({item.duration} min)")
                    
                    stream_choice = input("\nDo you want to simulate live streaming a playlist? (yes/no): ").lower()
                    if stream_choice == "yes":
                        p_to_stream = input("Enter playlist name to stream: ")
                        if p_to_stream in current_user.playlists:
                            playlist = current_user.playlists[p_to_stream]
                            print("\n--- Connecting to Stream Server ---")
                            
                            for track_stream_log in playlist.stream_tracks():
                                print(track_stream_log)
                        else:
                            print("Playlist not found.")

            elif user_choice == "4":
                current_user = None
                print("Logged out.")

if __name__ == "__main__":
    main()