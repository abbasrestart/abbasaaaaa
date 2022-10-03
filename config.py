## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME  =  getenv ( "SESSION_NAME" ، "AgCruSR0Ps84zEy9bBOHNQ8YJlh7UA72voA-fM8VxQKiEXiExXQ-m61sPj1Bx9cf9GCY66DvNiNaR0AyibhMEeDUdvLLztlYOJ7YZqh60Yx3rjfkNE2I-rO2E74ef8xvdcMmt03lXIa8ukrkV0Em6wwaBly4PABITHP7wr_jc-K8BCCg95r_5kdHYdr_uqzWuiuZv_V4b90E8LSDz_BtoV7UcSUhKJ3EUvxuU5elKuzcZhK8dr2MTIwxaem_-1xu9W3WSTCk4NDr8rioW6S0qLZrHZDtPYJtoMUY4G7UNJVMabYBmgdNb9477xFcumcv0PFG4YKudRbqZileT7f1Z5U7WrsDVgA" )
BOT_TOKEN  =  getenv ( "BOT_TOKEN" ، "5749237753:AAFrEpw8eqP9PWKNFcEWh3Evc3XCJXjTs_A" )
BOT_NAME      =      getenv ( "BOT_NAME"     ،     "اغاني"   )
API_ID   =   int ( getenv ( "API_ID"  ،  "13554830" ))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME  =  getenv ( "OWNER_USERNAME" ، "A_B_B_A_S_2007" )
ALIVE_NAME   =   getenv ( "ALIVE_NAME"  ،  "عباس" )
BOT_USERNAME  =  getenv ( "BOT_USERNAME" ، "Grops_hemaia_bot" )
OWNER_ID  =  getenv ( "OWNER_ID" ، "13554830" )
ASSISTANT_NAME  =  getenv ( "ASSISTANT_NAME" ، "A_B_B_A_S_2007" )
GROUP_SUPPORT  =  getenv ( "GROUP_SUPPORT" ، "a_b_b_a_s_grobe" )
UPDATES_CHANNEL  =  getenv ( "UPDATES_CHANNEL" ، "we94my" )
HEROKU_APP_NAME  =  getenv ( "HEROKU_APP_NAME" )
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
