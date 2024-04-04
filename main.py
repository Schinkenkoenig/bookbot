def get_words_counts(text: str):
    words = text.split()
    return len(words)


def count_letters(text: str):
    letters_count: dict[str, int] = {}
    for c in "".join([x.lower() for x in text.split()]):
        if not c.isalpha():
            continue
        if c not in letters_count:
            letters_count[c] = 1
        else:
            letters_count[c] += 1
    return letters_count


def read_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def letters_count_report(letters_dict: dict[str, int]):
    letters_dict_ary = [{"letter": k, "count": v} for (k, v) in letters_dict.items()]
    letters_dict_ary.sort(reverse=True, key=lambda x: x["count"])

    print("--- Begin report of books/frankenstein.txt ---")

    for d in letters_dict_ary:
        letter = d["letter"]
        count = d["count"]

        print(f"The '{letter}' character was found {count} times.")


def main():
    text = read_text("books/frankenstein.txt")
    count = get_words_counts(text)
    letters_count = count_letters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document.\n")
    letters_count_report(letters_count)
    print("--- End report ---")


main()
