def main():
    n = 1000

    num = 2 ** n

    num_str = str(num)

    print(sum(int(x) for x in num_str))


# If for some reason we couldn't actually calculate 2**1000,
# we could have instead began with its binary representation:
# 1 << 1000. Then converted this representation to base 10.
# 2^6 = ((2^6 // 10)*10 + (2^6 % 10) = (0b1000000 // 0b1010)*10 + (0b1000000 % 0b1010)


if __name__ == '__main__':
    main()