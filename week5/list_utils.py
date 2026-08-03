def filter_and_summarize(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)

    count = len(positive_numbers)
    total = sum(positive_numbers)

    if count > 0:
        average = total / count
    else:
        average = 0

    return positive_numbers, count, total, average


def main():
    numbers = [10, -5, 0, 7, -2, 15, 3]

    positive_numbers, count, total, average = filter_and_summarize(numbers)

    print("Original list:", numbers)
    print("Positive numbers:", positive_numbers)
    print("Count:", count)
    print("Sum:", total)
    print("Average:", average)


# Fixed division by zero when there are no positive numbers.
if __name__ == "__main__":
    main()
