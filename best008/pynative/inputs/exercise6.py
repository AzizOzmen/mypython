a = ["line1", "line2", "line3", "line4", "line5", "line6", "line7"]
for i in a:
    if i == "line5":
        continue 
    print(i)

print("----")
count = 0
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    count = len(lines)
with open("newFile.txt", "w") as fp:
    for line in lines:
        if (count == 3):
            count -= 1
            continue
        else:
            fp.write(line)
        count-=1