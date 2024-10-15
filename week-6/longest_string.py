def longest(strings):
    longest_str = strings[0]

    for string in strings:
        longest_str = string if len(string) > len(longest_str) else longest_str

    return longest_str


strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
print(longest(strings))
