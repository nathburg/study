# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
 #   blackjack(5,6,7) --> 18
  #  blackjack(9,9,9) --> 'BUST'
   # blackjack(9,9,11) --> 19
    
    def blackjack(a,b,c):
    sum = a + b + c
    for x in (a,b,c):
        if x < 1 or x > 11:
            return ("Your cards are fake.")
    if sum <= 21:
        return sum
    else:
        for x in (a,b,c):
            if x == 11:
                sum -= 10
                if sum <= 21:
                    return sum
        if sum > 21:
            return 'BUST'
