import moves

def check_correct(rubiks_cube):
    correct=False
    adjacent_colors={}
    adjacent_colors[rubiks_cube['F5']]=rubiks_cube['R5']
    adjacent_colors[rubiks_cube['R5']]=rubiks_cube['B5']
    adjacent_colors[rubiks_cube['B5']]=rubiks_cube['L5']
    adjacent_colors[rubiks_cube['L5']]=rubiks_cube['F5']
    front_color=rubiks_cube['F2']
    back_color=rubiks_cube['B2']
    left_color=rubiks_cube['L2']
    right_color=rubiks_cube['R2']
    if adjacent_colors[front_color]==right_color and adjacent_colors[right_color]==back_color and adjacent_colors[back_color]==left_color and adjacent_colors[left_color]==front_color:
        correct=True
    return correct

def correct_orientation(rubiks_cube):
    print("correctOrientation")
    sequence=[]
    for x in range(4):
        if rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5']:
            if sequence==['u','u','u']:
                sequence=["u'"]
            return sequence
        rubiks_cube=moves.execute_move(rubiks_cube,'u')
        sequence.append('u')
    return sequence
    
def opossite_colors(rubiks_cube):
    print('Opposite Colors')
    sequence=[]
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
    if opposite:
        if opposite_colors[front_color]==back_color:
            sequence.extend(['b','u',"b'",'u','b',"u'","u'","b'"])
        elif opposite_colors[right_color]==left_color:
            sequence.extend(['r','u',"r'",'u','r',"u'","u'","r'"])
            
    return opposite,sequence

def adjacent_colors(rubiks_cube):
    print('adjacent colors')
    sequence=[]
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
    if adjacent:
        if adjacent_colors[front_color]==right_color:
            sequence.extend(['f','u',"f'",'u','f',"u'","u'","f'"])
        elif adjacent_colors[right_color]==back_color:
            sequence.extend(['r','u',"r'",'u','r',"u'","u'","r'"])
        elif adjacent_colors[back_color]==left_color:
            sequence.extend(['b','u',"b'",'u','b',"u'","u'","b'"])
        elif adjacent_colors[left_color]==front_color:
            sequence.extend(['l','u',"l'",'u','l',"u'","u'","l'"])
    return adjacent,sequence


def topCrossOrientation(rubiks_cube):
    sequence=[]
    if check_correct(rubiks_cube):
        sequence.extend(correct_orientation(rubiks_cube))
        for x in sequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        return sequence,rubiks_cube

    opossite,opossite_sequence=opossite_colors(rubiks_cube)
    print(opossite,opossite_sequence)

    if opossite:
        sequence.extend(opossite_sequence)
        for x in opossite_sequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)

    adjacent,adjacent_sequence=adjacent_colors(rubiks_cube)
    print(adjacent,adjacent_sequence)
    if adjacent:
        sequence.extend(adjacent_sequence)
        for x in adjacent_sequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
    orientation_moves=correct_orientation(rubiks_cube)
    print(orientation_moves)
    for x in orientation_moves:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
        moves.print_2d_cube(rubiks_cube)
    return sequence,rubiks_cube
# moves.print_2d_cube(rubiks_cube)
# print(topCrossOrientation(rubiks_cube))