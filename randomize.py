import random
import moves
# rubiks_cube={'F1': 'Y', 'F2': 'W', 'F3': 'B', 'F4': 'O', 'F5': 'R', 'F6': 'G', 'F7': 'W', 'F8': 'W', 'F9': 'G', 'R1': 'O', 'R2': 'W', 'R3': 'G', 'R4': 'R', 'R5': 'W', 'R6': 'B', 'R7': 'O', 'R8': 'B', 'R9': 'R', 'B1': 'Y', 'B2': 'Y', 'B3': 'G', 'B4': 'Y', 'B5': 'O', 'B6': 'G', 'B7': 'G', 'B8': 'G', 'B9': 'O', 'L1': 'O', 'L2': 'O', 'L3': 'R', 'L4': 'W', 'L5': 'Y', 'L6': 'G', 'L7': 'Y', 'L8': 'B', 'L9': 'R', 'U1': 'Y', 'U2': 'R', 'U3': 'R', 'U4': 'Y', 'U5': 'G', 'U6': 'R', 'U7': 'B', 'U8': 'B', 'U9': 'W', 'D1': 'B', 'D2': 'O', 'D3': 'W', 'D4': 'O', 'D5': 'B', 'D6': 'R', 'D7': 'B', 'D8': 'Y', 'D9': 'W'}
def randomize(rubiks_cube):
    sequence=[]
    randomMoves=['f',"f'",'r',"r'",'l',"l'",'u',"u'",'d',"d'",'b',"b'",'rr','rl','ru','rd']
    noOfMoves=random.randint(25,50)
    for x in range(noOfMoves):
        sequence.append(random.choice(randomMoves))
    for x in sequence:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
    
    return rubiks_cube


# cube,move=randomize(rubiks_cube)
# moves.print_2d_cube(cube)
# print(move)
# print(cube)
