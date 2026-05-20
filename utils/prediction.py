def status_kondisi(x):

    if x < 70:
        return "Aman"

    elif x <= 100:
        return "Rawan"

    else:
        return "Overload"