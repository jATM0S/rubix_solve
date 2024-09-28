import whiteCrossCases
import moves
rubiks_cube = {
    'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
    'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
    'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
    'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
    'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
    'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
# rubiks_cube={'U1': 'W', 'U2': 'G', 'U3': 'G', 'U4': 'W', 'U5': 'O', 'U6': 'R', 'U7': 'O', 'U8': 'Y', 'U9': 'Y', 'R1': 'B', 'R2': 'Y', 'R3': 'O', 'R4': 'Y', 'R5': 'R', 'R6': 'G', 'R7': 'G', 'R8': 'W', 'R9': 'R', 'F1': 'G', 'F2': 'Y', 'F3': 'O', 'F4': 'R', 'F5': 'B', 'F6': 'Y', 'F7': 'O', 'F8': 'B', 'F9': 'O', 'D1': 'W', 'D2': 'R', 'D3': 'G', 'D4': 'Y', 'D5': 'O', 'D6': 'W', 'D7': 'W', 'D8': 'R', 'D9': 'B', 'L1': 'R', 'L2': 'B', 'L3': 'W', 'L4': 'B', 'L5': 'G', 'L6': 'B', 'L7': 'R', 'L8': 'Y', 'L9': 'R', 'B1': 'B', 'B2': 'O', 'B3': 'B', 'B4': 'Y', 'B5': 'Y', 'B6': 'G', 'B7': 'O', 'B8': 'G', 'B9': 'W'}

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
def dectect_white_side_pieces(rubiks_cube):
    corner_pieces=[['F1','U7','L2'],['F3','U9','R1'],['F7','R9','D1'],['F9','R7','D3'],['U1','R1','B3'],['U3','R3','B1'],['L7','D7','B9'],['R9','D9','B7']]
    white_corner_piece_positions=[]
    for pair in corner_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == 'W':  # Check if the position has a white piece
                white_corner_piece_positions.append(pair)    

    return white_corner_piece_positions


# function to get the white and front center colored piece 
def frontCenter_piece_position(rubiks_cube,white_side_pieces):
    fc_colored_piece_position=[]
    for pair in white_side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                fc_colored_piece_position=pair
    return fc_colored_piece_position


# def whiteCross(rubiks_cube):
#     side_pieces=[['F2','U8'],['F4','L6'],['F6','R4'],['F8','D2'],['U2','B2'],['U4','L2'],['U6','R2'],['B4','R6'],['B6','L4'],['B8','D8'],['R8','D6'],['L8','D4']]
#     sequence=[]
#     for i in range(4):
#         white_side_pieces=dectect_white_side_pieces(rubiks_cube,side_pieces)
#         print(white_side_pieces)

#         required_piece=frontCenter_piece_position(rubiks_cube,white_side_pieces)
#         print(required_piece)
#         moves.print_2d_cube(rubiks_cube)
        
#         sequence.extend(bring_piece_to_F8(rubiks_cube,side_pieces,required_piece))
        
#         rubiks_cube=moves.rotateLeft(rubiks_cube)
#         sequence.append('rl')
#         print(sequence)
#     return sequence

print(dectect_white_side_pieces(rubiks_cube))