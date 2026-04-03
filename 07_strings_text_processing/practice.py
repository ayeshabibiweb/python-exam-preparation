# 07 – Strings & Text Processing: Practice Problems
# Each problem states the task as a comment, followed by the full solution.
# Run this file: python practice.py

import re
import string

print("=" * 60)
print("PROBLEM 1: Caesar Cipher")
print("=" * 60)
# Write a function caesar_cipher(text, shift) that implements a
# Caesar cipher: shift each letter by 'shift' positions in the
# alphabet (wrapping around). Non-letter characters remain unchanged.
# Write a corresponding decrypt(text, shift) function.
# Example: caesar_cipher("Hello, World!", 3) → "Khoor, Zruog!"

def caesar_cipher(text, shift):
    result = []
    shift = shift % 26
    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return "".join(result)

def caesar_decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

original  = "Hello, World! The quick brown fox."
encrypted = caesar_cipher(original, 13)   # ROT-13
decrypted = caesar_decrypt(encrypted, 13)

print(f"  Original  : {original}")
print(f"  ROT-13    : {encrypted}")
print(f"  Decrypted : {decrypted}")
print(f"  Match     : {original == decrypted}")


print("\n" + "=" * 60)
print("PROBLEM 2: Word Statistics")
print("=" * 60)
# Write a function word_stats(text) that returns a dict with:
#   "word_count"    — total number of words
#   "unique_words"  — number of unique words (case-insensitive)
#   "avg_length"    — average word length (float, 2 dp)
#   "longest"       — the longest word (first if tie)
#   "most_common"   — the most frequent word (case-insensitive, first if tie)
# Words are sequences of alphabetic characters; strip punctuation.

def word_stats(text):
    translator = str.maketrans("", "", string.punctuation)
    words = text.lower().translate(translator).split()
    if not words:
        return {}

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    return {
        "word_count":   len(words),
        "unique_words": len(freq),
        "avg_length":   round(sum(len(w) for w in words) / len(words), 2),
        "longest":      max(words, key=len),
        "most_common":  max(freq, key=freq.get),
    }

sample = (
    "To be or not to be, that is the question. "
    "Whether 'tis nobler in the mind to suffer the "
    "slings and arrows of outrageous fortune."
)
stats = word_stats(sample)
for key, val in stats.items():
    print(f"  {key:<15}: {val}")


print("\n" + "=" * 60)
print("PROBLEM 3: Title Case Without .title()")
print("=" * 60)
# Write a function smart_title(text) that converts a string to
# title case, but keeps common short words (a, an, the, and, but,
# or, for, nor, on, at, to, by, in, of, up) in lowercase UNLESS
# they are the first or last word.
# Example: "the lord of the rings" → "The Lord of the Rings"

LOWERCASE_WORDS = {
    "a", "an", "the", "and", "but", "or", "for",
    "nor", "on", "at", "to", "by", "in", "of", "up",
}

def smart_title(text):
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in LOWERCASE_WORDS:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)

titles = [
    "the lord of the rings",
    "a tale of two cities",
    "gone with the wind",
    "of mice and men",
    "to kill a mockingbird",
]
for t in titles:
    print(f"  {t!r:38} → {smart_title(t)!r}")


print("\n" + "=" * 60)
print("PROBLEM 4: Email Validator")
print("=" * 60)
# Write a function is_valid_email(email) that returns True if the
# string is a plausible email address. Rules:
# - Contains exactly one @
# - Local part (before @) has at least 1 character: letters, digits, ._+-
# - Domain part contains at least one dot
# - TLD (after last dot) is 2-6 characters, letters only
# Use a regex pattern.

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,6}$"
    return bool(re.match(pattern, email))

test_emails = [
    ("alice@example.com",       True),
    ("user.name+tag@sub.co.uk", True),
    ("no-at-sign.com",          False),
    ("@missinglocal.com",       False),
    ("spaces here@test.com",    False),
    ("user@",                   False),
    ("a@b.c",                   True),
    ("bad@domain.toolongtld",   False),
]
all_pass = True
for email, expected in test_emails:
    result = is_valid_email(email)
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_pass = False
    print(f"  {status} {email!r:<35} expected={expected}, got={result}")
print(f"  All tests passed: {all_pass}")


print("\n" + "=" * 60)
print("PROBLEM 5: Run-Length Encoding")
print("=" * 60)
# Run-Length Encoding (RLE) compresses consecutive repeated characters.
# Write encode_rle(s) → compressed string, e.g. "AAABBC" → "3A2B1C"
# Write decode_rle(s) → original string, e.g. "3A2B1C" → "AAABBC"
# Handle single characters correctly: "A" → "1A", not "A".

