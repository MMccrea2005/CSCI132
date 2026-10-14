def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]

strVal = to_str(11,3)
print(f'{strVal} is of type {type(strVal)}')