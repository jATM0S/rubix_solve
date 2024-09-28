import whiteCrossCases
import moves
# rubiks_cube = {
#     'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
#     'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
#     'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
#     'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
#     'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
#     'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
rubiks_cube={'U1': 'O', 'U2': 'B', 'U3': 'G', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'B', 'U8': 'B', 'U9': 'W', 'R1': 'R', 'R2': 'R', 'R3': 'W', 'R4': 'Y', 'R5': 'B', 'R6': 'G', 'R7': 'R', 'R8': 'G', 'R9': 'G', 'F1': 'Y', 'F2': 'O', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'G', 'F7': 'O', 'F8': 'Y', 'F9': 'B', 'D1': 'B', 'D2': 'R', 'D3': 'W', 'D4': 'Y', 'D5': 'W', 'D6': 'W', 'D7': 'Y', 'D8': 'O', 'D9': 'Y', 'L1': 'G', 'L2': 'O', 'L3': 'R', 'L4': 'R', 'L5': 'G', 'L6': 'B', 'L7': 'O', 'L8': 'B', 'L9': 'W', 'B1': 'O', 'B2': 'W', 'B3': 'Y', 'B4': 'O', 'B5': 'R', 'B6': 'W', 'B7': 'R', 'B8': 'Y', 'B9': 'B'}

# cases and moves for each situation
def bring_piece_to_F8(rubiks_cube,side_pieces,moving_piece):
    if(moving_piece==side_pieces[0]):
        return whiteCrossCases.piece_on_front_top(rubiks_cube)
    elif(moving_piece==side_pieces[1]):
        return whiteCrossCases.piece_on_front_left(rubiks_cube)
    elif(moving_piece==side_pieces[2]):
        return whiteCrossCases.piece_on_front_right(rubiks_cube)
    elif(moving_piece==side_pieces[3]):
        return whiteCrossCases.piece_on_front_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[4]):
        return whiteCrossCases.piece_on_back_top(rubiks_cube)
    elif(moving_piece==side_pieces[5]):
        return whiteCrossCases.piece_on_left_top(rubiks_cube)
    elif(moving_piece==side_pieces[6]):
        return whiteCrossCases.piece_on_right_top(rubiks_cube)
    elif(moving_piece==side_pieces[7]):
        return whiteCrossCases.piece_on_right_right(rubiks_cube)
    elif(moving_piece==side_pieces[8]):
        return whiteCrossCases.piece_on_left_left(rubiks_cube)
    elif(moving_piece==side_pieces[9]):
        return whiteCrossCases.piece_on_back_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[10]):
        return whiteCrossCases.piece_on_right_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[11]):
        return whiteCrossCases.piece_on_left_bottom(rubiks_cube)
    
# to dectect the white piece
def dectect_white_side_pieces(rubiks_cube,side_pieces):
    white_side_piece_positions=[]
    for pair in side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == 'W':  # Check if the position has a white piece
                white_side_piece_positions.append(pair)    

    return white_side_piece_positions


# function to get the white and front center colored piece 
def frontCenter_piece_position(rubiks_cube,white_side_pieces):
    fc_colored_piece_position=[]
    for pair in white_side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                fc_colored_piece_position=pair
    return fc_colored_piece_position


def whiteCross(rubiks_cube):
    side_pieces=[['F2','U8'],['F4','L6'],['F6','R4'],['F8','D2'],['U2','B2'],['U4','L2'],['U6','R2'],['B4','R6'],['B6','L4'],['B8','D8'],['R8','D6'],['L8','D4']]
    sequence=[]
    for i in range(4):
        # moves.print_2d_cube(rubiks_cube)
        white_side_pieces=dectect_white_side_pieces(rubiks_cube,side_pieces)
        print(white_side_pieces)

        required_piece=frontCenter_piece_position(rubiks_cube,white_side_pieces)
        print(required_piece)
        
        face_moves=bring_piece_to_F8(rubiks_cube,side_pieces,required_piece)
        print(face_moves)
        for move in face_moves:
            rubiks_cube = whiteCrossCases.execute_move(rubiks_cube, move)
            moves.print_2d_cube(rubiks_cube) 
        
        rubiks_cube=moves.rotateLeft(rubiks_cube)
        moves.print_2d_cube(rubiks_cube)
        sequence.extend(face_moves)
        sequence.append('rl')
    return sequence

print(whiteCross(rubiks_cube))
