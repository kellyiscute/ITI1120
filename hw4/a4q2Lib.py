def eraseTable(tab):
    """
    (list) -> None
    This function prepares the game table (array)
    by putting '-' in all the elements.
    It does not create a new array
    Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
    """

    # to complete
    for i in range(tab.__len__()):
        for j in range(tab[i].__len__()):
            tab[i][j] = '-'


# returns nothing


def verifyWin(tab):
    """(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won"
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    """

    # to complete
    winner = testRows(tab)
    if winner != '-':
        print(f'Player {winner} has won!')
        return True
    winner = testCols(tab)
    if winner != '-':
        print(f'Player {winner} has won!')
        return True
    winner = testDiags(tab)
    if winner != '-':
        print(f'Player {winner} has won!')
        return True
    if testDraw(tab):
        print('It\'s a draw')
        return True
    return False


def testRows(tab):
    """ (list) ->  str
    * verify if there is a winning row.
    * Look for three 'X' or three 'O' in a row.
    * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    """

    # to complete
    for i in range(tab.__len__()):
        col = 0
        found_row = True
        while col < len(tab[i]) - 1:
            if tab[i][col] != tab[i][col + 1] or tab[i][col] == '-':
                found_row = False
                break
            col += 1
        if found_row:
            return tab[i][0]

    return '-'


def testCols(tab):
    """ (list) ->  str
    * verify a winning column.
    * look for three 'X' or three 'O' in a column.
    * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    """

    # to complete
    for col in range(len(tab)):
        row = 0
        found_col = True
        while row < len(tab) - 1:
            if tab[row][col] != tab[row + 1][col] or tab[row][col] == '-':
                found_col = False
                break
            row += 1
        if found_col:
            return tab[0][col]

    return '-'  # to be modified so that it returns the winner, or '-' if there is no winner


def testDiags(tab):
    """ (list) ->  str
    * Look for three 'X' or three 'O' in a diagonal.
    * If it is the case, the character 'X' or 'O' is returned
    * otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    """

    # to complete
    i = 0
    diag = tab[0][0]
    diag_found = True
    n = tab.__len__() - 1
    while i < n:
        if tab[i][i] != tab[i + 1][i + 1]:
            diag_found = False
            break
        i += 1
    if diag_found and diag != '-':
        return diag

    i = 0
    diag = tab[0][n]
    diag_found = True
    while i < n:
        if tab[i][n - i] != tab[i + 1][n - (i + 1)]:
            diag_found = False
            break
        i += 1
    if diag_found:
        return diag
    else:
        return '-'


def testDraw(tab):
    """ (list) ->  bool
    * verify if there is a draw
    * check if all the array elements have X or O, not '-'.
    * If we do not find find any '-' in the array, return True.
    * If there is any '-', return false.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    """

    # to complete
    for i in tab:
        if '-' in i:
            return False
    return True
