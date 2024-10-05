import moves
import frequentSequences

def check_left_rotation(rubiks_cube):
    sequence=[]
    rubiks_cube=moves.execute_move('rr')
    if(rubiks_cube['U2']==rubiks_cube['F5']and rubiks_cube['U8']==rubiks_cube['R5'] and rubiks_cube['R2']==rubiks_cube['B5']):
        sequence.extend(['rr','f']+frequentSequences.righty_sequence+["f'"])
        return sequence

def check_right_rotation(rubiks_cube):
    sequence=[]
    rubiks_cube=moves.execute_move('rl')
    if(rubiks_cube['U2']==rubiks_cube['F5']and rubiks_cube['U8']==rubiks_cube['L5'] and rubiks_cube['L2']==rubiks_cube['B5']):
        sequence.extend(['rl',"f'"]+frequentSequences.lefty_sequence+['f'])
        return sequence

def backPiece_match(rubiks_cube):
    sequence=[]
    if(check_left_rotation(rubiks_cube)):
        sequence=check_left_rotation(rubiks_cube)

    if(check_right_rotation(rubiks_cube)):
        sequence=check_right_rotation()
    return sequence
def frontPiece_match(rubiks_cube):
    sequence=[]
    if(check_left_rotation(rubiks_cube)):
        sequence=check_left_rotation(rubiks_cube)

    if(check_right_rotation(rubiks_cube)):
        sequence=check_right_rotation()
    return sequence

def verticalLine(rubiks_cube):
    sequence=[]
    # check if the line pair is of opposite color 
    # if opposite make a cross where ever no proper cross position will be made
    # if not opposite then turn into horizontal position that matches with at least one piece
    # if any of other three colors match with their face color then check other way
    # if not found in the color then check other color piece for the face color with their side piece color
    if rubiks_cube['B2']==rubiks_cube['B5']:
        sequence=backPiece_match(rubiks_cube)
    elif rubiks_cube['F2']==rubiks_cube['F5']:
        sequence=frontPiece_match(rubiks_cube)
    elif rubiks_cube['F2']==rubiks_cube['F5']:
        sequence=frontPiece_match(rubiks_cube)
def L(rubiks_cube):
    sequence=[]

    if rubiks_cube['U2']==rubiks_cube['U5'] and rubiks_cube['U4']==rubiks_cube['U5']:
        sequence.extend(['f'],frequentSequences.righty_sequence(),["f'"])
    elif rubiks_cube['U2']==rubiks_cube['U5'] and rubiks_cube['U6']==rubiks_cube['U5']:
        sequence.extend(['l','f','u',"f'","u'","l'"])

def dot(rubiks_cube):
    sequence=[]
    sequence.extend(['b','l','u',"l'","u'","b'"])
    sequence.extend(L(rubiks_cube))
    return sequence