from .convert import bin_dec

def group_by8(bits):
    blocks = []
    tmp = []
    for x in bits:
        tmp.append(x)
        if len(tmp)>=8:
            blocks.append(tmp)
            tmp = []
    return blocks

def get_mask(prefix):
    my_prefix = int(prefix)
    #print("my_prefix", my_prefix)
    bits = []
    for b in range(my_prefix):
        bits.append('1')
    #print(bits)

    zeros = []
    for z in range(32-len(bits)):
        zeros.append('0')
    #print(zeros)

    octetos = bits + zeros
    #print(octetos)

    blocks = group_by8(octetos)
    #print(blocks)

    result = []
    for block in blocks:
        result.append(str(bin_dec(block)))
    return ".".join(result)

