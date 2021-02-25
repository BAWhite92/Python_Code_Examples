#Given integers n, p1, and p2, determine if the bits of n 
#in position p1 and p2 are the same. Positions p1, p2 are 1 based with 1 being the least significant bit.

def bit_manip(n, p1, p2):
    #create "f" string of the number n, 08 is to format string to 8 digits and zero fill padded on left. (0000..)
    #b means to create the binary of n
    n_bits = f'{n:08b}'
    #turn new binary string representation into an int
    n_bits = int(n_bits)
    #find what the p1 and p2 positions of the biary number are and compare them
    p1_result = (n_bits >> (p1 - 1)) & 1
    #do P'n' - 1 as we want to see the actual value of P'n' in binary number n, if we moved by P'n' we would delete the P'n' value as the positions of p1 and p2 are 1 based here.
    p2_result = (n_bits >> (p2 - 1)) & 1
    test_same = p1_result == p2_result
    print("Bits of n in p1 and p2 being the same is", str(test_same).lower())

bit_manip(101, 2, 3)

#BIG NOTE!!! If this was a zero based position question you would do (n_bits >> p1) & 1 etc as when 0-based the left most (least significant) number is position 0 not position 1 as it is in 1-based.
