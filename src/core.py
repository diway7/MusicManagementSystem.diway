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

class Song(Content):
    def __init__(self, title, artist, duration, album, genre):
        super().__init__(title, artist, duration)
        self.album = album
        self.genre = genre

class Podcast(Content):
    def __init__(self, title, artist, duration, episode, guest):
        super().__init__(title, artist, duration)
        self.episode = episode
        self.guest = guest