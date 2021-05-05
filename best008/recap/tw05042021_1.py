# ## Coding Challenge -1 : Validate Combination of Brackets

# Purpose of the this coding challenge is to solve a combination problem using loops.

# ### Learning Outcomes

# At the end of the this coding challenge, students will be able to;

# - understand the use of loops.
# - solve the advanced and complicated problems.
# - understand the importance of pattern recognition.
# - get a better understanding in manipulating lists or strings.

# ### Problem Statement
  
# - Write a function that given a string containing just the characters
#  `(`, `)`, `{`, `}`, `[` and `]`, 
# determines if the input string is valid or not by using following rules.

# - An input string is valid if:

#   - Open brackets must be closed by the same type of brackets.

#   - Open brackets must be closed in the correct order.

# - Note that an empty string is also considered valid.

# - Example for user inputs and respective outputs

# ```bash
# Input        Output
# --------:    ------:
# "()"         True
# "()[]{}"     True
# "(]"         False
# "([)]"       False
# "{[]}"       True
# ""           True
# ```

def is_valid(s):
  parantez={"(":")","[":"]","{":"}"}
  open_par =set(["(","[","{"])
  control_list=[]
  for i in s:
    if i in open_par:
      control_list.append(i)
    elif control_list and i ==parantez[control_list[-1]]:
      control_list.pop()
    else:
      return False
  return control_list==[]
print(is_valid('[]({}){'))