import moves
import bottomCross
import bottomCorners
import secondLayer
rubiks_cube={'F1': 'O', 'F2': 'R', 'F3': 'O', 'F4': 'Y', 'F5': 'R', 'F6': 'O', 'F7': 'B', 'F8': 'Y', 'F9': 'Y', 'R1': 'G', 'R2': 'O', 'R3': 'B', 'R4': 'B', 'R5': 'G', 'R6': 'B', 'R7': 'G', 'R8': 'G', 'R9': 'W', 'B1': 'O', 'B2': 'Y', 'B3': 'W', 'B4': 'W', 'B5': 'O', 'B6': 'O', 'B7': 'R', 'B8': 'O', 'B9': 'O', 'L1': 'R', 'L2': 'R', 'L3': 'G', 'L4': 'W', 'L5': 'B', 'L6': 'G', 'L7': 'Y', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'W', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'Y', 'U8': 'B', 'U9': 'W', 'D1': 'Y', 'D2': 'R', 'D3': 'R', 'D4': 'G', 'D5': 'W', 'D6': 'W', 'D7': 'B', 'D8': 'Y', 'D9': 'G'}

def solve_cube(rubiks_cube):
    sequence=[]
    crossSequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
    sequence.extend(crossSequence)
    bottomCornersSequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
    sequence.extend(bottomCornersSequence)
    secondLayerSequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
    sequence.extend(secondLayerSequence)
    return sequence
print(solve_cube(rubiks_cube))