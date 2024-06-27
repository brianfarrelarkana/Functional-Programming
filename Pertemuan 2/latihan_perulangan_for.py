for i in range (10, 25) :
    for j in range (2, 1) :
        if i % j == 0 :
            print ("%d bukan prima" % i)
            break
        else :
            print ("%d adalah bilangan prima" % i)