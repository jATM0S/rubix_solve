import moves
import frequentSequences
# to test cube un comment rubiks_cube and uncomment the function at the end and change the names of condition
# rubiks_cube = {
#     'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
#     'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
#     'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
#     'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
#     'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
#     'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'   
# }

# piece in front tested    

def lefty_algorithm():
    return  ["l'","u'",'l',"u"]
def righty_algorithm():
    return  ['r','u',"r'","u'"]

# for left corner piece
def front_top_left(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['F1'] == rubiks_cube['D5']:
        sequence = ['f', 'u',"f'"]
    elif rubiks_cube['L3']==rubiks_cube['D5']:
        sequence = ["l'","u'",'l']
    else:
        for x in range(3):
            sequence.extend(frequentSequences.lefty_sequence())
    
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence

# def front_top_right(rubiks_cube):
#     sequence = []
    
#     # Decide on the sequence of moves based on the condition
#     if rubiks_cube['R1'] == rubiks_cube['D5']:
#         sequence = ['r', 'u',"r'"]
#     elif rubiks_cube['F3']==rubiks_cube['D5']:
#         sequence = ["f'","u'",'f']
#     else:
#         for x in range(3):
#             sequence.extend(righty_algorithm())
    
#     # Execute the sequence of moves and print the cube after each one
#     # for move in sequence:
#     #     rubiks_cube = moves.execute_move(rubiks_cube,move)
#     #     moves.print_2d_cube(rubiks_cube)
#     return sequence

def front_bottom_left(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['D1']==rubiks_cube['D5']:
        sequence=[]
    else:
        sequence.extend(["l'","u'",'l','u'])
        for move in sequence:
            rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
        sequence.extend(front_top_left(rubiks_cube_copy))
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
def front_top_right(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    
    # Decide on the sequence of moves based on the condition

    sequence.append('u')
    for move in sequence:
        rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
    sequence.extend(front_top_left(rubiks_cube_copy))    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
def front_bottom_right(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    
    # Decide on the sequence of moves based on the condition

    sequence.extend(['r','u',"r'"])
    for move in sequence:
        rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
    sequence.extend(front_top_left(rubiks_cube_copy))    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
def right_right_top(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    
    # Decide on the sequence of moves based on the condition

    sequence.extend(['u','u'])
    for move in sequence:
        rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
    sequence.extend(front_top_left(rubiks_cube_copy))
    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
def right_right_bottom(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    
    # Decide on the sequence of moves based on the condition

    sequence.extend(["b'","u'",'b'])
    for move in sequence:
        rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
    sequence.extend(front_top_left(rubiks_cube_copy))    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
def left_left_top(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    
    # Decide on the sequence of moves based on the condition

    sequence.append("u'")
    for move in sequence:
        rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
    sequence.extend(front_top_left(rubiks_cube_copy))    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence
def left_left_bottom(rubiks_cube):
    sequence = []
    rubiks_cube_copy=rubiks_cube.copy()
    
    # Decide on the sequence of moves based on the condition

    sequence.extend(["b'","u'",'b'])
    for move in sequence:
        rubiks_cube_copy=moves.execute_move(rubiks_cube_copy,move)
    sequence.extend(front_top_left(rubiks_cube_copy))    # Execute the sequence of moves and print the cube after each one
    # for move in sequence:
    #     rubiks_cube = moves.execute_move(rubiks_cube,move)
    #     moves.print_2d_cube(rubiks_cube)
    return sequence

# print(front_bottom_left(rubiks_cube))