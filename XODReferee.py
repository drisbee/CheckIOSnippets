__author__ = 'Andres'


def checkio(game_result):
    for i in range(3):
        if game_result[i] == 'XXX':
            return "X"
        elif game_result[i] == 'OOO':
            return "O"
        else:
            for row in range(3):
                if game_result[0][row] + game_result[1][row] + game_result[2][row] == "XXX":
                    return "X"
                elif game_result[0][row] + game_result[1][row] + game_result[2][row] == "XXX":
                    return "O"
                else:
                    if (game_result[0][2] + game_result[1][1] + game_result[2][0] == "XXX") or (
                                        game_result[0][0] + game_result[1][1] + game_result[2][2] == "XXX"):
                        return "X"
                    elif (game_result[0][2] + game_result[1][1] + game_result[2][0] == "OOO") or (
                                        game_result[0][0] + game_result[1][1] + game_result[2][2] == "OOO"):
                        return "O"
                    else:
                        return "D"



print checkio(([u'O.X', u'X.X', u'XOO']))
