def analyze_text(text):
    characters = len(text)
    words = len(text.split())
    e_count = text.count("e")

    return characters, words, e_count


def main():
    text = input("Enter a line of text: ")

    characters, words, e_count = analyze_text(text)

    print("\nText Statistics")
    print("Characters:", characters)
    print("Words:", words)
    print("Lowercase e's:", e_count)


# Fixed empty text by using split(), which returns an empty list.
if __name__ == "__main__":
    main()
