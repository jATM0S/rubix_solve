import moves

# to test cube un comment rubiks_cube and uncomment the function at the end and change the names of condition
# rubiks_cube = {
#     'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
#     'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
#     'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
#     'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
#     'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
#     'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'   
# }
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

# piece in front tested    
def piece_on_front_top(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F2'] == rubiks_cube['F5']:
        sequence = ['f', 'f']
    else:
        sequence = ["u'", "r'", 'f', "r"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence
    
def piece_on_front_right(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F6'] == rubiks_cube['F5']:
        sequence = ['f']
    else:
        sequence = ['r','u','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 
    return sequence

def piece_on_front_left(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F4'] == rubiks_cube['F5']:
        sequence = ["f'"]
    else:
        sequence = ["l'","u'",'l','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 
    return sequence

def piece_on_front_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F4'] == rubiks_cube['F5']:
        sequence = []
    else:
        sequence = ['f',"l'","u'",'l','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube) 
    return sequence

# piece in right (have to test)
def piece_on_right_top(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R2'] == rubiks_cube['F5']:
        sequence = ['u','f', 'f']
    else:
        sequence = ["r'", 'f', "r"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence
        
def piece_on_right_right(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R6'] == rubiks_cube['F5']:
        sequence = ["r'",'u', 'f','f','r']
    else:
        sequence = ["r'", "r'", 'f','r','r']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence

def piece_on_right_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R8'] == rubiks_cube['F5']:
        sequence = ["d'",'f','d',"f'"]
    else:
        sequence = ["r", 'f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence

# piece in left (have to test)
def piece_on_left_top(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['L2'] == rubiks_cube['F5']:
        sequence = ["u'",'f', 'f']
    else:
        sequence = ['l', "f'", "l'"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence
        
def piece_on_left_left(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['L4'] == rubiks_cube['F5']:
        sequence = ['l',"u'", 'f','f',"l'"]
    else:
        sequence = ['l', 'l', "f'","l'","l'"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence

def piece_on_left_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['L8'] == rubiks_cube['F5']:
        sequence = ["d'",'f','d',"f'"]
    else:
        sequence = ["l'", "f'"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence

# piece in the back top (have to test)
def piece_on_back_top(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['B2'] == rubiks_cube['F5']:
        sequence = ['u','u','f', 'f']
    else:
        sequence = ['u',"r'", 'f', "r"]
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence

def piece_on_back_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R8'] == rubiks_cube['F5']:
        sequence = ["d'","d'",'f','d','d',"f'"]
    else:
        sequence = ["d'","r",'d','f']
    
    # Execute the sequence of moves and print the cube after each one
    for move in sequence:
        rubiks_cube = execute_move(rubiks_cube, move)
        moves.print_2d_cube(rubiks_cube)
    return sequence

# test moves by change the name in the function below
# print(piece_on_left_top(rubiks_cube))