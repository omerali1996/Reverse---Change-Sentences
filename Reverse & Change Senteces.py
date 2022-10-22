



#----------------------------------------------
def reverse(x):
    """

    Parameters
    This function reverses the given sentence first,
    converts the letters up or low as contrast.
    Parameters.
    x

    Returns
    Give a vocabulary, word ord sentence
    type x must be string.

    """
    new_x = x.replace(" ", "=")
    c = ""
    for harf in new_x:
        if harf.islower():
            c += (harf.upper())
        elif harf.isupper():
            c += (harf.lower())
        else:
            c += (harf.lower())
    f = c.split("=")
    y = f.reverse()
    p = ""
    for i in f:
        p += i + " "
    print(p)

reverse("uYGuN Ali ÖmEr")
