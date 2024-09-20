def main():
    name = input("Как Вас зовут?\n")
    print(f"Здравствуйте, {name}!")
    vibe = input("Как дела?\n")
    if vibe == "хорошо":
        print("Я за вас рада!")
    if vibe == "плохо":
        print("Всё наладится!")


if __name__ == '__main__':
    main()