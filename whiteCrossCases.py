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
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F2'] == 'G':
        sequence = ['f', 'f']
    else:
        sequence = ["u'", "r'", 'f', "r"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 
    
# if the green piece is in front right
def piece_on_front_right(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F6'] == 'G':
        sequence = ['f']
    else:
        sequence = ['r','u','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 

# if the green piece is in front left
def piece_on_front_left(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F4'] == 'G':
        sequence = ["f'"]
    else:
        sequence = ["l'","u'",'l','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 

# if the green piece in in front bottom
def piece_on_front_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F4'] == 'G':
        sequence = []
    else:
        sequence = ['f',"l'","u'",'l','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 
    
piece_on_front_top(rubiks_cube)

# moves.print_2d_cube(execute_move(rubiks_cube,"f"))
