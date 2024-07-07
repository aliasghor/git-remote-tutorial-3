import student as sdt

def main() -> None:
    ali = sdt.Student("Ali",21)
    gerry = sdt.Student("Gerry",10)
    print(ali)
    print(gerry)

    ali.greet(gerry)

if __name__ == '__main__':
    main()