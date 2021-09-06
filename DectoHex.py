# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# The following are examples of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    r = max(0, r)
    r = min(255, r)
    r = "{0:02x}".format(r).upper()

    g = max(0, g)
    g = min(255, g)
    g = "{0:02x}".format(g).upper()

    b = max(0, b)
    b = min(255, b)
    b = "{0:02x}".format(b).upper()
    print(r+g+b)


rgb(275, 255, 255)



# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))