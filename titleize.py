def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase = phrase.lower()
    phrase = phrase[0].swapcase() + phrase[1:len(phrase)]

    i = 0
    while i < len(phrase):
        if phrase[i] == ' ':
            phrase = phrase[0:i+1] + phrase[i+1].swapcase() + phrase[i+2:len(phrase)]
        i += 1

    return phrase