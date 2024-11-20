import json

item = ["category", "created_at", "description", "difficulty", "firstblood", "flag", "hint", "id", "requires_launch_button", "score", "solves", "task_definition", "title"]
data = {}
count = 0

while count < len(item):
  x = input(f"{item[count]}: ")
  
  if x == "q":
    break
  
  data[item[count]] = x
  count += 1

json_data = json.dumps(data, indent=4)

with open('output.json', 'w') as file:
  file.write(json_data)

print("Data saved to output.json")
