def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # phrase = phrase.lower()
    # vowels = set('aeiou')
    # keys = vowels.intersection(phrase)
    # result = {}
    # for letter in keys:
    #     result[letter] = phrase.count(letter)
    # return result
    
    phrase = phrase.lower()
    vowels = set('aeiou')
    result = {}
    for letter in phrase:
        if letter in vowels:
            result[letter] = phrase.count(letter)
    return result
            
