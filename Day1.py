#only takes into consideration integer values in the string
def callibrate(string):
    nums = []
    for i in string:
        if i.isdigit():
            nums.append(i)
    n = "" + nums[0] + nums[nums.__len__() - 1]
    return n


def returnInt(string):
    if string == "one":
        return 1
    elif string == "two":
        return 2
    elif string == "three":
        return 3
    elif string == "four":
        return 4
    elif string == "five":
        return 5
    elif string == "six":
        return 6
    elif string == "seven":
        return 7
    elif string == "eight":
        return 8
    elif string == "nine":
        return 9
    elif string == "zero":
        return 0
    else:
        return string
    


#Takes into consideration spelled out integers allong with integer values

#Possible ideas
#Could use the index to find things and store them in an array
def betterCalibrate(string):
    string  = string.lower()
    ans = ""
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    firstIndexVal = -2
    firstVal = ""
    for i in nums:
        if i in string:
            firstIndexVal = string.index(i)
            firstVal = i
            break
    lowestIndexVal = firstIndexVal
    lowestVal = firstVal
    
    for i in nums:
        if string.find(i) < lowestIndexVal and string.find(i) != -1:
            lowestIndexVal = string.find(i)
            lowestVal = i
            
    ans =  "" + str(returnInt(lowestVal))

    highestIndexVal = firstIndexVal
    highestVal = firstVal
    for i in nums:
        if string.rfind(str(i)) > highestIndexVal and string.rfind(i) != -1:
            highestIndexVal = string.rfind(i)
            highestVal = i
    ans = ans + str(returnInt(highestVal))
    return(ans)
    

values = []
file = open("input.txt", "r")
for line in file:
    values.append(int(betterCalibrate(line)))
print(sum(values))




