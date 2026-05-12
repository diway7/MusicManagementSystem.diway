import json
import os

class StorageManager:
    @staticmethod
    def save_data(users, filename="data.json"):
        data = []
        for user in users:
            user_dict = {
                "username": user.username,
                "password": user.password,
                "playlists": {
                    p_name: [item.title for item in p_obj.content_items]
                    for p_name, p_obj in user.playlists.items()
                }
            }
            data.append(user_dict)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)