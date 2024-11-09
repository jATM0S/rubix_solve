import moves
import bottomCross
import bottomCorners
import secondLayer
import topCross
import topCrossOrientation
import topCorners
import topCornersOrientation


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
    return sequence

print(solve_cube(rubiks_cube))