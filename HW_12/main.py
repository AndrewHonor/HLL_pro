def new_format(string):

    len_x = len(string)
    if len_x <= 3:
        return string
    pars_string = ""

    for i in range(len_x):
        if i > 0 and (len_x - i) % 3 == 0:
            pars_string +=  "."+string[i]
        else:
            pars_string += string[i]
    return pars_string



assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
