import whiteCornerCases
import moves
# rubiks_cube = {
#     'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
#     'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
#     'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
#     'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
#     'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
#     'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
# rubiks_cube={'U1': 'O', 'U2': 'B', 'U3': 'G', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'B', 'U8': 'B', 'U9': 'W', 'R1': 'R', 'R2': 'R', 'R3': 'W', 'R4': 'Y', 'R5': 'B', 'R6': 'G', 'R7': 'R', 'R8': 'G', 'R9': 'G', 'F1': 'Y', 'F2': 'O', 'F3': 'G', 'F4': 'R', 'F5': 'O', 'F6': 'G', 'F7': 'O', 'F8': 'Y', 'F9': 'B', 'D1': 'B', 'D2': 'R', 'D3': 'W', 'D4': 'Y', 'D5': 'W', 'D6': 'W', 'D7': 'Y', 'D8': 'O', 'D9': 'Y', 'L1': 'G', 'L2': 'O', 'L3': 'R', 'L4': 'R', 'L5': 'G', 'L6': 'B', 'L7': 'O', 'L8': 'B', 'L9': 'W', 'B1': 'O', 'B2': 'W', 'B3': 'Y', 'B4': 'O', 'B5': 'R', 'B6': 'W', 'B7': 'R', 'B8': 'Y', 'B9': 'B'}
# rubiks_cube={'F1': 'O', 'F2': 'R', 'F3': 'O', 'F4': 'Y', 'F5': 'R', 'F6': 'O', 'F7': 'B', 'F8': 'Y', 'F9': 'Y', 'R1': 'G', 'R2': 'O', 'R3': 'B', 'R4': 'B', 'R5': 'G', 'R6': 'B', 'R7': 'G', 'R8': 'G', 'R9': 'W', 'B1': 'O', 'B2': 'Y', 'B3': 'W', 'B4': 'W', 'B5': 'O', 'B6': 'O', 'B7': 'R', 'B8': 'O', 'B9': 'O', 'L1': 'R', 'L2': 'R', 'L3': 'G', 'L4': 'W', 'L5': 'B', 'L6': 'G', 'L7': 'Y', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'W', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'Y', 'U8': 'B', 'U9': 'W', 'D1': 'Y', 'D2': 'R', 'D3': 'R', 'D4': 'G', 'D5': 'W', 'D6': 'W', 'D7': 'B', 'D8': 'Y', 'D9': 'G'}
def bring_piece_to_F7(rubiks_cube,corner_pieces,moving_piece):
    if(moving_piece==corner_pieces[0]):
        return whiteCornerCases.front_top_left(rubiks_cube)
    elif(moving_piece==corner_pieces[1]):
        return whiteCornerCases.front_top_right(rubiks_cube)
    elif(moving_piece==corner_pieces[2]):
        return whiteCornerCases.front_bottom_left(rubiks_cube)
    elif(moving_piece==corner_pieces[3]):
        return whiteCornerCases.front_bottom_right(rubiks_cube)
    elif(moving_piece==corner_pieces[4]):
        return whiteCornerCases.left_left_top(rubiks_cube)
    elif(moving_piece==corner_pieces[5]):
        return whiteCornerCases.right_right_top(rubiks_cube)
    elif(moving_piece==corner_pieces[6]):
        return whiteCornerCases.left_left_bottom(rubiks_cube)
    elif(moving_piece==corner_pieces[7]):
        return whiteCornerCases.right_right_bottom(rubiks_cube)
    
    
# to dectect the white piece
def dectect_white_corner_pieces(rubiks_cube,corner_pieces):

    white_corner_pieces=[]
    for pair in corner_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == 'W':  # Check if the position has a white piece
                white_corner_pieces.append(pair)    

    return white_corner_pieces


# function to get the white and front center colored piece 
def leftCorner_piece_position(rubiks_cube,white_corner_pieces):
    leftCorner_piece_position=[]
    required_pieces=[]
    for pair in white_corner_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                required_pieces.append(pair)
            
    for piece in required_pieces:
        for face in piece:
            if rubiks_cube[face]==rubiks_cube['L5']:
                leftCorner_piece_position=piece
    return leftCorner_piece_position

def rightCorner_piece_position(rubiks_cube,white_corner_pieces):
    rightCorner_piece_position=[]
    required_pieces=[]
    for pair in white_corner_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                required_pieces.append(pair)
    print(required_pieces)
    for piece in required_pieces:
        for face in piece:
            if rubiks_cube[face]==rubiks_cube['R5']:
                rightCorner_piece_position=piece
    return rightCorner_piece_position


# def whiteCorners(rubiks_cube):
#     corner_pieces=[['F1','U7','L2'],['F3','U9','R1'],['F7','L9','D1'],['F9','R7','D3'],['U1','R1','B3'],['U3','R3','B1'],['L7','D7','B9'],['R9','D9','B7']]
#     sequence=[]
#     for i in range(4):
#         moves.print_2d_cube(rubiks_cube)
#         white_corner_pieces=dectect_white_corner_pieces(rubiks_cube,corner_pieces)
#         print(white_corner_pieces)

#         leftCorner_piece=leftCorner_piece_position(rubiks_cube,white_corner_pieces)
#         print(leftCorner_piece)

#         # white_corner_pieces=dectect_white_corner_pieces(rubiks_cube,corner_pieces)
#         # print(white_corner_pieces)
#         # rightCorner_piece=rightCorner_piece_position(rubiks_cube,white_corner_pieces)
#         # print(rightCorner_piece)
#         face_moves=bring_piece_to_F7(rubiks_cube,corner_pieces,leftCorner_piece)
#         print(face_moves)
#         for move in face_moves:
#             rubiks_cube = moves.execute_move(rubiks_cube, move)
#             moves.print_2d_cube(rubiks_cube) 
       
#         sequence.extend(face_moves)
        
#         rubiks_cube=moves.rotateLeft(rubiks_cube)
#         sequence.append('rl')
#         # print(sequence)
#     return sequence
def whiteCorners(rubiks_cube):
    corner_pieces=[['F1','U7','L3'],['F3','U9','R1'],['F7','L9','D1'],['F9','R7','D3'],['U1','L1','B3'],['U3','R3','B1'],['L7','D7','B9'],['R9','D9','B7']]
    sequence=[]
    moves.print_2d_cube(rubiks_cube)
    for x in range(4):
        white_corner_pieces=dectect_white_corner_pieces(rubiks_cube,corner_pieces)
        print(white_corner_pieces)
        leftCorner_piece=leftCorner_piece_position(rubiks_cube,white_corner_pieces)
        print(leftCorner_piece)

        face_moves=bring_piece_to_F7(rubiks_cube,corner_pieces,leftCorner_piece)
        print(face_moves)
        for x in face_moves:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        sequence.extend(face_moves)
        rubiks_cube=moves.rotateLeft(rubiks_cube)
        moves.print_2d_cube(rubiks_cube)
        sequence.append('rl')
    return sequence


print(whiteCorners(rubiks_cube))