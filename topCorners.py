import moves
rubiks_cube={'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y', 'R1': 'O', 'R2': 'O', 'R3': 'B', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'F1': 'B', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G', 'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W', 'L1': 'G', 'L2': 'R', 'L3': 'O', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'B1': 'R', 'B2': 'B', 'B3': 'R', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B'}
def checkTopCorners(rubiks_cube):
    print("checkTopCorners")
    checkCorrect=False
    for x in range(4):
        if {rubiks_cube['F5'], rubiks_cube['U5'], rubiks_cube['L5']} <= {rubiks_cube['F1'], rubiks_cube['U7'], rubiks_cube['L3']}:
            rubiks_cube=moves.execute_move(rubiks_cube,'rl')
            checkCorrect=True
        else:
            checkCorrect=False
            return checkCorrect
    return checkCorrect


def findRequiredCorner(rubiks_cube):
    print("findRequiredCorner")
    sequence=[]
    requiredCornerExists=False
    for x in range(4):
        if {rubiks_cube['F5'], rubiks_cube['U5'], rubiks_cube['L5']} <= {rubiks_cube['F1'], rubiks_cube['U7'], rubiks_cube['L3']}:
            requiredCornerExists=True
            if x ==0:
                sequence=[]
            elif x==1:
                sequence=['rl']
            elif x==2:
                sequence=['rl','rl']
            elif x==3:
                sequence=['rr']
            break
        else:
            rubiks_cube=moves.execute_move(rubiks_cube,'rl')
    return requiredCornerExists,sequence


def rightOrLeftNiklas(rubiks_cube):
    print("rightorLeftNIklas")
    sequence=[]
    if {rubiks_cube['F5'], rubiks_cube['R5'], rubiks_cube['U5']} <= {rubiks_cube['U1'], rubiks_cube['B3'], rubiks_cube['L1']}:
        sequence=['r',"u'","l'",'u',"r'","u'",'l','u']
    else:
        sequence=['rr',"l'",'u','r',"u'",'l','u',"r'","u'"]
    return sequence


def topCorners(rubiks_cube):
    sequence=[]
    # if oriented correctly returns as it is
    if checkTopCorners(rubiks_cube):
        return rubiks_cube,sequence
    # find the correct corner if it exists

    requiredCornerExists,cornerToFSequence=findRequiredCorner(rubiks_cube)
    if requiredCornerExists:
        print(cornerToFSequence)
        for x in cornerToFSequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        sequence.extend(cornerToFSequence)
    
    # if correct corner does not exits then do a sune and go to the corrected corner
    else:
        print('making one correct corner')
        sequence.extend(['r',"u'","l'",'u',"r'","u'",'l','u'])
        requiredCornerExists,cornerToFSequence=findRequiredCorner(rubiks_cube)
        print(cornerToFSequence)
        for x in cornerToFSequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        sequence.extend(cornerToFSequence)
        
    
    # if left side move is to be done or right side move is to be done decide
    niklas=rightOrLeftNiklas(rubiks_cube)        
    print(niklas)
    for x in niklas:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
        moves.print_2d_cube(rubiks_cube)
    sequence.extend(niklas)
    
    return rubiks_cube,sequence


# moves.print_2d_cube(rubiks_cube)
print(topCorners(rubiks_cube))