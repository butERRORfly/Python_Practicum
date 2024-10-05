def find_second_level_friends(friend_pairs):
    friends_map = {}
    for person1, person2 in friend_pairs:
        friends_map[person1] = friends_map.get(person1, set()) | set([person2])
        friends_map[person2] = friends_map.get(person2, set()) | set([person1])

    second_level_friends = {}
    for person in friends_map:
        direct_friends = friends_map[person]
        second_level_set = set()
        for friend in direct_friends:
            second_level_set.update(friends_map[friend])
        second_level_set.discard(person)
        second_level_set.difference_update(direct_friends)
        second_level_friends[person] = sorted(second_level_set)

    return second_level_friends


def main():
    friend_pairs = []
    while line := input():
        person1, person2 = list(map(str, line.split()))
        friend_pairs.append((person1, person2))

    second_level_friends = find_second_level_friends(friend_pairs)
    for person in sorted(second_level_friends):
        friends_list = ', '.join(second_level_friends[person])
        print(f"{person}: {friends_list}")


if __name__ == "__main__":
    main()
