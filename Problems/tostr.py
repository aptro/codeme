def tostr(n ,base):
    converttostr = "0123456789ABCDEF"
    if n < base:
        return converttostr[n]
    else:
        return tostr(n // base, base) + converttostr[n%base]
    