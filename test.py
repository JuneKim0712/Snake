elif snake[-1][0] == food[0] and direction[0] != 20 and snake[-1][0] - 20 > -20 and bin[4]:
        ans = 'left'
    elif snake[-1][0] == food[0] and direction[0] != -20 and snake[-1][0] + 20 < 500 and bin[3]:
        ans = 'right'
    elif snake[-1][1] == food[1] and direction[1] != 20 and snake[-1][1] - 20 > -20 and bin[2]:
        ans = 'up'
    elif snake[-1][1] == food[1] and direction[1] != -20 and snake[-1][1] + 20 < 500 and bin[1]:
        ans = 'down'