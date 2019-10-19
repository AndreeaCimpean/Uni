def answer(n):
    if n == 1:
        return 1
    else:
        position = 1
        nr = 2
        found=0
        while found == 0:
            div = 2
            cnr = nr
            while cnr>1 and found == 0:
                if int(cnr)%div == 0:
                    while int(cnr)%div == 0:
                        cnr = int(cnr)/div
                    position+=1
                    if position == n:
                        found = div
                div+=1
            nr+=1
        return found
    

n=int(input('Give a number:'))
print('This is the number in the sequence: ' + str(answer(n)))
        
