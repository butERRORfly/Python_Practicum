import re
from itertools import product
def main():
    class AmiBool:
        def __init__(self, value):
            self.value = value

        def __net__(self):
            return AmiBool(not self.value)

        def __oreo__(self, other):
            return AmiBool(self.value or other.value)

        def __andeo__(self, other):
            return AmiBool(self.value and other.value)

        def _xor__(self, other):
            return AmiBool(self.value != other.value)

        def __implication__(self, other):
            return AmiBool((not self.value) or other.value)

        def __equal__(self, other):
            return AmiBool(self.value == other.value)

        def __str__(self):
            return '1' if self.value else '0'

    string = input()
    variables = sorted(set(re.findall(r"[A-Z]", string)))
    print(' '.join(sorted(set(variables))), 'F')

    vars_mental = {}
    for var in product([0, 1], repeat=len(set(variables))):
        for num in var:
            for i, key in reversed(list(enumerate(reversed(variables)))):
                vars_mental[key] = AmiBool(i)
        result = eval(string, {}, vars_mental)
        print(*var, result)
    print(vars_mental)



if __name__ == "__main__":
    main()
