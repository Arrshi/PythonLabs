import json

with open("in.json", "r") as read_file:
    data = json.load(read_file)

todos_by_user = {}
list = []

for item in data:
    if item["completed"]:
        try:
            todos_by_user[item["userId"]] += 1
        except KeyError:
            todos_by_user[item["userId"]] = 1

for key, value in todos_by_user.items():
    d = dict()
    d["userID"] = key
    d["task_completed"] = value
    list.append(d)

with open("out.json", "w") as write_file:
    json.dump(list, write_file)