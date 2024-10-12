import moves
rubiks_cube={'F1': 'Y', 'F2': 'R', 'F3': 'O', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G', 'R1': 'Y', 'R2': 'B', 'R3': 'Y', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'B1': 'R', 'B2': 'O', 'B3': 'Y', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B', 'L1': 'O', 'L2': 'G', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'Y', 'U3': 'G', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'B', 'U8': 'Y', 'U9': 'G', 'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}
def correct_orientation(rubiks_cube):
    correct=False
    for x in range(4):
        if rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5']:
            correct=True
            return correct
        rubiks_cube=moves.execute_move('u')

    return correct

def dectect_opossite_colors(rubiks_cube):
    opposite_colors={}
    opposite_colors[rubiks_cube['F5']]=rubiks_cube['B5']
    opposite_colors[rubiks_cube['B5']]=rubiks_cube['F5']
    opposite_colors[rubiks_cube['U5']]=rubiks_cube['D5']
    opposite_colors[rubiks_cube['D5']]=rubiks_cube['U5']
    opposite_colors[rubiks_cube['R5']]=rubiks_cube['L5']
    opposite_colors[rubiks_cube['L5']]=rubiks_cube['R5']
    front_color=rubiks_cube['F2']
    back_color=rubiks_cube['B2']
    left_color=rubiks_cube['L2']
    right_color=rubiks_cube['R2']
    print(opposite_colors)
    moves.print_2d_cube(rubiks_cube)
    opposite=False
    if opposite_colors[front_color]==back_color or opposite_colors[right_color]==left_color:
        opposite=True
    return opposite

def dectect_adjacent_colors(rubiks_cube):
    adjacent_colors={}
    adjacent_colors[rubiks_cube['F5']]=rubiks_cube['R5']
    adjacent_colors[rubiks_cube['R5']]=rubiks_cube['B5']
    adjacent_colors[rubiks_cube['B5']]=rubiks_cube['L5']
    adjacent_colors[rubiks_cube['L5']]=rubiks_cube['F5']
    front_color=rubiks_cube['F2']
    back_color=rubiks_cube['B2']
    left_color=rubiks_cube['L2']
    right_color=rubiks_cube['R2']
    print(adjacent_colors)
    moves.print_2d_cube(rubiks_cube)
    adjacent=False
    if adjacent_colors[front_color]==right_color or adjacent_colors[right_color]==back_color or adjacent_colors[back_color]==left_color or adjacent_colors[left_color]==front_color:
        adjacent=True
    return adjacent


def dectect_cube_orientation(rubiks_cube):
    # opposite or not 
    if dectect_opossite_colors(rubiks_cube):
        print('opposite')
    else:
        print('not opposite')

print(dectect_adjacent_colors(rubiks_cube))