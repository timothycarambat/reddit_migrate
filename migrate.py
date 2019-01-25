import os
import helpers
from dotenv import load_dotenv
load_dotenv()

origin_client_secret = os.getenv("ORIGIN_CLIENT_SECRET")
origin_client_id = os.getenv("ORIGIN_CLIENT_ID")
new_client_secret = os.getenv("NEW_CLIENT_SECRET")
new_client_id = os.getenv("NEW_CLIENT_ID")

origin_user = {
    'username': os.getenv("ORIGIN_USERNAME"),
    'pass': os.getenv("ORIGIN_USERPASS")
}
new_user = {
    'username': os.getenv("NEW_USERNAME"),
    'pass': os.getenv("NEW_USERPASS")
}

access_token = helpers.get_user_token(origin_client_id, origin_client_secret, origin_user)
(subs, friend_subs) = helpers.get_subreddits(access_token)

new_access_token = helpers.get_user_token(new_client_id, new_client_secret, new_user)

helpers.subscribe_new_user(new_access_token, subs, 'Subreddits')
helpers.subscribe_new_user(new_access_token, friend_subs, 'Followers')
