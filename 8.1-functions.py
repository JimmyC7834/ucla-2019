 ####################### PART ONE #########################
def max(a, b):
    # 1) create a program that checks which input/argument (a or b) is bigger
    # 2) return the bigger value
    ################### YOUR CODE BELOW ######################
    return a if a > b else b
    ##########################################################

# Test Cases:

print('max() results below: ')
print(max( 2, 10))
print(max( 4, 4))
print(max( 33, 32))
print(max( -50, -5))
print(max( -1, 0))






####################### PART TWO #########################
# 1) create your own function called findMax
# 2) findMax will take a LIST as an input/argument
# 3) use the max function from Part One to find the maximum value in the LIST
# 4) return the max value
# hint: create an empty function first and
# hint: test that you can properly invoke/call the function in part 3

################### YOUR CODE BELOW ######################
def findMax(num):
    m = num[0]
    for n in num:
        m = max(m,n)
    return m


##########################################################









####################### PART THREE #########################
# 1) Run your findMax function using the Test Cases below as the inputs
#
# Test Cases:
print('findMax() results below: ')
list1 = [4,2,99,32,50]
list2 = ['mars', 'mark', 'marge', 'marvel', 'mares']
list3 = ['Narwhal', 'Chinese Water Deer', 'Pangolin', 'Bat-eared Fox','Markhor']
list4 = ['Daisy', 'iris', 'Violet', 'poppy', 'Lily']
ls = [list1,list2,list3,list4]
for l in ls:
    print(findMax(l))

##################### EXAMPLE ############################
# We created two functions below called firstFunction() and anotherFunction()
# anotherFunction() uses firstFunction() and then we printed the results
# Feel free to uncomment and run the program below:
#
# def firstFunction(a,b):
#     return [a,b]

# def anotherFunction (someList):
#     return(firstFunction(someList[1], someList[3]))

# print('anotherFunction() results below: ')
# aList = [1,2,3,4]
# b = anotherFunction(aList) 
# print(b)
#
##########################################################

################### YOUR CODE BELOW ######################




##########################################################

