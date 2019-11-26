36


d 2    num 18
d 3    num 12
d 4    num 9
d 5    num 9
d 6    num 6
18*2




1,2,4,5 10,10, 20,25,50, 100


trinum = 1
for i in range(2,1000000000000): #essentially a while True
    trinum = trinum + i #tfunction
    div = 2 #
    half=trinum//2 #simple math trick 
    num = 100 #trivial, just must be >2
    for d in range(2,half):
        if d>=num:
            break #breaks to if div>500 line, which doesnt                     evaluate, so therefore jumps to for i.
        if trinum%d ==0: 
            num = trinum//d
            div = div + 2
        if d*d == trinum: #5*9 and 9*5 count as 2, but 6*6 counts as 1.
            div -=1

    if div > 500:
        print("FOUND:")
        print(trinum)
        break




