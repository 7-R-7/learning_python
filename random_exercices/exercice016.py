import string

a = "abcDegHi" # Missing 'f'

b = "dEFgi" # Missing 'h'

c = "xYz" # No Missing

def find_letter(letter):

    alpha = string.ascii_lowercase

    start = alpha.index(letter[0])

    for N in alpha[start:]:

        if N not in letter:

            return N

    return f"No Missing Letter"

print(find_letter(a.lower()))
print(find_letter(b.lower()))
print(find_letter(c.lower()))
