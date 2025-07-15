def format_num (num):

    formated_num = f"{num:,}"

    if len(formated_num) > 3 :

        to_list = formated_num.split(",")

        first = to_list[:-1]

        first_join = "".join(first)

        first_int = int(first_join)

        first_format = f"{first_int:,}"

        final_result = f"{first_format}_{to_list[-1]}"

        return final_result

    return formated_num

print(format_num(100))

print(format_num(1780))

print(format_num(120678950))

print(format_num(510656780910))

print(format_num(120453765014032))


