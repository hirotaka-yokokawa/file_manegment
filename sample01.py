def main():

    f = open("users.txt", mode="r") #rはread

    text = f.read()

    print(text)

    f.close()


if __name__ == "__main__":
    main()
