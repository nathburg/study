# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#
#     spy_game([1,2,4,0,0,7,5]) --> True
#     spy_game([1,0,2,4,0,5,7]) --> True
#     spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    state = 0
    for x in nums:
        if state == 0:
            if x == 0:
                state = 1
            else:
                continue
        elif state == 1:
            if x == 0:
                state = 2
            else:
                continue
        elif state == 2:
            if x == 7:
                state = 3
                break
            else:
                continue
    if state < 3:
        return False
    else:
        return True
