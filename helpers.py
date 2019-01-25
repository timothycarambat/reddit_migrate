import requests
import requests.auth

def get_user_token(client_id, client_secret, user):
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {"grant_type": "password", "username": user['username'], "password": user['pass']}
    headers = {"User-Agent": "python3.6/0.1"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    response = response.json()
    return response['access_token']

def get_subreddits(access_token):

    subreddits_subscribed = []
    friends_subscribed = []
    has_remaining_subs = True
    next_page = None

    while has_remaining_subs:
        headers = {
            "Authorization": f"bearer {access_token}",
            "User-Agent": "python3.6/0.1"
        }
        response = requests.get(
            f"https://oauth.reddit.com/subreddits/mine/subscriber.json{f'?after={next_page}' if next_page != None else ''}",
            headers=headers
        ).json()
        subs = response['data']['children']

        for sub in subs:
            sub_name = sub['data']['display_name']
            sub_id = sub['data']['name']
            if("u_" in sub_name):
                friends_subscribed.append(sub_id)
            else:
                subreddits_subscribed.append(sub_id)

        if response['data']['after'] != None:
            print(f"Fetching Next Page :: {response['data']['after']}")
            next_page = response['data']['after']
        else:
            has_remaining_subs = False

    return (subreddits_subscribed, friends_subscribed)


def subscribe_new_user(access_token, subs, type):
    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": "python3.6/0.1 by YourUsername"
    }
    post_data = {
    "action": "sub",
    "skip_initial_defaults": True,
    "sr": ",".join(subs)
    }

    response = requests.post("https://oauth.reddit.com/api/subscribe", data=post_data, headers=headers)
    if response.status_code == requests.codes.ok:
        print(f"New Account Now Subbed to all origin Account {type}")
    else:
        print(f"New Account Failed to be Subscribed to {type}")
    return True

def unsubscribe_new_user(access_token, subs, type):
    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": "python3.6/0.1 by YourUsername"
    }
    post_data = {
    "action": "unsub",
    "sr": ",".join(subs)
    }

    response = requests.post("https://oauth.reddit.com/api/subscribe", data=post_data, headers=headers)
    if response.status_code == requests.codes.ok:
        print(f"New Account Now Un-Subbed to all origin Account {type}")
    else:
        print(f"New Account Failed to be Unsubscribed to {type}")
    return True
