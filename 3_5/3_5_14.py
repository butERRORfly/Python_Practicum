import json

from django.views.decorators.vary import vary_on_cookie


def main():
    with open("users.json", encoding="UTF-8") as file_in:
        users = json.load(file_in)

    with open("updates.json", encoding="UTF-8") as file_in:
        updates = json.load(file_in)



    for i in users:
        print(i)

if __name__ == '__main__':
    main()