def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    end_phrase = ''
    to_swap = to_swap.lower()
    def flip_case(letter):
        if letter.islower():
            return letter.upper()
        return letter.lower()    

    for l in phrase:
        if l.lower() == to_swap:
            l = flip_case(l)
        end_phrase += l
        
    return end_phrase