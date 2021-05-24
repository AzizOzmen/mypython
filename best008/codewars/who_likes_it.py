def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
    
print(likes(["Alex", "Jacob", "Mark", "Max","Alex", "Jacob", "Mark", "Max"]))
#-----------------------------------
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

print(likes(["Alex", "Jacob", "Mark", "Max","Alex", "Jacob", "Mark", "Max"]))
#-----------------------------------
def likes(input):
    if bool(input) == 0:
        print("no one likes this")
    elif len(input) == 1:
        print(input[0], "likes this")
    elif len(input) == 2:
        print(input[0], "and", input[1], "like this")
    elif len(input) == 3:
        print(input[0],input[1], "and", input[2], "like this")
    else:
        print(input[0] + ",", input[1],  "and", (len(input) - 2), "others like this")

likes(["Alex", "Jacob", "Mark", "Max","Alex", "Jacob", "Mark", "Max"])