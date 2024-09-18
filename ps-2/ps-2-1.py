import numpy as np
import math

def get_bits(number):
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    bytes = number.tobytes()
    bits = []
    for byte in bytes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))

def print_float32_bits(number):
    bitlist=get_bits(np.float32(number))
    sign = bitlist[0]
    exponent = bitlist[1:9]
    mantissa = bitlist[9:32]
    
    template_f = '''{number} decimal ->
        bitlist = {bitlist}
        sign = {sign} 
        exponent = {exponent} 
        mantissa = {mantissa}
        '''
    
    print(template_f.format(number=number, bitlist=bitlist, sign=sign, exponent=exponent, mantissa=mantissa))


def bits_to_number(bitlist):
    sign = bitlist[0]
    exponent = bitlist[1:9]
    mantissa = bitlist[9:32]
    
    s = math.pow(-1, sign)
    e = int(''.join(str(x) for x in exponent), 2)
    
    m_list = []
    for i in range(len(mantissa)):
        m_list.append(mantissa[i] * math.pow(2, -(i+1)))
    
    answer = s * (1 + np.sum(np.array(m_list))) * math.pow(2, e - 127)
    
    return answer


# tests

# template = "{number} decimal -> {bitlist}"

# number = np.int8(124)

# print(template.format(number = number, bitlist = get_bits(np.int8(number))))

# print_float32_bits(1.0)


# answers
number = 100.98763

print(rf"NumPy's 32-bit floating point representation of {number} is")
print_float32_bits(number)

print('This 32-bit representation in fact corresponds to')
print(bits_to_number(get_bits(np.float32(number))))

print('We can check that: 13236651/131072 = ', 13236651/131072, '\n')

print('The difference is')
print(np.float64(13236651/131072 - 100.98763))

