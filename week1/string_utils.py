def count_vowels(text: str) -> int:
    if text is None:
        raise TypeError("Input cannot be None")
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_string(text: str) -> str:
    if text is None:
        raise TypeError("Input cannot be None")
    return text[::-1]


def is_palindrome(text: str) -> bool:
    if text is None:
        raise TypeError("Input cannot be None")
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> int:
    if text is None:
        raise TypeError("Input cannot be None")
    return len(text.split())


def capitalise_words(text: str) -> str:
    if text is None:
        raise TypeError("Input cannot be None")
    return " ".join(word.capitalize() for word in text.split())


def remove_duplicates(text: str) -> str:
    if text is None:
        raise TypeError("Input cannot be None")

    result = []
    prev = None
    for char in text:
        if char != prev:
            result.append(char)
            prev = char
    return "".join(result)