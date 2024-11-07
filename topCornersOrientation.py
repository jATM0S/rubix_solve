import moves

def topCornersOrienation(rubiks_cube):
    sequence=[]
    for x in range(4):
        # check if top corners are solved
        if rubiks_cube['U1']==rubiks_cube['U5'] and rubiks_cube['U3']==rubiks_cube['U5'] and rubiks_cube['U7']==rubiks_cube['U5'] and rubiks_cube['U9']==rubiks_cube['U5']:
            break         
        
        cornerMatchSequence=[]
        # do it until top color matches with the top center
        print("matching top corner")
        while rubiks_cube['U3']!=rubiks_cube['U5']:
            cornerMatchSequence.extend(['r','d',"r'","d'"])
            for x in ['r','d',"r'","d'"]:
                rubiks_cube=moves.execute_move(rubiks_cube,x)
                moves.print_2d_cube(rubiks_cube)
        print(cornerMatchSequence)
        sequence.extend(cornerMatchSequence)

        # check if top corners are solved
        if rubiks_cube['U1']==rubiks_cube['U5'] and rubiks_cube['U3']==rubiks_cube['U5'] and rubiks_cube['U7']==rubiks_cube['U5'] and rubiks_cube['U9']==rubiks_cube['U5']:
            break

        rubiks_cube=moves.execute_move(rubiks_cube,'u')
        sequence.append('u')
    
    # then rotate the top do the move again
    lastOrientation=[]
    testCube=rubiks_cube
    while testCube['F2']!=testCube['F5']:
        lastOrientation.append('u')
        testCube=moves.execute_move(testCube,'u')

    if lastOrientation==['u','u','u']:
        lastOrientation=['u']
    for x in lastOrientation:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
        moves.print_2d_cube(rubiks_cube)

    sequence.extend(lastOrientation)

    return rubiks_cube,sequence
    
# moves.print_2d_cube(rubiks_cube)
# print(topCornersOrienation(rubiks_cube))