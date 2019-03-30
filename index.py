import requests
import json
from pprint import pprint


r = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(r.text)

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

max_complete = top_users[0][1]

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

pprint(todos)