import secondLayerCases
import moves
# rubiks_cube = {
#     'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
#     'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
#     'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
#     'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
#     'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
#     'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
# rubiks_cube={'U1': 'O', 'U2': 'B', 'U3': 'G', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'B', 'U8': 'B', 'U9': 'W', 'R1': 'R', 'R2': 'R', 'R3': 'W', 'R4': 'Y', 'R5': 'B', 'R6': 'G', 'R7': 'R', 'R8': 'G', 'R9': 'G', 'F1': 'Y', 'F2': 'O', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'G', 'F7': 'O', 'F8': 'Y', 'F9': 'B', 'D1': 'B', 'D2': 'R', 'D3': 'W', 'D4': 'Y', 'D5': 'W', 'D6': 'W', 'D7': 'Y', 'D8': 'O', 'D9': 'Y', 'L1': 'G', 'L2': 'O', 'L3': 'R', 'L4': 'R', 'L5': 'G', 'L6': 'B', 'L7': 'O', 'L8': 'B', 'L9': 'W', 'B1': 'O', 'B2': 'W', 'B3': 'Y', 'B4': 'O', 'B5': 'R', 'B6': 'W', 'B7': 'R', 'B8': 'Y', 'B9': 'B'}
rubiks_cube={'F1': 'O', 'F2': 'Y', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'B', 'F7': 'B', 'F8': 'O', 'F9': 'O', 'R1': 'R', 'R2': 'G', 'R3': 'Y', 'R4': 'W', 'R5': 'W', 'R6': 'W', 'R7': 'Y', 'R8': 'O', 'R9': 'Y', 'B1': 'B', 'B2': 'W', 'B3': 'O', 'B4': 'G', 'B5': 'R', 'B6': 'G', 'B7': 'G', 'B8': 'R', 'B9': 'O', 'L1': 'W', 'L2': 'Y', 'L3': 'W', 'L4': 'O', 'L5': 'Y', 'L6': 'G', 'L7': 'G', 'L8': 'R', 'L9': 'W', 'U1': 'B', 'U2': 'R', 'U3': 'R', 'U4': 'B', 'U5': 'B', 'U6': 'Y', 'U7': 'G', 'U8': 'O', 'U9': 'W', 'D1': 'R', 'D2': 'B', 'D3': 'B', 'D4': 'Y', 'D5': 'G', 'D6': 'W', 'D7': 'Y', 'D8': 'B', 'D9': 'R'}

def bring_piece_to_top(rubiks_cube,unsolved_piece):
    if(unsolved_piece==['F4','L6']):
        return secondLayerCases.piece_on_frontLeft(rubiks_cube)
    elif(unsolved_piece==['F6','R4']):
        return secondLayerCases.piece_on_frontRight(rubiks_cube)
    elif(unsolved_piece==['B4','R6']):
        return secondLayerCases.piece_on_rightRight(rubiks_cube)
    elif(unsolved_piece==['B6','L4']):
        return secondLayerCases.piece_on_leftLeft(rubiks_cube)
    
    
# to dectect the white piece
# def dectect_required_side_pieces(rubiks_cube,side_pieces):
#     required_side_pieces=[]
#     required_piece=[]

#     for pair in side_pieces:
#         for position in pair:  # Iterate over each position in the current pair
#             if rubiks_cube[position] == rubiks_cube['F5']:  # Check if the position has a white piece
#                 required_side_pieces.append(pair)
    
#     for pair in required_side_pieces:
#         for position in pair:  # Iterate over each position in the current pair
#             if rubiks_cube[position] == rubiks_cube['R5']:  # Check if the position has a white piece
#                 required_piece=pair    

#     return required_piece

def dectect_top_pieces(rubiks_cube):
    pieces_on_top=[['F2','U8'],['U2','B2'],['U4','L2'],['U6','R2']]
    unrequired_pieces=[]
    required_top_pieces=[]
    if pieces_on_top:
        for pair in pieces_on_top:
            for position in pair:  # Iterate over each position in the current pair
                if rubiks_cube[position] == rubiks_cube['D5'] or rubiks_cube[position]==rubiks_cube['U5']:  # Check if the position has a white piece
                    unrequired_pieces.append(pair)
                    break

    required_top_pieces = [item for item in pieces_on_top if item not in unrequired_pieces]
    return required_top_pieces

