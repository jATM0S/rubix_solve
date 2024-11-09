import random
import moves
rubiks_cube={'F1': 'R', 'F2': 'G', 'F3': 'Y', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G', 'R1': 'G', 'R2': 'O', 'R3': 'R', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'B1': 'G', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B', 'L1': 'Y', 'L2': 'R', 'L3': 'B', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'U1': 'O', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'O', 'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
def randomize(rubiks_cube):
    sequence=[]
    randomMoves=['f',"f'",'r',"r'",'l',"l'",'u',"u'",'d',"d'",'b',"b'",'rr','rl','ru','rd']
    noOfMoves=random.randint(15,25)
    for x in range(noOfMoves):
        sequence.append(random.choice(randomMoves))
    for x in sequence:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
    
    return rubiks_cube,sequence


cube,move=randomize(rubiks_cube)
moves.print_2d_cube(cube)
print(move)
print(cube)