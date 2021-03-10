# TASK 1:
# Binary - > Int:
# 1) 2
# 2) 45
# 3) 9
# 4) 110
# Int -> Binary:
# 1) 101
# 2) 1100
# 3) 100101


# TASK 2:
def BinaryToInt(B):
    # First reverse the string
    B = B[::-1]
    Int = 0
    # Iterate through the reversed binary number adding up the correspodning powers of 2
    n = len(B)
    for i in range(n):
        Bit = int(B[i])
        Int += Bit * (2**i) # note that ** means to the power of
    return Int


# TASK 3:
def IntToBinary(N):
    Run = True
    # Divide by 2 until you reach one and save the remainders
    Remainders = ''
    while Run:
        Remainders += str(N%2)
        N = N // 2
        if (N == 0):
            Run = False
    # Reverse the remainders
    B = Remainders[::-1]
    return B


# TASK 4:
def IntToByte(N):
    BinaryN = IntToBinary(N)
    Zeros = ''
    Remainder = len(BinaryN) % 8
    Gap = 8 - Remainder
    for i in range( 8-len(BinaryN) ):
        Zeros += '0'
    Byte = Zeros + BinaryN
    return Byte


def StringToBytes(String):
    Output = []
    for Letter in String:
        ASCII = ord(Letter)
        B = IntToByte(ASCII)
        #B = '0b' + B
        Output.append(B)
    return Output

def BytesToString(Bytes):
    Output = ''
    for Byte in Bytes:
        ASCII = BinaryToInt(Byte)
        Letter = chr(ASCII)
        Output += Letter
    return Output


# TASK 5:
def UTFDecoder(BitStream):
    n = len(BitStream)
    if n%8 != 0:
        print("Error: Input is not in byte form (length is not a multiple of 8).")

    # Splitting the string into bytes
    Bytes = []
    Index = 0
    while Index < n:
        Byte = BitStream[Index : Index+8]
        Bytes.append(Byte)
        Index += 8


    # Splitting the bytes into characters and removing the prefixes
    Characters = []
    CharStartIndex = 0
    while CharStartIndex < len(Bytes):
        FirstByte = Bytes[CharStartIndex]
        # Find the first 0
        Index = FirstByte.find('0')
        if Index == 0:
            Character = [FirstByte]
            CharStartIndex += 1
        else:
            Character = Bytes[CharStartIndex : CharStartIndex + Index]
            CharStartIndex += Index
        Characters.append(Character)

    # Removing the prefixes
    for i in range(len(Characters)):
        Character = Characters[i]
        for j in range(len(Character)):
            Byte = Character[j]
            # Remove up to and including the first 0
            Index = Byte.find('0')
            # Update in the Characters list
            Characters[i][j] = Byte[Index+1:None]


    # Turning each character into one binary number (instead of list of bytes)
    Encodings = []
    for Char in Characters:
        Binary = ''.join(Char)
        Encodings.append(Binary)



    # Turning binary into symbols
    Message = ''
    for Binary in Encodings:
        X = BinaryToInt(Binary)
        Letter = chr(X)
        Message += Letter


    return Message

print()
Message1 = ['01010100', '01101000', '01100101', '01110010', '01100101', '00100000', '01100001', '01110010', '01100101', '00100000', '01101111', '01101110', '01101100', '01111001', '00100000', '00110001', '00110000', '00100000', '01110100', '01111001', '01110000', '01100101', '01110011', '00100000', '01101111', '01100110', '00100000', '01110000', '01100101', '01101111', '01110000', '01101100', '01100101', '00100000', '01101001', '01101110', '00100000', '01110100', '01101000', '01100101', '00100000', '01110111', '01101111', '01110010', '01101100', '01100100', '00111010', '00100000', '01110100', '01101000', '01101111', '01110011', '01100101', '00100000', '01110111', '01101000', '01101111', '00100000', '01110101', '01101110', '01100100', '01100101', '01110010', '01110011', '01110100', '01100001', '01101110', '01100100', '00100000', '01100010', '01101001', '01101110', '01100001', '01110010', '01111001', '00100000', '01100001', '01101110', '01100100', '00100000', '01110100', '01101000', '01101111', '01110011', '01100101', '00100000', '01110111', '01101000', '01101111', '00100000', '01100100', '01101111', '01101110', '00100111', '01110100', '00101110']
print( BytesToString(Message1) )
print()

Message2 = '1110101010001101100111111100001110110001110010011000100111000011101101101110000110111010100011110010000011101111101111111010010111001110100110001100111010110000111100001001110110010110100101110010000011100101101100001011101011001110101101011110000110010111101010011100010010010001110011111000101011110000100111011001011010010011111000101000010010001010001000001110000010111000100111111110001010000100101011101101100010111001110100101010000100100001'
print( UTFDecoder(Message2) )
print()