def move_for_required_face(rubiks_cube,top_pieces):
    sequence=[]
    face_move=[]
    top_move=[]
    # find the color of a top piece
    for position in top_pieces[0]:  # Iterate over each position in the current pair
        if position in {'F2', 'R2' ,'L2','B2'} :
            color=rubiks_cube[position]
            piece_position=position
    # move to the color of the top face color    
    if rubiks_cube['R5']==color:
        face_move=['rl']
    elif rubiks_cube['L5']==color:
        face_move=['rr']
    elif rubiks_cube['B5']==color:
        face_move=['rl','rl']
    for move in face_move:
        rubiks_cube=moves.execute_move(rubiks_cube,move)

    # move the top piece until it matches the front
    while rubiks_cube['F2']!=rubiks_cube['F5']:
        rubiks_cube=moves.execute_move(rubiks_cube,'u')
        top_move.append('u')
    if top_move==['u','u','u']:
        top_move=["u'"]
    sequence.extend(face_move)
    sequence.extend(top_move)
    return sequence

def state(rubiks_cube):
    check_solve_cube=rubiks_cube.copy()
    is_solved=True
    unsolved_piece=[]
    for x in range(4):
        if check_solve_cube['F4']!=check_solve_cube['F5'] or check_solve_cube['L6']!=check_solve_cube['L5']:
            is_solved=False
            if x==0:
                unsolved_piece=['F4','L6']
            elif x==1:
                unsolved_piece=['F6','R4']
            elif x==2:
                unsolved_piece=['B4','R6']
            else:
                unsolved_piece=['B6','L4']
            break
        check_solve_cube=moves.execute_move(check_solve_cube,'rl')    
    return is_solved,unsolved_piece

def secondLayer(rubiks_cube):
    sequence=[]
    moves.print_2d_cube(rubiks_cube)
    for x in range(4):
        # first search top for top pieces 
        top_pieces=dectect_top_pieces(rubiks_cube)
        print(top_pieces)
        
        if top_pieces:
            matchingFace_moves=move_for_required_face(rubiks_cube,top_pieces)
            print(matchingFace_moves)
            for move in matchingFace_moves:
                rubiks_cube=moves.execute_move(rubiks_cube,move)
                moves.print_2d_cube(rubiks_cube)
            sequence.extend(matchingFace_moves)

            correct_position_moves=secondLayerCases.piece_on_front_top(rubiks_cube)
            print(correct_position_moves)
            for move in correct_position_moves:
                rubiks_cube = moves.execute_move(rubiks_cube,move)
                moves.print_2d_cube(rubiks_cube)
            sequence.extend(correct_position_moves)
        
        # if no top pieces decide if solved or not. if not solved find the unsolved piece
        else:
            is_solved,unsolved_piece=state(rubiks_cube)
            if is_solved==True:
                moves.print_2d_cube(rubiks_cube)
                return sequence
            else:
                print(unsolved_piece)
                bringing_moves=bring_piece_to_top(rubiks_cube,unsolved_piece)
                print(bringing_moves)
                for move in bringing_moves:
                    rubiks_cube = moves.execute_move(rubiks_cube,move)
                    moves.print_2d_cube(rubiks_cube)
                sequence.extend(bringing_moves)

                top_pieces=dectect_top_pieces(rubiks_cube)
                print(top_pieces)
                matchingFace_moves=move_for_required_face(rubiks_cube,top_pieces)
                print(matchingFace_moves)
                for move in matchingFace_moves:
                    rubiks_cube = moves.execute_move(rubiks_cube,move)
                    moves.print_2d_cube(rubiks_cube)
                sequence.extend(matchingFace_moves)

                correct_position_moves=secondLayerCases.piece_on_front_top(rubiks_cube)
                print(correct_position_moves)
                for move in correct_position_moves:
                    rubiks_cube = moves.execute_move(rubiks_cube,move)
                    moves.print_2d_cube(rubiks_cube)
                sequence.extend(correct_position_moves)
    return sequence


print(secondLayer(rubiks_cube))
