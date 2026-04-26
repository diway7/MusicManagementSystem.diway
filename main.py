from src.core import Artist, Song, Podcast, User
def main():
    print("---  Melodix: Music Management System ---\n")
    artist = Artist("The Weeknd", "Canadian pop star")
    song1 = Song("Blinding Lights", artist, 3.2, "After Hours", "Synthwave")
    song2 = Song("Save Your Tears", artist, 3.6, "After Hours", "Synthpop")
    
    user = User("Melody_Girl", "pass123")
    print(f" Welcome, {user.username}!")
    my_favs = user.create_playlist("Cozy Vibes")
    print(f"Created playlist: '{my_favs.name}'")
    my_favs.add_content(song1)
    my_favs.add_content(song2)
    
    print("\n--- Current Playlist Details ---")
    for item in my_favs.content_items:
        print(item.get_details())
    total_time = my_favs.calculate_total_duration()
    print(f"\nTotal duration: {total_time} minutes")
    print(f"System check: Complete for Week 1")

if __name__ == "__main__":
    main()