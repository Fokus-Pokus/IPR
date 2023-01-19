import json
import requests as requests

#data =""" {
   # "president": {
   #     "name": "Zaphod Beeblebrox",
  #      "species": "Betelgeusian"
   # }
#}
#with open("values.json", "r") as read_file:
    #data = json.load(read_file)
   # print(data)"""

#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#todos = json.loads(response.text)
#with open("data_file.json", "w") as write_file:
#    json.dump(todos, write_file, indent=4)

with open("data_file.json", "r") as read_file:
    todos = json.load(read_file)
    print(todos)
    todos_by_user = {}
    #print(todos[:3])
    # Увеличение выполненных задач каждым пользователем.
    for todo in todos:
        
        if todo["completed"]:
            print(todo)
            try:
                # Увеличение количества существующих пользователей.
                todos_by_user[todo["userId"]] += 1
            except KeyError:
                # Новый пользователь, ставим кол-во 1.
                todos_by_user[todo["userId"]] = 1

    # Создание отсортированного списка пар (userId, num_complete).
    top_users = sorted(todos_by_user.items(),
                       key=lambda x: x[1], reverse=True)
    print(top_users)

    # Получение максимального количества выполненных задач.
    max_complete = top_users[0][1]

    # Создание списка всех пользователей, которые выполнили
    # максимальное количество задач.
    users = []
    for user, num_complete in top_users:
        if num_complete < max_complete:
            break
        users.append(str(user))

    max_users = " and ".join(users)
