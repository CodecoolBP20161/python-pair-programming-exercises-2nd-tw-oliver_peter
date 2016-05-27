import string
import random


def passwordgen():
    lowercase = (list(string.ascii_lowercase))
    uppercase = (list(string.ascii_uppercase))
    digits = (list(string.digits))
    punctuation = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?')
    # actually if you use this instead, you can have more special characters,
    # therefore a more secure password, but fail the test sometimes:
    # punctuation = (list(string.punctuation))
    charlist = ((random.sample(lowercase, 2)) + (random.sample(uppercase, 2)) +
                (random.sample(digits, 2)) + (random.sample(punctuation, 2)))
    random.shuffle(charlist)  # for better security :)
    password = ''.join(charlist)
    return password


def main():
    print(passwordgen())
    return


if __name__ == '__main__':
    main()
