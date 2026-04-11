import pytest
from string_utils import (
    count_vowels,
    reverse_string,
    is_palindrome,
    word_count,
    capitalise_words,
    remove_duplicates
)

# ---------------- VOWELS ----------------
def test_count_vowels_normal():
    assert count_vowels("Hello") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_none():
    with pytest.raises(TypeError):
        count_vowels(None)


# ---------------- REVERSE ----------------
def test_reverse_normal():
    assert reverse_string("abc") == "cba"

def test_reverse_single():
    assert reverse_string("a") == "a"

def test_reverse_none():
    with pytest.raises(TypeError):
        reverse_string(None)


# ---------------- PALINDROME ----------------
def test_palindrome_true():
    assert is_palindrome("racecar") is True

def test_palindrome_sentence():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False

def test_palindrome_none():
    with pytest.raises(TypeError):
        is_palindrome(None)


# ---------------- WORD COUNT ----------------
def test_word_count_normal():
    assert word_count("Hello World") == 2

def test_word_count_spaces():
    assert word_count("   ") == 0

def test_word_count_none():
    with pytest.raises(TypeError):
        word_count(None)


# ---------------- CAPITALISE ----------------
def test_capitalise_words():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_single():
    assert capitalise_words("python") == "Python"

def test_capitalise_none():
    with pytest.raises(TypeError):
        capitalise_words(None)


# ---------------- REMOVE DUPLICATES ----------------
def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_no_change():
    assert remove_duplicates("abc") == "abc"

def test_remove_duplicates_none():
    with pytest.raises(TypeError):
        remove_duplicates(None)