def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Action: '{func.__name__}' executed successfully.")
        return result
    return wrapper

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
        return f" Song: {self.title} | Artist: {self.artist.name} | Album: {self.album} | Genre: {self.genre}"

class Podcast(Content):
    def __init__(self, title, artist, duration, episode_number, guest):
        super().__init__(title, artist, duration)
        self.episode_number = episode_number
        self.guest = guest

    def get_details(self):
        return f"Podcast Ep {self.episode_number}: {self.title} | Guest: {self.guest}"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.content_items = []

    def add_content(self, item):
        self.content_items.append(item)

    def remove_content(self, title):
        self.content_items = [item for item in self.content_items if item.title.lower() != title.lower()]

    def calculate_total_duration(self):
        return round(sum(item.duration for item in self.content_items), 2)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlists = {}

    @log_action
    def create_playlist(self, name):
        new_playlist = Playlist(name)
        self.playlists[name] = new_playlist
        return new_playlist

class MusicManager:
    def __init__(self):
        self.all_content = []
        self.users = []

    def search_by_title(self, title):
        return [item for item in self.all_content if title.lower() in item.title.lower()]

    @log_action
    def register_user(self, username, password):
        if any(u.username == username for u in self.users):
            print(f"User '{username}' already exists!")
            return None
        new_user = User(username, password)
        self.users.append(new_user)
        return new_user

    def login(self, username, password):
        for u in self.users:
            if u.username == username and u.password == password:
                return u
        return None