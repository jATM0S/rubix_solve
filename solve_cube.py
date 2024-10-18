import moves
import bottomCross
import bottomCorners
import secondLayer
import topCross
import topCrossOrientation
rubiks_cube={'F1': 'R', 'F2': 'W', 'F3': 'Y', 'F4': 'Y', 'F5': 'Y', 'F6': 'Y', 'F7': 'Y', 'F8': 'Y', 'F9': 'Y', 'R1': 'B', 'R2': 'O', 'R3': 'B', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'B1': 'Y', 'B2': 'Y', 'B3': 'O', 'B4': 'W', 'B5': 'W', 'B6': 'W', 'B7': 'W', 'B8': 'W', 'B9': 'W', 'L1': 'W', 'L2': 'R', 'L3': 'W', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'O', 'U4': 'B', 'U5': 'B', 'U6': 'B', 'U7': 'B', 'U8': 'B', 'U9': 'R', 'D1': 'G', 'D2': 'G', 'D3': 'G', 'D4': 'G', 'D5': 'G', 'D6': 'G', 'D7': 'G', 'D8': 'G', 'D9': 'G'}

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

    print(rubiks_cube)
    return sequence

print(solve_cube(rubiks_cube))