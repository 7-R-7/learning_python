def convert(n):
    st = str(n)

    rev_list = []

    for num in st :

        rev_list.append(int(num))
    
    rev_list.reverse()
    return rev_list

print("123456789 =>",convert(123456789))
print("54678234 =>",convert(54678234))
