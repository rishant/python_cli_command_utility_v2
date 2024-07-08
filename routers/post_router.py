# routers/post_router.py
import requests

from decorators.command_decorator import command


class PostRouter:
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    @command('get_posts')
    def get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        return response.json()

    @command('get_external_posts')
    def get_posts(self, api_uri):
        response = requests.get(f"{api_uri}")
        return response.json()