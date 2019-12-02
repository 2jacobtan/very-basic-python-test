#given in email

"""
Python Test
1.Given a number and reverse it. For example:
a. Input 123 , output 321
b. Input 321, output 123
c. Input -456, output -654
d. Input 120, output 21
2.Check if a list contains duplicated element, if has return True.For example:
a. [0, 1, 1, 2], return True
b. [0, 1, 2], return False
"""

import re
from typing import List,Tuple,Any

# Question 1

## solution function
def reverse_str(num: int) -> int:
  return_str = ""
  if num<0:
    return_str += '-'
    num = abs(num)
  num_string = str(num)
  return_str += num_string[::-1]
  return int(return_str)

## copy-pasta
raw_text_1 = """a. Input 123 , output 321
b. Input 321, output 123
c. Input -456, output -654
d. Input 120, output 21""".splitlines()
## generate test cases
test_cases_1: List[Tuple] = []
for i,line in enumerate(raw_text_1):
  print(f"processing line {i}…")
  match = re.findall(r"-?\d+",line)
  assert len(match) == 2, f"invalid number of matches per line: {len(match)}"
  test_cases_1.append(tuple(map(int,match)))
for t in test_cases_1:
  print(t)

## testing
print("__Given Goal Output__")
for given,goal in test_cases_1:
  output = reverse_str(given)
  assert output == goal
  print(given, goal, output)

print("*** End of question 1. ***\n")

# Question 2

## solution function
def has_duplicate(list1: List[Any]) -> bool:
  encountered = set()
  for item in list1:
    if item in encountered:
      return True
    encountered.add(item)
  return False

## test cases
test_cases_2: List[Tuple] = [
  ([0, 1, 1, 2],True),
  ([0, 1, 2],False)
]
## testing
print("__Given Goal Output__")
for given,goal in test_cases_2:
  output = has_duplicate(given)
  assert output == goal
  print(given, goal, output)

print("*** End of question 2. ***\n")
