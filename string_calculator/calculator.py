import re
regex = re.compile(r'\d+') # add one or more digits def negatives_number(string):

def negatives_number(string):
    empty_string = ''
    for x in range(len(string)):
        if string[x] == '-' and string[x+1].isdecimal():
            empty_string += '-' + string[x+1] + ','
        return empty_string


def add(string):
    sum = 0
    numbers = regex.findall(string) # this line is telling the program to find all the regular expressions
    negatives = negatives_number(string)
    try:
        string[:-1]
    except:
        raise "This is not okay!"
    if negatives:
        raise Exception("Oops! Negative numbers are not allowed: " + negatives)
    if string == '':
        return 0
    else:
        for x in numbers:
            if int(x) > 30:
                pass
        
            else:
                num = int(x)
                sum += num
        return sum
print(add("//[***]\n7***2***1000")) #This should print only 9 and ignore 1000 integer
