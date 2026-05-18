import json
import os
from src.core import User, Playlist, Song, Podcast, Artist

class StorageManager:
    @staticmethod
    def save_data(users, all_content, filename="data.json"):
        data = {
            "users": [],
            "catalog": []
        }
        
        for user in users:
            user_dict = {
                "username": user.username,
                "password": user.password,
                "playlists": {
                    p_name: [item.title for item in p_obj.content_items]
                    for p_name, p_obj in user.playlists.items()
                }
            }
            data["users"].append(user_dict)
            
        for item in all_content:
            item_dict = {
                "title": item.title,
                "artist": item.artist.name,
                "duration": item.duration,
                "type": "song" if isinstance(item, Song) else "podcast"
            }
            if isinstance(item, Song):
                item_dict.update({"album": item.album, "genre": item.genre})
            elif isinstance(item, Podcast):
                item_dict.update({"episode_number": item.episode_number, "guest": item.guest})
            data["catalog"].append(item_dict)
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("[STORAGE] All changes saved to disk.")
        except IOError as e:
            print(f"[STORAGE ERROR] Could not save data: {e}")

    @staticmethod
    def load_data(manager, filename="data.json"):
        if not os.path.exists(filename):
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            artists_cache = {}
            for item in data.get("catalog", []):
                art_name = item["artist"]
                if art_name not in artists_cache:
                    artists_cache[art_name] = Artist(art_name)
                artist_obj = artists_cache[art_name]
                
                if item["type"] == "song":
                    manager.all_content.append(Song(item["title"], artist_obj, item["duration"], item["album"], item["genre"]))
                elif item["type"] == "podcast":
                    manager.all_content.append(Podcast(item["title"], artist_obj, item["duration"], item["episode_number"], item["guest"]))
            
            for u_data in data.get("users", []):
                user = User(u_data["username"], u_data["password"])
                for p_name, tracks in u_data.get("playlists", {}).items():
                    playlist = user.create_playlist(p_name)
                    for t_title in tracks:
                        track_obj = next((t for t in manager.all_content if t.title.lower() == t_title.lower()), None)
                        if track_obj:
                            playlist.add_content(track_obj)
                manager.users.append(user)
                
            print("[STORAGE] Data successfully loaded from backup.")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"[STORAGE ERROR] Data file is corrupted, starting fresh: {e}")