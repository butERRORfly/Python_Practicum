from itertools import combinations


def main():
    masty = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
    nominal = [
        "10",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "валет",
        "дама",
        "король",
        "туз",
    ]
    mast_in = input()
    nominal_out = input()
    rasklad_before = tuple(input().split(", "))

    coloda = [n + " " + masty[m] for n in nominal for m in masty]

    out_3_cards = combinations(sorted(coloda), 3)

    flag_next = False
    for rasklad in out_3_cards:
        if (
            flag_next
            and all(nominal_out not in i for i in rasklad)
            and any(masty[mast_in] in i for i in rasklad)
        ):
            print(", ".join(rasklad))
            break
        if rasklad == rasklad_before:
            flag_next = True


if __name__ == "__main__":
    main()
