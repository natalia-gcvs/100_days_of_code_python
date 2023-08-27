import requests


class Post:
    def __init__(self, id):
        self.id = id

    def get_post(self):
        blog_posts = requests.get(" https://api.npoint.io/c790b4d5cab58020d391").json()
        for post in blog_posts:
            if post['id'] == self.id:
                return post


