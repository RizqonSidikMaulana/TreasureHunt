
def printMap(marker, total_x_axis, total_y_axis):
    print('===== MAP =====')

    for y in range(total_y_axis):
        print()
        for x in range(total_x_axis):
            cell = (y,x)
            if cell in marker :
                if marker[cell] == 'clear' :
                    print('. ', end='')
                else :
                    print('x ', end='')
            else :
                print('# ', end='')

    print("\n")
    print("===============")
    print()

def findTreasure(position, marker, total_x_axis, total_y_axis):
    coordinate_treasure = []

    position = (position[0] - 1, position[1])
    for a in range(position[0], 0, -1):
        a_step = (a, position[1])

        # If position on A step is a clear path so continue to the B step
        if a_step in marker:
            b_step = (a_step[0], a_step[1] + 1)

            for b in range(b_step[1], total_x_axis, 1):
                b_step = (b_step[0], b)

                # If position on B step is a clear path so continue to the C step
                if b_step in marker :

                    for c in range(b_step[0], total_y_axis, 1):
                        c_step = (c + 1, b_step[1])

                        # If position on C step is a clear path, add the coordinate to the list
                        if c_step in marker:
                            coordinate_treasure.append((c_step))
                        else :
                            break
                else :
                    break
        else :
            break

    return coordinate_treasure

def displayBoardWithProbableTreasure(start_position, marker, total_x_axis, total_y_axis):
    print('Treasure Coordinate ')

    # Get coordinate of the treasure.
    probable_treasure = findTreasure(start_position, marker, total_x_axis, total_y_axis)

    for y in range(total_y_axis):
        print()
        for x in range(total_x_axis):
            cell = (y,x)
            if cell in marker :
                if cell in probable_treasure :
                    print('$ ', end='')
                elif marker[cell] == 'clear' :
                    print('. ', end='')
                else :
                    print('x ', end='')

            else :
                print('# ', end='')

    print("\n")
    print("===============")
    print()

# mark clear path and start position
marker = {
        (1,1) : "clear",
        (1,2) : "clear",
        (1,3) : "clear",
        (1,4) : "clear",
        (1,5) : "clear",
        (1,6) : "clear",
        (2,1) : "clear",
        (2,5) : "clear",
        (2,6) : "clear",
        (3,1) : "clear",
        (3,2) : "clear",
        (3,3) : "clear",
        (3,5) : "clear",
        (4,1) : "start",
        (4,3) : "clear",
        (4,4) : "clear",
        (4,5) : "clear",
        (4,6) : "clear",
    }

# Print map with following dimensions.
x = 8
y = 6
printMap(marker, x, y)

# Coordinate to start hunting.
start_position = (4,1)

print("Total Probable Coordinate : ", len(findTreasure(start_position, marker, x, y)))
print("Coordinate : ", findTreasure(start_position, marker, x, y))
displayBoardWithProbableTreasure(start_position, marker, x, y)


