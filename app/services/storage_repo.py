from appwrite.services.storage import Storage
from .appwrite_client import get_appwrite_client

class AvatarRepository:
    def __init__(self):
        client = get_appwrite_client()
        self.storage = Storage(client)
        self.bucket_id = 'avatars'

    def upload_avatar(self, photo_file):
        result = self.storage.create_file(
            bucket_id=self.bucket_id,
            file_id='unique()',
            file=photo_file
        )
        return result['$id'] # Retorna apenas o ID para salvar no banco