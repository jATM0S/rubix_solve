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

rubik_string=("YROGGGGGGYBYOOOOOOROYBBBBBBOGRRRRRRRBYGYYYBYGWWWWWWWWW")

cube_dict = string_to_rubiks_dict(rubik_string)

print(cube_dict)
moves.print_2d_cube(cube_dict)




