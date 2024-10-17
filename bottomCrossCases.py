import moves

# piece in front tested    
def piece_on_front_top(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F2'] == rubiks_cube['F5']:
        sequence = ['f', 'f']
    else:
        sequence = ["u'", "r'", 'f', "r"]
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
    
def piece_on_front_right(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F6'] == rubiks_cube['F5']:
        sequence = ['f']
    else:
        sequence = ['r','u',"r'",'f','f']
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube, move)
    #     moves.print_2d_cube(rubiks_cube) 
    return sequence

def piece_on_front_left(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F4'] == rubiks_cube['F5']:
        sequence = ["f'"]
    else:
        sequence = ["l'","u'",'l','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube, move)
    #     moves.print_2d_cube(rubiks_cube) 
    return sequence

def piece_on_front_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F8'] == rubiks_cube['F5']:
        sequence = []
    else:
        sequence = ['f',"l'","u'",'l','f','f']
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube, move)
    #     moves.print_2d_cube(rubiks_cube) 
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
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
        
def piece_on_right_right(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R6'] == rubiks_cube['F5']:
        sequence = ["r'",'u', 'f','f','r']
    else:
        sequence = ["r'", "r'", 'f','r','r']
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence

def piece_on_right_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R8'] == rubiks_cube['F5']:
        sequence = ["d'",'f','d',"f'"]
    else:
        sequence = ["r", 'f']
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
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
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
        
def piece_on_left_left(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['L4'] == rubiks_cube['F5']:
        sequence = ['l',"u'", 'f','f',"l'"]
    else:
        sequence = ['l', 'l', "f'","l'","l'"]
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence

def piece_on_left_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['L8'] == rubiks_cube['F5']:
        sequence = ["d'",'f','d',"f'"]
    else:
        sequence = ["l'", "f'"]
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
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
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence

def piece_on_back_bottom(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['R8'] == rubiks_cube['F5']:
        sequence = ["d'","d'",'f','d','d',"f'"]
    else:
        sequence = ["d'","r",'d','f']
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence

# test moves by change the name in the function below
# print(piece_on_left_top(rubiks_cube))