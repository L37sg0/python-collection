# import requests module
import requests

response = requests.get("https://gitlab.com/api/v4/users/L37sg0/projects")
# print(response.text)
# print(response.json()[0])
my_projects = response.json()
for project in my_projects:
    print(project['id'])
    print(project['name'])