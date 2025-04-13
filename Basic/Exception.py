

ItemsInCart = 0


if ItemsInCart !=2:
    pass
    #raise Exception ("The product count is not matching")

assert(ItemsInCart == 0)


try:
    with open('file.txt', 'r') as readers:
        readers.read()


except:
    print("I reached this block because there is failure in the try block")



try:
    with open('file.txt', 'r') as readers:
        readers.read()


except Exception as e:
    print(e)


#print("I reached this block because there is failure in the try block")