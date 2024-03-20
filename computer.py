#Computer

#insert as insert()
#user  = values entered by user in a array  btw sort the array
#empty = gives us the array containing empty values bte sort the array

import random

def comp_insert(user,empty):
    for i in range(0, len(user),1):
        for j in range(i,len(user),1):
            if user[i] != None and user[j] == None:
                random.choice(empty)
            
            if user[i] == 1 and user[j] == 2:
                if 3 in empty :
                    insert(3)
                    break
            
            if user[i] == 1 and user[j] == 5:
                if 9 in empty :
                    insert(9)
                    break

            if user[i] == 1 and user[j] == 4:
                if 9 in empty :
                    insert(7)
                    break

            if user[i] == 2 and user[j] == 3:
                if 1 in empty :
                    insert(1)
                    break

            if user[i] == 2 and user[j] == 5:
                if 8 in empty :
                    insert(8)
                    break

            if user[i] == 3 and user[j] == 6:
                if 9 in empty :
                    insert(9)
                    break

            if user[i] == 3 and user[j] == 5:
                if 7 in empty :
                    insert(7)
                    break

            if user[i] == 4 and user[j] == 5:
                if 6 in empty :
                    insert(6)
                    break

            if user[i] == 4 and user[j] == 7:
                if 1 in empty :
                    insert(1)
                    break

            if user[i] == 5 and user[j] == 6:
                if 4 in empty :
                    insert(4)
                    break

            if user[i] == 5 and user[j] == 8:
                if 2 in empty :
                    insert(2)
                    break

            if user[i] == 5 and user[j] == 9:
                if 1 in empty :
                    insert(1)
                    break

            if user[i] == 5 and user[j] == 7:
                if 3 in empty :
                    insert(3)
                    break

            if user[i] == 6 and user[j] == 9:
                if 3 in empty :
                    insert(3)
                    break

            if user[i] == 7 and user[j] == 8 :
                if 9 in empty :
                    insert(9)
                    break

            if user[i] == 8 and user[j] == 9:
                if 7 in empty :
                    insert(7)
                    break

    insert(random.choice(empty))
    break