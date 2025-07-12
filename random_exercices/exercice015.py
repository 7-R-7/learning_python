import string 
import random

def make_serial(count):

    all_chars = string.ascii_letters + string.digits

    chars_count = len(all_chars)

    serial_list = []

    while count > 0:

        random_number = random.randint(0, chars_count - 1)

        random_character = all_chars[random_number]

        serial_list.append(random_character)

        count -= 1

    print("".join(serial_list))

make_serial(40)
