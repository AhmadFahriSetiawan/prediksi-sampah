import folium


def warna_marker(status):

    if "Aman" in status:
        return "green"

    elif "Rawan" in status:
        return "orange"

    else:
        return "red"