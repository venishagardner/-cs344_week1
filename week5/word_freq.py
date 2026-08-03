def count_words(text):
    text = text.lower()
    words = text.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def main():
    text = input("Enter a line or paragraph of text: ")

    counts = count_words(text)

    print("\nWord Frequency")

    for word in counts:
        print(word + ":", counts[word])


# Fixed word counting by converting text to lowercase first.
if __name__ == "__main__":
    main()
