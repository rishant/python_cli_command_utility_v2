# routers/user_router.py
import json

from decorators.command_decorator import command

from services.user_service import UserService
from models.user import User


class UserRouter:
    def __init__(self):
        self.user_service = UserService()

    @command('create_user')
    def create_user(self, mongo_uri, user_data):
        # Validate Request
        # Convert input request into model class
        user = User.from_dict(user_data)
        user_id = self.user_service.create_user(mongo_uri, user)
        return f"User created with ID: {str(user_id)}"

    @command('get_user_by_id')
    def get_user_by_id(self, mongo_uri, user_id):
        # Validate Request
        user = self.user_service.get_user_by_id(mongo_uri, user_id)
        if user:
            user = user.to_dict()
            user['_id'] = str(user['_id'])
            return json.dumps(user)
        else:
            return f"User with ID {user_id} not found"

    @command('get_user')
    def get_user(self, mongo_uri, username):
        # Validate Request
        user = self.user_service.get_user(mongo_uri, username)
        if user:
            return user
        else:
            return f"User with ID {username} not found"

    @command('update_user')
    def update_user(self, mongo_uri, user_id, update_data):
        user = User.from_dict(update_data)
        modified_count = self.user_service.update_user(mongo_uri, user_id, user)
        if modified_count > 0:
            return f"User with ID {user_id} updated successfully"
        else:
            return f"User with ID {user_id} not found"

    @command('delete_user')
    def delete_user(self, mongo_uri, user_id):
        deleted_count = self.user_service.delete_user(mongo_uri, user_id)
        if deleted_count > 0:
            return f"User with ID {user_id} deleted successfully"
        else:
            return f"User with ID {user_id} not found"
