# testing moves
while cont == 'y':

    option = input("What move to do? ")
    
    if option == "f":
        rubiks_cube = F(rubiks_cube)
    elif option == "f'":
        rubiks_cube = F_inv(rubiks_cube) 
    elif option == "r":
        rubiks_cube = R(rubiks_cube) 
    elif option == "r'":
        rubiks_cube = R_inv(rubiks_cube) 
    elif option == "l":
        rubiks_cube = L(rubiks_cube) 
    elif option == "l'":
        rubiks_cube = L_inv(rubiks_cube) 
    elif option == "u":
        rubiks_cube = U(rubiks_cube) 
    elif option == "u'":
        rubiks_cube = U_inv(rubiks_cube) 
    elif option == "d":
        rubiks_cube = D(rubiks_cube) 
    elif option == "d'":
        rubiks_cube = D_inv(rubiks_cube) 
    elif option == "b":
        rubiks_cube = B(rubiks_cube) 
    elif option == "b'":
        rubiks_cube = B_inv(rubiks_cube) 
    elif option == "rr":
        rubiks_cube = rotateRight(rubiks_cube) 
    elif option == "rl":
        rubiks_cube = rotateLeft(rubiks_cube) 
    elif option == "ru":
        rubiks_cube = rotateUp(rubiks_cube) 
    elif option == "rd":
        rubiks_cube = rotateDown(rubiks_cube) 
    else:
        print("Invalid move. Please try again.")

    print_2d_cube(rubiks_cube)  # Print the current state of the cube
    # Ask if the user wants to continue
    cont = input("Option y if you want to continue: ").strip().lower()

print("Exiting the program.")
