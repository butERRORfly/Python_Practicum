def main():
    numbers = {15, 49, 36}
    print(dict(sorted({x: [y for y in range(1, x + 1) if x % y == 0] for x in numbers}.items())))
if __name__ == "__main__":
    main()
