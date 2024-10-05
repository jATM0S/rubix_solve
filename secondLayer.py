import secondLayerCases
import moves

def bring_piece_to_top(rubiks_cube,unsolved_piece):
    print("brig_piece to top")
    if(unsolved_piece==['F4','L6']):
        return secondLayerCases.piece_on_frontLeft(rubiks_cube)
    elif(unsolved_piece==['F6','R4']):
        return secondLayerCases.piece_on_frontRight(rubiks_cube)
    elif(unsolved_piece==['B4','R6']):
        return secondLayerCases.piece_on_rightRight(rubiks_cube)
    elif(unsolved_piece==['B6','L4']):
        return secondLayerCases.piece_on_leftLeft(rubiks_cube)


def dectect_top_pieces(rubiks_cube):
    print("dectect_top_pieces")
    pieces_on_top=[['F2','U8'],['U4','L2'],['U6','R2'],['U2','B2']]
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
    print("move_for_required_face")
    sequence=[]
    face_move=[]
    top_move=[]
    # find the color of a top piece
    for position in top_pieces[0]:  # Iterate over each position in the current pair
        if position in {'F2', 'R2' ,'L2','B2'} :
            color=rubiks_cube[position]
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
    while rubiks_cube['F2'] != rubiks_cube['F5'] or (rubiks_cube['U8'] != rubiks_cube['L5'] and rubiks_cube['U8'] != rubiks_cube['R5']):
        rubiks_cube=moves.execute_move(rubiks_cube,'u')
        top_move.append('u')

    if top_move==['u','u','u']:
        top_move=["u'"]
    sequence.extend(face_move)
    sequence.extend(top_move)
    return sequence

def state(rubiks_cube):
    print("state")
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

def top_to_correct_position(rubiks_cube,top_pieces):
    print("top_to_correct_position")
    sequence=[]
    
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
    return sequence,rubiks_cube

def secondLayer(rubiks_cube):
    sequence=[]
    moves.print_2d_cube(rubiks_cube)
    for x in range(4):
        # first search top for top pieces 
        top_pieces=dectect_top_pieces(rubiks_cube)
        print(top_pieces)
        
        if top_pieces:
           correct_position_moves,rubiks_cube= top_to_correct_position(rubiks_cube,top_pieces)
           sequence.extend(correct_position_moves)

        # if no top pieces decide if solved or not. if not solved find the unsolved piece
        else:
            is_solved,unsolved_piece=state(rubiks_cube)
            if is_solved==True:
                moves.print_2d_cube(rubiks_cube)
                return sequence,rubiks_cube
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
                
                correct_position_moves,rubiks_cube= top_to_correct_position(rubiks_cube,top_pieces)
                sequence.extend(correct_position_moves)
    return sequence,rubiks_cube


# print(secondLayer(rubiks_cube))

