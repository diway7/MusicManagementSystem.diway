class Artist:
    def __init__(self, name, bio=""):
        self.name = name
        self.bio = bio
        self.track_list = []

class Content:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def get_details(self):
        return f"{self.title} - {self.duration} min"

class Song(Content):
    def __init__(self, title, artist, duration, album, genre):
        super().__init__(title, artist, duration)
        self.album = album
        self.genre = genre
    def get_details(self):
        return f" Song: {self.title} | Album: {self.album} | Genre: {self.genre}"

class Podcast(Content):
    def __init__(self, title, artist, duration, episode_number, guest):
        super().__init__(title, artist, duration)
        self.episode_number = episode_number
        self.guest = guest
    def get_details(self):
        return f" Podcast Ep {self.episode_number}: {self.title} | Guest: {self.guest}"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.content_items = []
    def add_content(self, item):
        self.content_items.append(item)
    def calculate_total_duration(self):
        return sum(item.duration for item in self.content_items)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlists = {}
    def create_playlist(self, name):
        new_playlist = Playlist(name)
        self.playlists[name] = new_playlist
        return new_playlist

class MusicManager:
    def __init__(self):
        self.all_songs = []
        self.all_podcasts = []
        self.users = []
    def search_by_title(self, title):
        pass