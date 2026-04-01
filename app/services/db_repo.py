from appwrite.services.databases import Databases
from .appwrite_client import get_appwrite_client

class ProfileRepository:
    def __init__(self):
        client = get_appwrite_client()
        self.db = Databases(client)
        self.db_id = 'main_db'
        self.col_id = 'profiles'

    def create_profile(self, user_id, name, bio, links, photo_id):
        return self.db.create_document(
            database_id=self.db_id,
            collection_id=self.col_id,
            document_id='unique()',
            data={
                'userId': user_id,
                'name': name,
                'bio': bio,
                'links': links,
                'photoId': photo_id
            }
        )