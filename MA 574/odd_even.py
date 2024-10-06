# Take the user input for z and coefficients.
z = int(input("Provide z-> "))
coefficients = input("Provide the Coefficients of the polynomial->")
# convert the input to array
coeffArr = coefficients.split()
# define a string variable and assign the 1st element of the array in the form of string.
strP = str(coeffArr[0])
# define a int variable and assign the 1st element of the array in the form of string.
finalAns = int(coeffArr[0])
# declare a for loop to perform the operations to create a string for the user and to generate the output.
for i in range(1,len(coeffArr)):
    #if the coefficient is 0 - ignore
    if(int(coeffArr[i])==0):
        pass
    # if the coefficient is positive mention +sign explcitely int the string variable.
    elif(int(coeffArr[i])>0):
        #if the counter = 1 just add x with power 1 
        if(i==1):
            strP = strP+"+"+str(coeffArr[i])+"x"
            finalAns = finalAns+(int(coeffArr[i])*z)
        # else add power similar to the counter i
        else:
            strP = strP+"+"+str(coeffArr[i])+"x^"+str(i)
            finalAns = finalAns+(int(coeffArr[i])*(z**i))
    else:
        if(i==1):
            strP = strP+str(coeffArr[i])+"x"
            finalAns = finalAns+(int(coeffArr[i])*z)
        else:
            strP = strP+str(coeffArr[i])+"x^"+str(i)
            finalAns = finalAns+(int(coeffArr[i])*(z**i))
print("The provided polynomial is P(x)=",strP)
print("P("+str(z)+")="+strP.replace("x","("+str(z)+")"),"=",finalAns)

print(finalAns)
