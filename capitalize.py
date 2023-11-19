def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    phrase = phrase[0].swapcase() + phrase[1:len(phrase)]

    # i = 0
    # while i < len(phrase):
    #     if phrase[i] == ' ':
    #         phrase = phrase[0:i+1] + phrase[i+1].swapcase() + phrase[i+2:len(phrase)]
    #     i += 1

    return phrase