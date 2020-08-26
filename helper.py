def parse_numbers(num):
    if isinstance(num[-1], int):
        number = num
        pass
    else:
        if (num[-1].lower() == "k"):
            multiplier = 1000
            number = float(num[:-1])
            number *= multiplier
        elif (num[-1].lower() == "m"):
            multiplier = 1000000
            number = float(num[:-1])
            number *= multiplier
        elif (num[-1].lower() == "b"):
            multiplier = 1000000000
            number = float(num[:-1])
            number *= multiplier
        else:
            number = num

    try:
        output = int(number.replace(',', ''))
    except AttributeError:
        output = int(number)
    return output

# print(parse_numbers("2.7M"))
# print(parse_numbers("26,285,258"))
# print(parse_numbers("2.22K"))
