def first_repeat_char(word):
    seen = set()
    for character in word:
        if character not in seen:
            seen.add(character)
        else:
            return character
    return "_"
print(first_repeat_char('hih'))
    