s(rubiks_cube)        
    print(niklas)
    for x in niklas:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
        moves.print_2d_cube(rubiks_cube)
    sequence.extend(niklas)