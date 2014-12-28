__author__ = 'Andres'


def checkio(game_result):
    three = [(0,0)]
    for i in range(3):
        if game_result[i] == 'XXX':
            return "X"
            break
        if game_result[i] == 'OOO':
            return "O"
            break
        if (game_result[0][0] + game_result[1][0] + game_result[2][0] == "XXX"
            ) or (game_result[0][1] + game_result[1][1] + game_result[2][1] == "XXX"
            ) or (game_result[0][2] + game_result[1][2] + game_result[2][2] == "XXX"
            ) or (game_result[0][2] + game_result[1][1] + game_result[2][0] == "XXX"
            ) or (game_result[0][0] + game_result[1][1] + game_result[2][2] == "XXX"):
            return "X"
            break
        if (game_result[0][0] + game_result[1][0] + game_result[2][0] == "OOO"
            ) or (game_result[0][1] + game_result[1][1] + game_result[2][1] == "OOO"
            ) or (game_result[0][2] + game_result[1][2] + game_result[2][2] == "OOO"
            ) or (game_result[0][2] + game_result[1][1] + game_result[2][0] == "OOO"
            ) or (game_result[0][0] + game_result[1][1] + game_result[2][2] == "OOO"):
            return "O"
            break
    else:
        return "D"


print checkio([u"OO.",u"XXX",u"XOX"])
print checkio([
        u"X.O",
        u"XX.",
        u"XOO"])== "X", "Xs wins"
print checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
print checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
print checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"
