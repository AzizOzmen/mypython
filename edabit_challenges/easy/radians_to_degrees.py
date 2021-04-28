# Create a function that takes an angle in radians 
# and returns the corresponding angle 
# in degrees rounded to one decimal place.

# Examples
# radians_to_degrees(1) ➞ 57.3
# radians_to_degrees(20) ➞ 1145.9
# radians_to_degrees(50) ➞ 2864.8

# 1.
def radians_to_degrees(radians):
    degrees = radians*57.2958
    print("{:.1f}".format(degrees))  # Print do not return value
    # print("%.1f" % degrees)  #  % Print do not retun value
    # print(round(degrees, 1))  # Round function

radians_to_degrees(1)
radians_to_degrees(20)
radians_to_degrees(50)

print("----")

# 2.
import math
def radians_to_degrees(rad):
	print(round(math.degrees(rad),1))  #with round function

radians_to_degrees(1)
radians_to_degrees(20)
radians_to_degrees(50)
