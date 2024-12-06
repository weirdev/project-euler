ONE_TO_NINE = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEN_TO_NINETEEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
]
TENS_TWENTY_TO_NINETY = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"
THOUSAND = "thousand"


def number_to_words(n) -> str:
    if n == 1000:
        return f"{ONE_TO_NINE[0]} {THOUSAND}"

    result = ""
    if n >= 100:
        result += f"{ONE_TO_NINE[n // 100 - 1]} {HUNDRED}"
        if n % 100 == 0:
            return result
        n %= 100
        result += " and "

    if n >= 20:
        result += TENS_TWENTY_TO_NINETY[n // 10 - 2]
        if n % 10 == 0:
            return result
        n %= 10
        result += "-"
    elif n >= 10:
        return result + TEN_TO_NINETEEN[n - 10]

    return result + ONE_TO_NINE[n - 1]


def main():
    print(
        sum(
            len(number_to_words(i).replace(" ", "").replace("-", ""))
            for i in range(1, 1001)
        )
    )


if __name__ == "__main__":
    main()
