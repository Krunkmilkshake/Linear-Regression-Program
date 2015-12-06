__author__ = 'zacharymelby'


def readpt():

    # This function will prompt the user to enter x and y values.
    # It will check to ensure the user entered valid values, then
    # return the x-y coordinate as a tuple.

    x_valid = False
    y_valid = False

    # take in x and y values and check to ensure user entered
    # valid float values
    while not x_valid:
        try:
            x = float(input('Enter x-coordinate: '))
            x_valid = True
        except ValueError:
            print('Invalid x_coord value, please reenter.')
    while not y_valid:
        try:
            y = float(input('Enter y-coordinate: '))
            y_valid = True
        except ValueError:
            print('Invalid y-coord value, please reenter.')

    return x, y


def makesetpt(set1):
    """
    This function will repeatedly prompt the user for x-y coordinates
    until the user decides they are done. It will then return those
    coordinates as a set of tuples.
    """
    ans = 'y'
    while ans in 'yY':
        set1.add(readpt())
        ans = input("Enter another (y or n)? ")

    return set1


def sums(set1):
    """
    This function will return the five sums needed to determine the regression line.
    """
    allx = 0
    ally = 0
    xy = 0
    xsquare = 0
    ysquare = 0

    # step through the set a calculate the five sums needed
    for point in set1:
        allx += point[0]
        ally += point[1]
        xy += point[0] * point[1]
        xsquare += point[0] * point[0]
        ysquare += point[1] * point[1]

    return allx, ally, xy, xsquare, ysquare


def vert(points_set):
    """
    This function will determined if all the pints are on the same x-coordinate.
    If they are it will return a tuple (True, first-x-value). If not, it should
    return a tuple (False, first-x-value).
    """

    xs_are_equal = True
    x_val = 0
    # gets a x-value to test for
    for point in points_set:
        x_val = point[0]

    # now that we have a x-value, we can check all points against it
    for point in points_set:
        if point[0] != x_val:
            xs_are_equal = False

    # Return based on the bool state of xs_area_equal
    if xs_are_equal:
        return True, x_val
    else:
        return False, x_val


def regression(master_set):
    """
    This function will take in the four sums needed as a tuple and all the points the
    user entered in the form of a set
    """

    sums_tup = sums(master_set)
    # unpack sums_tup for easier reading and writing code

    allx = sums_tup[0]
    ally = sums_tup[1]
    xy = sums_tup[2]
    xsquare = sums_tup[3]
    n = len(master_set)
    sxy = xy - (allx * ally) / n
    sxx = xsquare - (allx * allx) / n

    a = sxy / sxx
    b = (ally / n) - a * (allx / n)

    a_b_return = (a, b)

    return a_b_return


def menu():
    """
    This function will show the menu of options and return
    the users choice in int form.
    """

    print('')
    print('Select an option: ')
    print('1 - Display points')
    print('2 - Remove a point')
    print('3 - Add another point')
    print('4 - Find regression line and exit main')
    n = input('=> ')
    valid_choice = False

    while not valid_choice:
        try:
            n = int(n)
            valid_choice = True
        except ValueError:
            print('Please choose a menu option using numbers')
            n = input('=>')

    return n


def display_points(set1):
    """
    This function will take in a set of points in tuple form.
    It will then display all the points in the set.
    """

    print(set1)


def remove_point(set1):
    """
    This function will take in a set of points in tuple form.
    It will prompt the user for the point they want to remove from the
    set if it is there. It will then return the new set.
    """

    user_point = readpt()
    if user_point not in set1:
        print('Point not in set - no changes made')
    else:
        set1.remove(user_point)

    return set1


def main():

    # Program Greeting
    print('Linear Regression Program\n')

    # init
    main_set = set()
    program_terminate = False

    # Get first point
    set1 = makesetpt(main_set)
    while not program_terminate:

        # Menu choice
        m_choice = menu()
        if m_choice == 1:
            if len(main_set) == 0:
                print('{}')
            else:
                print(main_set)
        elif m_choice == 2:
            print('Enter a point to remove')
            set1 = remove_point(main_set)
            print('Point has been removed')
        elif m_choice == 3:
            print('Enter a point to add:')
            set1.add(readpt())
            print('Point has been added')
        elif m_choice == 4:
            if len(main_set) == 1:
                print("Only one point entered - cannot determine regression line ")
                print("Enter one or more points.")
            elif len(main_set) == 0:
                print("Set has no points - cannot determine regression line ")
                print("Enter one or more points.")
            else:
                if vert(main_set)[0]:
                    print('Regression line equation: x = ', vert(main_set)[1])
                else:
                    a, b = regression(main_set)
                    if b < 0:
                        print('Regression line equation: y = ', a, 'x -', b)
                    else:
                        print('Regression line equation: y = ', a, 'x +', b)
                    return lambda x: a * x + b

main()
