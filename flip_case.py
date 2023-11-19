def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    i = 0

    while i < len(phrase)-1:
        if phrase[i].lower() == to_swap.lower():
            phrase = phrase[0:i] + phrase[i].swapcase() + phrase[i+1: len(phrase)]
        i+=1

    #check the last letter
    if phrase[len(phrase)-1].lower() == to_swap.lower():
        phrase = phrase[0:len(phrase)-1] + phrase[len(phrase)-1].swapcase()

    return phrase