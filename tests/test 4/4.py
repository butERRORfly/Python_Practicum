import requests
from collections import defaultdict


def find_unique_strings():
    string_counts = defaultdict(int)
    seen_responses = set()
    url = "http://127.0.0.1:5000/"
    
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            response_tuple = tuple(sorted(data))
            
            if response_tuple in seen_responses:
                break
            seen_responses.add(response_tuple)
            

            for string in data:
                string_counts[string] += 1
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к серверу: {e}")
            break
    
    unique_strings = [string for string, count in string_counts.items() if count == 1]
    
    unique_strings_sorted = sorted(unique_strings, key=lambda s: s.lower(), reverse=True)
    
    for string in unique_strings_sorted:
        print(string)


if __name__ == "__main__":
    find_unique_strings()