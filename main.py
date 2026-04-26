from src.core import Artist, Song, Podcast
def main():
    print("--- Music Management System Initialized ---")
    
    artist = Artist("The Weeknd")
    song = Song("Blinding Lights", artist, 3.5, "After Hours", "Synthwave")
    pod = Podcast("Late Night Talk", artist, 45, 12, "Bella Hadid")
    artist.track_list.append(song)
    artist.track_list.append(pod)
    print(f"Artist: {artist.name}")
    print(f"Added Song: {song.get_details()}")
    print(f"Added Podcast: {pod.get_details()}")
    print(f"\nTotal tracks by {artist.name}: {len(artist.track_list)}")

if __name__ == "__main__":
    main()