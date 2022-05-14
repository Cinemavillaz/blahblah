import os
import time

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "18473hsbbaau"


    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = 


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = "kdgsh3737"
    
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = "hehehe"


    # Your database name from mongoDB
    DATABASE_NAME = "Cluster0"


    # ID of users that can use the bot commands
    AUTH_USERS = [2737366, 7474747]


    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = "no"


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = "ueheheh384"


    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = "add"
    DELETE_FILTER_CMD = "del"
    DELETE_ALL_CMD = "delall"
    CONNECT_COMMAND = "connect"
    DISCONNECT_COMMAND = "disconnect"


    # To record start time of bot
    BOT_START_TIME = time.time()
