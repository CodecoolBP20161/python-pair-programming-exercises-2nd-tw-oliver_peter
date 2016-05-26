def palindrome(str):
    # for i in range(len(str)):
    str = str.replace(' ', '')
    if str.lower() == str.lower()[::-1]:
        return True
    else:
        return False


def main():
    str_input = input(str("Please enter a string! "))
    print(palindrome(str_input))
    return


if __name__ == '__main__':
    main()
