def can_eat(warrior1, warrior2):
    return True if sorted([abs(warrior1[0] - warrior2[0]), abs(warrior1[1] - warrior2[1])]) == [1, 2] else False
