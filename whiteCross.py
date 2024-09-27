import moves
rubiks_cube = {
    'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
    'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
    'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
    'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
    'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
    'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'   
}
def execute_move(rubiks_cube,move):
    if move == "f":
        return moves.F(rubiks_cube)
    elif move == "f'":
        return moves.F_inv(rubiks_cube) 
    elif move == "r":
        return moves.R(rubiks_cube) 
    elif move == "r'":
        return moves.R_inv(rubiks_cube) 
    elif move == "l":
        return moves.L(rubiks_cube) 
    elif move == "l'":
        return moves.L_inv(rubiks_cube) 
    elif move == "u":
        return moves.U(rubiks_cube) 
    elif move == "u'":
        return  moves.U_inv(rubiks_cube) 
    elif move == "d":
        return moves.D(rubiks_cube) 
    elif move == "d'":
        return moves.D_inv(rubiks_cube) 
    elif move == "b":
        return moves.B(rubiks_cube) 
    elif move == "b'":
        return moves.B_inv(rubiks_cube) 
    elif move == "rr":
        return moves.rotateRight(rubiks_cube) 
    elif move == "rl":
        return moves.rotateLeft(rubiks_cube) 
    elif move == "ru":
        return moves.rotateUp(rubiks_cube) 
    elif move == "rd":
        return moves.rotateDown(rubiks_cube) 
    
# if the green white piece is in right side
def piece_on_front_top(rubiks_cube):
    sequence=[]
    if rubiks_cube['F2']=='G':
        sequence=['f','f','f','f']
    else:
        sequence=['t','r','f',"r'"]
    for x in sequence:
        rubiks_cube=execute_move(rubiks_cube,x)
        moves.print_2d_cube(rubiks_cube)
    

# to dectect the white piece
def dectect_white_side_pieces(rubiks_cube):
    # search_positions=['F2','F4','F6','F8','R2', 'R4', 'R6', 'R8','L2', 'L4', 'L6', 'L8','D2', 'D4', 'D6', 'D8','B2', 'B4', 'B6', 'B8']
    side_pieces=[['F2','U8'],['F4','L6'],['F6','R4'],['F8','D2'],['U2','B2'],['U3','L2'],['U6','R2'],['B4','R6'],['B6','L4'],['B8','D8'],['R8','D6'],['L8','D4']]
    white_piece_positions=[]
    for pair in side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == 'W':  # Check if the position has a white piece
                white_piece_positions.append(pair)
                
    # for detecting green white piece
    for pair in white_piece_positions:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == 'G': 
                green_piece_position=pair
    return green_piece_position
# print(dectect_white_green_piece(rubiks_cube))

piece_on_front_top(rubiks_cube)

# def whiteCross(rubiks_cube):
#     new_cube=rubiks_cube.copy()
#     # dectect white green piece position
    

#     # cases and moves for each situation
#     # condition of white cross completion
#     return new_cube