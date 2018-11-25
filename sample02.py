def main():
    f = open("users.txt", mode="r") #データの読み込みができる｡

    text = f.read()

    lines = text.split("\n")

    for line in lines: # リストが出てきたらfor文使おう｡
        user = line.split(",")

        info = f"{user[0]}さんは{user[1]}歳です"

        print(info)

    f.close()  #読んだら閉じよう｡


if __name__ == "__main__":
    main()
