import moves
import bottomCross
import bottomCorners
import secondLayer
import topCross
import topCrossOrientation
rubiks_cube={'F1': 'W', 'F2': 'W', 'F3': 'B', 'F4': 'B', 'F5': 'O', 'F6': 'B', 'F7': 'O', 'F8': 'O', 'F9': 'O', 'R1': 'R', 'R2': 'R', 'R3': 'R', 'R4': 'Y', 'R5': 'W', 'R6': 'B', 'R7': 'W', 'R8': 'W', 'R9': 'W', 'B1': 'B', 'B2': 'O', 'B3': 'Y', 'B4': 'R', 'B5': 'R', 'B6': 'Y', 'B7': 'R', 'B8': 'R', 'B9': 'R', 'L1': 'O', 'L2': 'O', 'L3': 'O', 'L4': 'O', 'L5': 'Y', 'L6': 'W', 'L7': 'Y', 'L8': 'Y', 'L9': 'Y', 'U1': 'B', 'U2': 'W', 'U3': 'W', 'U4': 'B', 'U5': 'B', 'U6': 'Y', 'U7': 'B', 'U8': 'R', 'U9': 'Y', 'D1': 'G', 'D2': 'G', 'D3': 'G', 'D4': 'G', 'D5': 'G', 'D6': 'G', 'D7': 'G', 'D8': 'G', 'D9': 'G'}
# def solve_cube(rubiks_cube):
#     sequence=[]
#     print("bottomcross")
#     # crossSequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
#     # sequence.extend(crossSequence)

#     print("bottomcorner")
#     bottomCornersSequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
#     sequence.extend(bottomCornersSequence)

#     # print("secondlayer")
#     # secondLayerSequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
#     # sequence.extend(secondLayerSequence)
#     # topCrossSequence,rubiks_cube=topCross.top_cross(rubiks_cube)
#     # sequence.extend(topCrossSequence)
#     # topCrossOrientationSequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
#     # sequence.extend(topCrossOrientationSequence)
#     # print(len(sequence))
#     return sequence
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
    print(rubiks_cube)
    return sequence

print(solve_cube(rubiks_cube))