if __name__ == "__main__":
    number = int(input("숫자를 입력해주세요. : "))

    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    print(divisors)