def encode_rle(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i-1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)

def decode_rle(s):
    pattern = re.compile(r"(\d+)([A-Za-z])")
    return "".join(int(n) * ch for n, ch in pattern.findall(s))

test_cases = [
    "AAABBBCCDDDDDE",
    "ABCDE",
    "AAAAAA",
    "A",
    "",
]
for original in test_cases:
    encoded = encode_rle(original)
    decoded = decode_rle(encoded)
    ok = "✓" if decoded == original else "✗"
    print(f"  {ok} {original!r:20} → encode: {encoded!r:15} → decode: {decoded!r}")


print("\n" + "=" * 60)
print("PROBLEM 6: Anagram Detector")
print("=" * 60)
# Write a function are_anagrams(s1, s2) that returns True if s1 and s2
# are anagrams of each other (same letters, possibly different order,
# ignoring case and spaces).
# Then write group_anagrams(words) that groups a list of words into
# sublists of anagrams, returning a list of groups.

def are_anagrams(s1, s2):
    normalize = lambda s: sorted(s.lower().replace(" ", ""))
    return normalize(s1) == normalize(s2)

def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return [g for g in groups.values() if len(g) > 1]

pairs = [("listen", "silent"), ("hello", "world"),
         ("astronomer", "moon starer"), ("abc", "cba")]
for a, b in pairs:
    print(f"  are_anagrams({a!r}, {b!r}) = {are_anagrams(a, b)}")

word_list = ["eat", "tea", "tan", "ate", "nat", "bat", "star", "rats", "arts"]
groups = group_anagrams(word_list)
print(f"\n  Anagram groups:")
for g in sorted(groups, key=len, reverse=True):
    print(f"    {g}")


print("\n" + "=" * 60)
print("PROBLEM 7: Extract Structured Data with Regex")
print("=" * 60)
# Given a block of text containing product entries in the format:
#   Product: <name> | Price: $<price> | Stock: <qty>
# Write extract_products(text) that returns a list of dicts with
# keys "name", "price" (float), "stock" (int).
# Then print products priced below $50 sorted by price.

def extract_products(text):
    pattern = re.compile(
        r"Product:\s*(?P<name>[^|]+?)\s*\|\s*"
        r"Price:\s*\$(?P<price>[\d.]+)\s*\|\s*"
        r"Stock:\s*(?P<stock>\d+)"
    )
    products = []
    for m in pattern.finditer(text):
        products.append({
            "name":  m.group("name").strip(),
            "price": float(m.group("price")),
            "stock": int(m.group("stock")),
        })
    return products

catalogue = """
Product: USB Cable | Price: $9.99 | Stock: 150
Product: Mechanical Keyboard | Price: $89.00 | Stock: 30
Product: Mouse Pad | Price: $14.99 | Stock: 200
Product: Monitor Stand | Price: $45.00 | Stock: 45
Product: Webcam HD | Price: $59.99 | Stock: 20
Product: HDMI Adapter | Price: $12.50 | Stock: 80
"""

products = extract_products(catalogue)
affordable = sorted(
    (p for p in products if p["price"] < 50),
    key=lambda p: p["price"]
)

print(f"  Total products found: {len(products)}")
print(f"  Products under $50 (sorted by price):")
for p in affordable:
    print(f"    {p['name']:<22} ${p['price']:>6.2f}  (stock: {p['stock']})")


print("\n" + "=" * 60)
print("PROBLEM 8: String Compression Statistics")
print("=" * 60)
# Write a function analyse_text(text) that returns a dict with:
#   "chars"        — total characters (including spaces)
#   "letters"      — only alphabetic characters
#   "digits"       — only digit characters
#   "spaces"       — space and tab characters
#   "punctuation"  — punctuation characters
#   "lines"        — number of lines
#   "sentences"    — number of sentences (end with . ! ?)

def analyse_text(text):
    return {
        "chars":       len(text),
        "letters":     sum(1 for c in text if c.isalpha()),
        "digits":      sum(1 for c in text if c.isdigit()),
        "spaces":      sum(1 for c in text if c in " \t"),
        "punctuation": sum(1 for c in text if c in string.punctuation),
        "lines":       text.count("\n") + 1,
        "sentences":   len(re.findall(r"[.!?]+", text)),
    }

sample_text = """Python is a high-level, general-purpose programming language.
Its design philosophy emphasises code readability.
Python 3.8 added the walrus operator (:=) and positional-only parameters!
Did you know Python is used in science, web development, and AI?"""

stats = analyse_text(sample_text)
print(f"  Analysis of sample text ({stats['lines']} lines):")
for key, val in stats.items():
    print(f"    {key:<14}: {val}")
