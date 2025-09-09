#take input
rows = int(input("Please enter the number of rows"))
number = 1 # initialise by 1

print ("Floyd's Triange")
#outer loop for numbe of rows
for i in range (1, rows + 1):
    #inner loop for number of columns
        for j in range (1, i+1):
        #Display result
            print(number,end=" ")
            number = number + 1
        print()