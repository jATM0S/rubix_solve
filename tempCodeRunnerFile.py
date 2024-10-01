    top_pieces=dectect_top_pieces(rubiks_cube)
    print(top_pieces)
    
    if top_pieces:
        matchingFace_moves=move_for_required_face(rubiks_cube,top_pieces)
        for move in matchingFace_moves:
            rubiks_cube=moves.execute_move(rubiks_cube,move)
        sequence.extend(matchingFace_moves)
        print(matchingFace_moves)

        sequence.extend(secondLayerCases.piece_on_front_top(rubiks_cube))
        # Execute the sequence of moves and print the cube after each one
        for move in sequence:
            rubiks_cube = moves.execute_move(rubiks_cube,move)
            moves.print_2d_cube(rubiks_cube)
