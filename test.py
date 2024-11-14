import moves
import validate
import solve_cube
import randomize
import bottomCross
import bottomCorners
import secondLayer
import topCross
import topCrossOrientation
import topCorners
import topCornersOrientation
import randomize
cube = {
    'F1': 'G', 'F2': 'G', 'F3': 'G', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G',  
    'B1': 'B', 'B2': 'B', 'B3': 'B', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B',  
    'L1': 'R', 'L2': 'R', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R',  
    'R1': 'O', 'R2': 'O', 'R3': 'O', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O',  
    'U1': 'Y', 'U2': 'Y', 'U3': 'Y', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'Y',  
    'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
def test(cube):
    cubes=[]
    errors=[]
    total=0
    noOftests=int(input("How many tests to run? "))
    for x in range (noOftests):
            rubiks_cube=randomize.randomize(cube)
            sequence,solved,error=solve_cube.solve_cube(rubiks_cube)
            if not solved:
                cubes.append(rubiks_cube)
                errors.append(error)
            total+=len(sequence)

    if not cubes:
        print(f"all {x} test cases passed")
        return total/noOftests
    else:
        return cubes,errors

def testValidation(cube):
    cubes=[]
    total=0
    noOftests=int(input("How many tests to run? "))
    for x in range (noOftests):
        try:
            rubiks_cube=randomize.randomize(cube)
            sequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
            sequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
            sequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
            sequence,rubiks_cube=topCross.top_cross(rubiks_cube)
            sequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
            sequence,rubiks_cube=topCorners.topCorners(rubiks_cube)
            sequence,rubiks_cube=topCornersOrientation.topCornersOrienation(rubiks_cube)
            solved=validate.checkTopCornersOrietation(rubiks_cube)
            if not solved:
                cubes.append(rubiks_cube)
            total+=len(sequence)
        except Exception as e:
            cubes.append(rubiks_cube)

    if not cubes:
        print("all test cases passed")
        return total/noOftests
    else:
        print("unsolved cubes")
        for x in cubes:
            moves.print_2d_cube(x)
        print(len(cubes))
        return cubes
# print(testValidation(cube))
print(test(cube))
