def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    indexes = list()
    vowels = 'aeiou'
    for i in range(len(s)):
        if s[i].lower() in vowels:
            indexes.append(i)
    s_list = list(s)
    for i in range(len(indexes)):
        s_list[indexes[i]] = s[indexes[-1-i]]
        s_list[indexes[-1-i]] = s[indexes[i]]
    s = ''.join(s_list)
    return s

    