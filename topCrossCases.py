import moves
import frequentSequences

def line(rubiks_cube):
    sequence=[]
    if rubiks_cube['U2']==rubiks_cube['U5'] and rubiks_cube['U8']==rubiks_cube['U5']:
        sequence=['r','b','u',"b'","u'"]
    if rubiks_cube['U4']==rubiks_cube['U5'] and rubiks_cube['U6']==rubiks_cube['U5']:
        sequence.extend(['f']+frequentSequences.righty_sequence()+["f'"])
    return sequence


def L(rubiks_cube):
    sequence=[]

    if rubiks_cube['U2']==rubiks_cube['U5'] and rubiks_cube['U4']==rubiks_cube['U5']:
        sequence.extend(['f']+frequentSequences.righty_sequence()+["f'"])
    elif rubiks_cube['U2']==rubiks_cube['U5'] and rubiks_cube['U6']==rubiks_cube['U5']:
        sequence.extend(['l','f','u',"f'","u'","l'"])
    elif rubiks_cube['U6']==rubiks_cube['U5'] and rubiks_cube['U8']==rubiks_cube['U5']:
        sequence.extend(['b','l','u',"l'","u'","b'"])
    elif rubiks_cube['U4']==rubiks_cube['U5'] and rubiks_cube['U8']==rubiks_cube['U5']:
        sequence.extend(['r','b','u',"b'","u'","r'"])
    for x in sequence:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
    sequence.extend(rubiks_cube)
    return sequence

def dot(rubiks_cube):
    sequence=[]
    sequence.extend(['b','l','u',"l'","u'","b'"])
    sequence.extend(L(rubiks_cube))
    for x in sequence:
        moves.print_2d_cube(rubiks_cube)
        rubiks_cube=moves.execute_move(rubiks_cube,x)
    sequence.extend(L(rubiks_cube))
    return sequence

# print(line(rubiks_cube))