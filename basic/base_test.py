def convert(num, base):
    T = "0123456789ABCDEF"
    quotient, remainder = divmod(num, base)

    if quotient == 0:
        return T[remainder]
    else:
        return convert(quotient, base) + T[remainder]


if __name__ == "__main__":
    num_10 = 236

    num_2 = bin(num_10)  # 접두어 "0b"가 붙음
    num_8 = oct(num_10)
    num_16 = hex(num_10)

    print("10 -> 2 : ", num_2)
    print("10 -> 8 : ", num_8)
    print("10 -> 16 : ", num_16)
    print("=================")

    # int(x, base=10)
    print("2 -> 10 : ", int(num_2, 2))
    print("8 -> 10 : ", int(num_8, 8))
    print("16 -> 10 : ", int(num_16, 16))
    print("=================")

    print(convert(num_10, 2))
    print(convert(num_10, 8))
    print(convert(num_10, 16))

    print("=================")
    print(int(convert(num_10, 2), 2))
    print(int(convert(num_10, 8), 8))
    print(int(convert(num_10, 16), 16))
