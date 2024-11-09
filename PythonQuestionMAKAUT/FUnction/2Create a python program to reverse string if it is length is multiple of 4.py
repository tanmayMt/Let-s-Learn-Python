def reverse_str(n):
    if len(n) == 4:
        return ''.join(reversed(n))
    else:
        return ("string length is multiple of 4")

print(reverse_str("Tanm"))
print(reverse_str("bgfhsdofgh")) 