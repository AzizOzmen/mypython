height = []
while True:
    num = input("Type 'ok' when you are done: ")
    if num != "ok":
        height.append(int(num))
    else:
        break
areas = 0
max_l = max_r = 0
l = 0
r = len(height)-1
while l < r:
    if height[l] < height[r]:
        if height[l] > max_l:
            max_l = height[l]
        else:
            areas += max_l - height[l]
        l += 1
    else:
        if height[r] > max_r:
            max_r = height[r]
        else:
            areas += max_r - height[r]
        r -= 1
print("\nRain-trapped area : ", areas)