def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    word_array = phrase.lower().split(' ')
    titles = []
    for word in word_array:
        titles.append(word.capitalize())
    return ' '.join(titles)