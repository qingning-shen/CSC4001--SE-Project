D bv8 v000
D bv32 v001
D bv64 v002
D bv16 v003
D bv32 v004
D bv16 v004
B 009 ( ( ( 0000000101101011 ) & ( v002 ) ) & ( ( v001 ) + ( 1101010110101100010001000100111000000111111101000101011101011010 ) ) )
B 012 ( ( ( v002 ) + ( v001 ) ) & ( ( 0001011100001000110000110111010100010011101010011000111011101110 ) + ( 0100111111001101100010001001111010101011011110001101001001001100 ) ) )
B 046 ( ( ! ( 01010001001101100001001100001010 ) ) & ( ( v003 ) | ( v001 ) ) )
R v000
D bv64 v001
D bv32 v001
A v002 ( ( ( 1101000000011111 ) | ( v004 ) ) + ( ( 0000110110010110111110110111100111100110011100000110100101110001 ) & ( 10100101000010001100011111001001 ) ) )
D bv32 v002
D bv32 v004
R v002
A v001 ( ( ( v002 ) + ( 1001011000001100010010011100010110100011011000100001001011111110 ) ) | ( ( 1100101010101010 ) & ( v000 ) ) )
B 021 ( ( ( 00000101 ) + ( 01010001110100010001111101000001 ) ) | ( ( 11011011 ) | ( 00101110 ) ) )
D bv64 v001
A v001 ( ( ( 10100001 ) & ( 0101001100100011 ) ) - ( ( 0011001101100000111111111110101101001111101000101110000000010101 ) | ( 1100100000100011011000101110101011000000101111010111001100010001 ) ) )
D bv8 v001
A v000 ( ( ! ( v004 ) ) | ( ( 01111111 ) + ( v001 ) ) )
R v002
D bv16 v004
B 034 ( ( ! ( 10101100 ) ) & ( ( v000 ) | ( v001 ) ) )
D bv8 v003
R v003
A v002 ( ( ( v002 ) | ( v004 ) ) + ( ( v003 ) | ( v000 ) ) )
B 032 ( ( ( v004 ) & ( 0001011111111100100000011011110000011101110011110100011000101010 ) ) + ( ! ( v001 ) ) )
B 048 ( ! ( ! ( v001 ) ) )
D bv8 v003
R v000
D bv8 v002
B 053 ( ( ! ( v001 ) ) + ( ( 1101011010001100100000010100101101000010100001000001010001010011 ) - ( 1001101111011111 ) ) )
D bv16 v003
D bv8 v002
B 047 ( ! ( ( v001 ) & ( v004 ) ) )
R v004
R v002
R v004
A v003 ( ( ( 01011101 ) & ( v002 ) ) & ( ( v003 ) | ( 0111010110010010 ) ) )
B 049 ( ( ( v003 ) | ( 1111001110101110 ) ) | ( ( 11001000 ) - ( v004 ) ) )
D bv16 v000
D bv64 v002
R v002
A v004 ( ! ( ( 11001010 ) - ( v001 ) ) )
D bv64 v001
R v003
R v001
R v004
A v001 ( ( ( v004 ) | ( 00000010 ) ) + ( ( v001 ) - ( v000 ) ) )
D bv16 v004
B 053 ( ( ( v004 ) | ( 1101001101100000111001010010000111110101001110001001000000101011 ) ) - ( ( 00001100100011100111111111010000 ) + ( v004 ) ) )
D bv32 v004
R v001
