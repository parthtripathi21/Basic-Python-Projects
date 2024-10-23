import random
import Compare as Cmp

def game(num):
    rnum = random.randint(1,100)

    if rnum == num:
        print(f"You guessed correct the number is {num}")
    else:
        Cmp.compare(num,rnum)
        for i in range(5,0,-1):
            new = int(input(f"Try another number you have {i} chances left."))
            if i>0:
                if new == rnum:
                    print(f"You guessed correctly the number is {rnum}")
                    break
                else:
                    Cmp.compare(new,rnum)
                    continue
            
        print(f"You have used all the chances, but you could not guess the number correctly.\nThe number was {rnum}")