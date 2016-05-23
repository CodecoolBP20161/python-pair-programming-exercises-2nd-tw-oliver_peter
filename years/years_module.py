import datetime


def years(age):
    now = datetime.datetime.now()
    return (now.year)+(100-age)


def main():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    print(name, "will be 100 years old in", years(age))
    return


if __name__ == '__main__':
    main()
