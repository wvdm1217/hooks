def reverse_string(string):
    return string[::-1]


if __name__ == "__main__":
    print(reverse_string("hello world"))
    print(reverse_string("goodbye world"))
    print(reverse_string("hello world") == "dlrow olleh")
