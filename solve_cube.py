import moves
import bottomCross
import bottomCorners
import secondLayer
import topCross
import topCrossOrientation
import topCorners
import topCornersOrientation
# rubiks_cube={'F1': 'R', 'F2': 'B', 'F3': 'W', 'F4': 'R', 'F5': 'Y', 'F6': 'W', 'F7': 'W', 'F8': 'W', 'F9': 'W', 'R1': 'B', 'R2': 'Y', 'R3': 'Y', 'R4': 'R', 'R5': 'G', 'R6': 'G', 'R7': 'R', 'R8': 'Y', 'R9': 'W', 'B1': 'O', 'B2': 'W', 'B3': 'G', 'B4': 'Y', 'B5': 'W', 'B6': 'G', 'B7': 'G', 'B8': 'R', 'B9': 'O', 'L1': 'Y', 'L2': 'W', 'L3': 'B', 'L4': 'O', 'L5': 'B', 'L6': 'B', 'L7': 'G', 'L8': 'Y', 'L9': 'R', 'U1': 'R', 'U2': 'B', 'U3': 'B', 'U4': 'G', 'U5': 'O', 'U6': 'O', 'U7': 'Y', 'U8': 'O', 'U9': 'O', 'D1': 'B', 'D2': 'O', 'D3': 'G', 'D4': 'R', 'D5': 'R', 'D6': 'B', 'D7': 'Y', 'D8': 'G', 'D9': 'O'}

def checkSolved(rubiks_cube):
    solved=False
    faces=['F','L','R','B','U','D']
    for face in faces:
        if not all(rubiks_cube[f'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['1','2','3','4','6','7','8','9']): 
            return False
    return True

def solve_cube(rubiks_cube):
    sequence=[]
    print("bottomcross")
    crossSequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
    sequence.extend(crossSequence)
    print(crossSequence)

    print("bottomcorners")
    cornersSequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
    sequence.extend(cornersSequence)
    print(cornersSequence)
    
    print("2nd layer")
    secondLayerSequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
    sequence.extend(secondLayerSequence)
    print(secondLayerSequence)
    
    print("topCross")
    topCrossSequence,rubiks_cube=topCross.top_cross(rubiks_cube)
    sequence.extend(topCrossSequence)
    print(topCrossSequence)
    
    print("topcrossOrientation")
    topCrossOrientationSequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
    sequence.extend(topCrossOrientationSequence)
    print(topCrossOrientationSequence)

    print("topCorners")
    topCornersSequence,rubiks_cube=topCorners.topCorners(rubiks_cube)
    sequence.extend(topCornersSequence)
    print(topCornersSequence)

    print("topCornersOrientation")
    topCornersOrientationSequence,rubiks_cube=topCornersOrientation.topCornersOrienation(rubiks_cube)
    sequence.extend(topCornersOrientationSequence)
    print(topCornersOrientationSequence)
    
    moves.print_2d_cube(rubiks_cube)
    if checkSolved(rubiks_cube):
        return sequence,True
    else:
        return sequence,False
    # return sequence

# print(solve_cube(rubiks_cube))
# print(checkSolved(rubiks_cube))