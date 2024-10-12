# solved state
# rubiks_cube = {
#     'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
#     'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
#     'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
#     'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
#     'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
#     'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}


# cubes to test for stages
# rubik_string = 'OROYROBYYGOBBGBGGWOYWWOOROORRGWBGYRRBBWWYGYBWYRRGWWBYG'
# rubiks_cube={'F1': 'O', 'F2': 'R', 'F3': 'O', 'F4': 'Y', 'F5': 'R', 'F6': 'O', 'F7': 'B', 'F8': 'Y', 'F9': 'Y', 'R1': 'G', 'R2': 'O', 'R3': 'B', 'R4': 'B', 'R5': 'G', 'R6': 'B', 'R7': 'G', 'R8': 'G', 'R9': 'W', 'B1': 'O', 'B2': 'Y', 'B3': 'W', 'B4': 'W', 'B5': 'O', 'B6': 'O', 'B7': 'R', 'B8': 'O', 'B9': 'O', 'L1': 'R', 'L2': 'R', 'L3': 'G', 'L4': 'W', 'L5': 'B', 'L6': 'G', 'L7': 'Y', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'W', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'Y', 'U8': 'B', 'U9': 'W', 'D1': 'Y', 'D2': 'R', 'D3': 'R', 'D4': 'G', 'D5': 'W', 'D6': 'W', 'D7': 'B', 'D8': 'Y', 'D9': 'G'}

# rubik_string = 'OYGROBBOORGYWWWYOYBWOGRGGROWYWOYGGRWBRRBBYGOWRBBYGWYBR'
# rubiks_cube={'F1': 'O', 'F2': 'Y', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'B', 'F7': 'B', 'F8': 'O', 'F9': 'O', 'R1': 'R', 'R2': 'G', 'R3': 'Y', 'R4': 'W', 'R5': 'W', 'R6': 'W', 'R7': 'Y', 'R8': 'O', 'R9': 'Y', 'B1': 'B', 'B2': 'W', 'B3': 'O', 'B4': 'G', 'B5': 'R', 'B6': 'G', 'B7': 'G', 'B8': 'R', 'B9': 'O', 'L1': 'W', 'L2': 'Y', 'L3': 'W', 'L4': 'O', 'L5': 'Y', 'L6': 'G', 'L7': 'G', 'L8': 'R', 'L9': 'W', 'U1': 'B', 'U2': 'R', 'U3': 'R', 'U4': 'B', 'U5': 'B', 'U6': 'Y', 'U7': 'G', 'U8': 'O', 'U9': 'W', 'D1': 'R', 'D2': 'B', 'D3': 'B', 'D4': 'Y', 'D5': 'G', 'D6': 'W', 'D7': 'Y', 'D8': 'B', 'D9': 'R'}

# rubik_string = 'OBGWYGBBWRRWYBGRGGYOGROGOYBBRWYWWYOYGORRGBOBWOWYORWRYB'
# rubiks_cube={'U1': 'O', 'U2': 'B', 'U3': 'G', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'B', 'U8': 'B', 'U9': 'W', 'R1': 'R', 'R2': 'R', 'R3': 'W', 'R4': 'Y', 'R5': 'B', 'R6': 'G', 'R7': 'R', 'R8': 'G', 'R9': 'G', 'F1': 'Y', 'F2': 'O', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'G', 'F7': 'O', 'F8': 'Y', 'F9': 'B', 'D1': 'B', 'D2': 'R', 'D3': 'W', 'D4': 'Y', 'D5': 'W', 'D6': 'W', 'D7': 'Y', 'D8': 'O', 'D9': 'Y', 'L1': 'G', 'L2': 'O', 'L3': 'R', 'L4': 'R', 'L5': 'G', 'L6': 'B', 'L7': 'O', 'L8': 'B', 'L9': 'W', 'B1': 'O', 'B2': 'W', 'B3': 'Y', 'B4': 'O', 'B5': 'R', 'B6': 'W', 'B7': 'R', 'B8': 'Y', 'B9': 'B'}



# cubes with whitecross
# whitecross string
# rubik_string='OOOBOWWORYYROWBYWWWOYRRYORWBWYRYWGYRRYGRBBBBGBGGGGGOGB'
# rubiks_cube={'F1': 'O', 'F2': 'O', 'F3': 'O', 'F4': 'B', 'F5': 'O', 'F6': 'W', 'F7': 'W', 'F8': 'O', 'F9': 'R', 'R1': 'Y', 'R2': 'Y', 'R3': 'R', 'R4': 'O', 'R5': 'W', 'R6': 'B', 'R7': 'Y', 'R8': 'W', 'R9': 'W', 'B1': 'W', 'B2': 'O', 'B3': 'Y', 'B4': 'R', 'B5': 'R', 'B6': 'Y', 'B7': 'O', 'B8': 'R', 'B9': 'W', 'L1': 'B', 'L2': 'W', 'L3': 'Y', 'L4': 'R', 'L5': 'Y', 'L6': 'W', 'L7': 'G', 'L8': 'Y', 'L9': 'R', 'U1': 'R', 'U2': 'Y', 'U3': 'G', 'U4': 'R', 'U5': 'B', 'U6': 'B', 'U7': 'B', 'U8': 'B', 'U9': 'G', 'D1': 'B', 'D2': 'G', 'D3': 'G', 'D4': 'G', 'D5': 'G', 'D6': 'G', 'D7': 'O', 'D8': 'G', 'D9': 'B'}

# rubik_string=("YYBGRYWRRRRYGGYWGBRBGOOOOOBRBOGBRWBOWYGOYBGRYGWBWWWOWY")
# rubiks_cube={'F1': 'Y', 'F2': 'Y', 'F3': 'B', 'F4': 'G', 'F5': 'R', 'F6': 'Y', 'F7': 'W', 'F8': 'R', 'F9': 'R', 'R1': 'R', 'R2': 'R', 'R3': 'Y', 'R4': 'G', 'R5': 'G', 'R6': 'Y', 'R7': 'W', 'R8': 'G', 'R9': 'B', 'B1': 'R', 'B2': 'B', 'B3': 'G', 'B4': 'O', 'B5': 'O', 'B6': 'O', 'B7': 'O', 'B8': 'O', 'B9': 'B', 'L1': 'R', 'L2': 'B', 'L3': 'O', 'L4': 'G', 'L5': 'B', 'L6': 'R', 'L7': 'W', 'L8': 'B', 'L9': 'O', 'U1': 'W', 'U2': 'Y', 'U3': 'G', 'U4': 'O', 'U5': 'Y', 'U6': 'B', 'U7': 'G', 'U8': 'R', 'U9': 'Y', 'D1': 'G', 'D2': 'W', 'D3': 'B', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'O', 'D8': 'W', 'D9': 'Y'}



# CUBES WITH YELLOR CROSS
rubik_string=("YROGGGGGGYBYOOOOOOROYBBBBBBOGRRRRRRRBYGYYYBYGWWWWWWWWW")
rubiks_cube={'F1': 'Y', 'F2': 'R', 'F3': 'O', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G', 'R1': 'Y', 'R2': 'B', 'R3': 'Y', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'B1': 'R', 'B2': 'O', 'B3': 'Y', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B', 'L1': 'O', 'L2': 'G', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'Y', 'U3': 'G', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'B', 'U8': 'Y', 'U9': 'G', 'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}