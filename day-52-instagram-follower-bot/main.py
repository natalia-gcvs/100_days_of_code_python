from insta_followers import InstaFollowers

SIMILAR_ACCOUNT = 'Instagram account you want to target'
USERNAME = "Your username"
PASSWORD = "Your password"

insta_followers = InstaFollowers()

insta_followers.login(username_=USERNAME, password_=PASSWORD)

insta_followers.find_followers(similar_account=SIMILAR_ACCOUNT)

insta_followers.follow()




