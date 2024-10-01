import moves
def string_to_rubiks_dict(cube_string):
    # Ensure the string has 54 characters (9 for each face)
    if len(cube_string) != 54:
        raise ValueError("The cube string must contain exactly 54 characters.")
    
    # Mapping from string positions to the cube dictionary
    # face_order = ['U', 'R', 'F', 'D', 'L', 'B']
    face_order = ['F','R','B','L','U','D']
    rubiks_map = {}
    
    for i, face in enumerate(face_order):
        start_idx = i * 9
        for j in range(9):
            rubiks_map[f'{face}{j+1}'] = cube_string[start_idx + j]
    
    return rubiks_map

# Example usage:
# rubik_string = 'OBGWYGBBWRRWYBGRGGYOGROGOYBBRWYWWYOYGORRGBOBWOWYORWRYB'
# rubik_string = 'OROYROBYYGOBBGBGGWOYWWOOROORRGWBGYRRBBWWYGYBWYRRGWWBYG'
rubik_string = 'OYGROBBOORGYWWWYOYBWOGRGGROWYWOYGGRWBRRBBYGOWRBBYGWYBR'

cube_dict = string_to_rubiks_dict(rubik_string)

print(cube_dict)
moves.print_2d_cube(cube_dict)


# cubes to test for stages
# rubiks_cube={'F1': 'O', 'F2': 'R', 'F3': 'O', 'F4': 'Y', 'F5': 'R', 'F6': 'O', 'F7': 'B', 'F8': 'Y', 'F9': 'Y', 'R1': 'G', 'R2': 'O', 'R3': 'B', 'R4': 'B', 'R5': 'G', 'R6': 'B', 'R7': 'G', 'R8': 'G', 'R9': 'W', 'B1': 'O', 'B2': 'Y', 'B3': 'W', 'B4': 'W', 'B5': 'O', 'B6': 'O', 'B7': 'R', 'B8': 'O', 'B9': 'O', 'L1': 'R', 'L2': 'R', 'L3': 'G', 'L4': 'W', 'L5': 'B', 'L6': 'G', 'L7': 'Y', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'W', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'Y', 'U8': 'B', 'U9': 'W', 'D1': 'Y', 'D2': 'R', 'D3': 'R', 'D4': 'G', 'D5': 'W', 'D6': 'W', 'D7': 'B', 'D8': 'Y', 'D9': 'G'}
# rubiks_cube={'F1': 'O', 'F2': 'Y', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'B', 'F7': 'B', 'F8': 'O', 'F9': 'O', 'R1': 'R', 'R2': 'G', 'R3': 'Y', 'R4': 'W', 'R5': 'W', 'R6': 'W', 'R7': 'Y', 'R8': 'O', 'R9': 'Y', 'B1': 'B', 'B2': 'W', 'B3': 'O', 'B4': 'G', 'B5': 'R', 'B6': 'G', 'B7': 'G', 'B8': 'R', 'B9': 'O', 'L1': 'W', 'L2': 'Y', 'L3': 'W', 'L4': 'O', 'L5': 'Y', 'L6': 'G', 'L7': 'G', 'L8': 'R', 'L9': 'W', 'U1': 'B', 'U2': 'R', 'U3': 'R', 'U4': 'B', 'U5': 'B', 'U6': 'Y', 'U7': 'G', 'U8': 'O', 'U9': 'W', 'D1': 'R', 'D2': 'B', 'D3': 'B', 'D4': 'Y', 'D5': 'G', 'D6': 'W', 'D7': 'Y', 'D8': 'B', 'D9': 'R'}
# rubiks_cube={'U1': 'O', 'U2': 'B', 'U3': 'G', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'B', 'U8': 'B', 'U9': 'W', 'R1': 'R', 'R2': 'R', 'R3': 'W', 'R4': 'Y', 'R5': 'B', 'R6': 'G', 'R7': 'R', 'R8': 'G', 'R9': 'G', 'F1': 'Y', 'F2': 'O', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'G', 'F7': 'O', 'F8': 'Y', 'F9': 'B', 'D1': 'B', 'D2': 'R', 'D3': 'W', 'D4': 'Y', 'D5': 'W', 'D6': 'W', 'D7': 'Y', 'D8': 'O', 'D9': 'Y', 'L1': 'G', 'L2': 'O', 'L3': 'R', 'L4': 'R', 'L5': 'G', 'L6': 'B', 'L7': 'O', 'L8': 'B', 'L9': 'W', 'B1': 'O', 'B2': 'W', 'B3': 'Y', 'B4': 'O', 'B5': 'R', 'B6': 'W', 'B7': 'R', 'B8': 'Y', 'B9': 'B'}