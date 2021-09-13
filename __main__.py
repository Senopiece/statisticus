from pyrogram import Client, filters
from collections import defaultdict
import os

results = defaultdict(lambda: 0)

api_id = os.environ["TELEGRAM_APP_API_ID"]
api_hash = os.environ["TELEGRAM_APP_API_HASH"]


with Client("surikat", api_id, api_hash) as app:
    chat = input("Enter chat name/id: ")
    upper_edge = int(input("Upper edge (unix time): "))
    #lower_edge = int(input("Lower edge (unix time): "))
    
    for msg in app.iter_history(chat, 10):
        if msg.date < upper_edge:
            break
        
        if msg.from_user.username != None:
            results[msg.from_user.username] += 1
        else:
            results[msg.from_user.id] += 1


i = 0
for user, activity in sorted(results.items(), key = lambda item: item[1], reverse = True):
    i += 1
    print("`{}. {} ({})`".format(i, user, activity))
