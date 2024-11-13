import moves
import randomize
import bottomCross
import bottomCorners
import secondLayer
import topCross
import topCrossOrientation
import topCorners
import topCornersOrientation
rubiks_cube={'F1': 'O', 'F2': 'O', 'F3': 'O', 'F4': 'B', 'F5': 'O', 'F6': 'W', 'F7': 'W', 'F8': 'O', 'F9': 'R', 'R1': 'Y', 'R2': 'Y', 'R3': 'R', 'R4': 'O', 'R5': 'W', 'R6': 'B', 'R7': 'Y', 'R8': 'W', 'R9': 'W', 'B1': 'W', 'B2': 'O', 'B3': 'Y', 'B4': 'R', 'B5': 'R', 'B6': 'Y', 'B7': 'O', 'B8': 'R', 'B9': 'W', 'L1': 'B', 'L2': 'W', 'L3': 'Y', 'L4': 'R', 'L5': 'Y', 'L6': 'W', 'L7': 'G', 'L8': 'Y', 'L9': 'R', 'U1': 'R', 'U2': 'Y', 'U3': 'G', 'U4': 'R', 'U5': 'B', 'U6': 'B', 'U7': 'B', 'U8': 'B', 'U9': 'G', 'D1': 'B', 'D2': 'G', 'D3': 'G', 'D4': 'G', 'D5': 'G', 'D6': 'G', 'D7': 'O', 'D8': 'G', 'D9': 'B'}
def checkBottomCross(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if rubiks_cube[F'{face}5']!=rubiks_cube[f'{face}8']:
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['2','4','6','8']):
        return False 
    return True
def checkBottomCorners(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all(rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    return True

def checkSecondLayer(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    return True    

def checkTopCross(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    if not all (rubiks_cube['U5']==rubiks_cube[f'U{x}']for x in ['2','4','6','8']):
        return False
    return True    
def checkTopCrossOrientation(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['2','4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    if not all (rubiks_cube['U5']==rubiks_cube[f'U{x}']for x in ['2','4','6','8']):
        return False    
    return True

def checkTopCorners(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[f'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['2','4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    if not all (rubiks_cube['U5']==rubiks_cube[f'U{x}']for x in ['2','4','6','8']):
        return False
    for x in range(4):
        if {rubiks_cube['F5'],rubiks_cube['U5'],rubiks_cube['L5']}!={rubiks_cube['F1'],rubiks_cube['U7'],rubiks_cube['L3']}:
            return False
        rubiks_cube=moves.execute_move(rubiks_cube,'rl')
    return True
def checkTopCornersOrietation(rubiks_cube):
    faces=['F','L','R','B','U','D']
    for face in faces:
        if not all (rubiks_cube[f'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['2','4','6','7','8','9']):
            return False
    return True
def test(cube):
    cubes=[]
    total=0
    noOftests=int(input("How many tests to run? "))
    for x in range (noOftests):
        try:
            rubiks_cube=randomize.randomize(cube)
            sequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
            solved=checkBottomCross(rubiks_cube)
            if not solved:
                cubes.append(rubiks_cube)
            total+=len(sequence)
        except Exception as e:
            cubes.append(rubiks_cube)

    if not cubes:
        print("all test cases passed")
        return total/noOftests
    else:
        return cubes
print(test(rubiks_cube))