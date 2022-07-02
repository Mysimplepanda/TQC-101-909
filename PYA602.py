def check(card):
    if card == "A":
        return 1
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    else:
        return int(card)


numbers=[input() for i in range(5)]
print(sum(list(map(check,numbers))))
