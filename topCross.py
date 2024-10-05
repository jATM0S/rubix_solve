import moves
rubiks_cube={'F1': 'O', 'F2': 'Y', 'F3': 'R', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G', 'R1': 'Y', 'R2': 'O', 'R3': 'Y', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'B1': 'O', 'B2': 'Y', 'B3': 'R', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B', 'L1': 'G', 'L2': 'G', 'L3': 'G', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'U1': 'Y', 'U2': 'R', 'U3': 'B', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'B', 'U9': 'B', 'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
def dectect_topCross_pieces(rubiks_cube):
    sequence=[]
    solved=False
    count=0
    # top_side_pieces=[['F2','U8'],['U4','L2'],['U6','R2'],['U2','B2']]
    if all(rubiks_cube[pos] == rubiks_cube['U5'] for pos in ['U2', 'U4', 'U6','u8']):
        ++count
    if count>=2:
        if all(rubiks_cube[pos]==rubiks_cube['U5'] for pos in ['U2','U8']):
            print('smothing')
    return sequence

def top_cross(rubiks_cube):
    sequence=[]

    return sequence

# print(top_cross(rubiks_cube))