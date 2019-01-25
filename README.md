# Reddit Account Migration

## What is this?
This project is to help with taking two reddit accounts and having the ability to have the subs and follows of the target account be automatically have the same subs and follows of the original account. This wont remove any subs on either account that are already there - only the ones being synced.

Found on [/r/programmingRequests](https://www.reddit.com/r/programmingrequests/comments/aj8tst/request_something_to_transfer_reddit/)


## Getting Setup:
- python >= 3.6; [Python Downloads](https://www.python.org/downloads/)
  - get this installed and running; make sure on a command line/terminal `python -V` is returning something
- be sure `pip` is installed (should be already)
- `pip install --user virtualenv`
- clone this directory anywhere onto your computer
- `cd reddit_migrate`
- `python virtualenv env`; this will create a directory in the folder named `env`
- Activate the virtual environment by `source env/bin/activate` (macOS terminal) OR `.\env\Scripts\activate` (windows cmd)
- if successful you should now see a `(env)` prepended to your terminal!
- `pip install -r requirements.txt`
- `cp .env.example .env` This will copy and create a new .env file in the root directory
- Open up the project in your editor and you're ready to copy paste some configuration.

## Configure your accounts:
Before you get started you will have to login to the two accounts you're trying to configure and do the following process. **You have to do this for BOTH accounts**

- Log in to Account One (this is the one you want to get the subreddits and follows from)
- Go to your [user preferences](https://www.reddit.com/prefs/apps)
- Click `Create/Develop App`
- Use the following settings for the field that appear:
    - Name: `Reddit Migrate`
    - select: `Script`
    - description: `You can put any text here`
    - about URL: leave empty
    - redirect URL: `https://reddit.com
    - Click create App!
- You will see the details get populated on the screen. There are two main ones we need here.
    - Under `personal use script` there is a string or random text. this is the `ORIGIN_CLIENT_ID` in `.env`
    - the text next to `secret` is the `ORIGIN_CLIENT_SECRET` in `.env`
    - set the `ORIGIN_USERNAME` and `ORIGIN_USERPASS`to the Account One's information
- Log out of the first account, log into the second account (the one you want to sync this information to) and repeat the process (even creating the app authorization!). This time all the information needs to get copied into the `NEW_XXX` variables of the `.env` file.
-
## Running the Script
- in the project root with the virtualenv activated.
- run `python migrate.py`
- You will see some outputs - any errors and it probably didnt work - email the creator of the script or start an issue
- Log into the second account
- WOW all your subreddits from account one and user follows are all there!
    - Wait... you said you messed up?
    - Open `migrate.py` in any editor and change the two lines that say `helpers.subscribe_new_user(..)` to `helpers.unsubscribe_new_user(...)`
    - run the script again and it will unsubscribe all the subscriptions that the origin account is also subbed to.

When you're all done go back to the preferences for each account and remove the authorized apps you just created to run this - since you don't need them anymore.
