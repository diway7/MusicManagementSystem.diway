import unittest
from src.core import MusicManager, Artist, Song, Playlist, User
class TestMusicManagementSystem(unittest.TestCase):

    def setUp(self):
        self.manager = MusicManager()
        self.artist = Artist("Linkin Park", "Rock band")
        self.song1 = Song("In the End", self.artist, 3.36, "Hybrid Theory", "Nu Metal")
        self.song2 = Song("Numb", self.artist, 3.07, "Meteora", "Nu Metal")
        self.manager.all_content.extend([self.song1, self.song2])

    def test_user_registration_success(self):
        user = self.manager.register_user("test_user", "password123")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "test_user")
        self.assertIn(user, self.manager.users)

    def test_user_registration_duplicate_edge_case(self):
        self.manager.register_user("unique_user", "pass1")
        duplicate_user = self.manager.register_user("unique_user", "pass2")
        self.assertIsNone(duplicate_user)
        self.assertEqual(len(self.manager.users), 1)

    def test_playlist_duration_calculation(self):
        playlist = Playlist("Rock Vibes")
        playlist.add_content(self.song1)
        playlist.add_content(self.song2)
        
        expected_duration = round(3.36 + 3.07, 2)
        self.assertEqual(playlist.calculate_total_duration(), expected_duration)

    def test_remove_content_from_playlist(self):
        playlist = Playlist("My Favs")
        playlist.add_content(self.song1)
        playlist.add_content(self.song2)
        playlist.remove_content("In the End")
        
        self.assertEqual(len(playlist.content_items), 1)
        self.assertEqual(playlist.content_items[0].title, "Numb")

    def test_search_functionality(self):
        results = self.manager.search_by_title("numb")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Numb")


if __name__ == "__main__":
    unittest.main()