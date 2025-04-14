import requests


def get_and_sort_users():
    server_address = input().strip()

    if not server_address.startswith(('http://', 'https://')):
        server_address = 'http://' + server_address

    try:
        response = requests.get(f"{server_address}/users", timeout=5)
        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            print("No users found")
            return

        full_names = [
            f"{user['last_name']} {user['first_name']}"
            for user in users
            if 'last_name' in user and 'first_name' in user
        ]
        full_names_sorted = sorted(full_names)

        for name in full_names_sorted:
            print(name)

    except requests.exceptions.RequestException:
        print("Error connecting to server")
    except (ValueError, KeyError):
        print("Invalid data format from server")


if __name__ == "__main__":
    get_and_sort_users()
