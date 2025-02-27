def int_to_unsigned_bin(d:int) -> str:
    b = ''
    if d == 0:
        return '0'
    while d > 0:
        b += str(d % 2)
        d = d//2
    return b[::-1]

print(int_to_unsigned_bin(13))

def unsigned_bin_to_int(b:str) -> int:
    d = 0
    B = [i for i in b][::-1]
    for i in range (len(B)):
        d += int(B[i])*(2**i)
    return d

print(unsigned_bin_to_int('1101'))

def add_bin_to_bin(a: str, b: str) -> str:
    a, b = a[::-1], b[::-1]
    max_len = max(len(a), len(b))
    
    result = []
    carry = 0
    
    for i in range(max_len):
        bit_a = int(a[i]) if i < len(a) else 0
        bit_b = int(b[i]) if i < len(b) else 0
        
        bit_sum = bit_a + bit_b + carry
        result.append(str(bit_sum % 2))
        carry = bit_sum // 2
        
    if carry:
        result.append('1')

    return ''.join(result[::-1])

print(add_bin_to_bin('1101', '0110'))
