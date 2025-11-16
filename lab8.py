# Program Name: Lab8
# Course: IT1114
# Student Name: Laydix Roblero
# Assignment Number: Lab8
# Due Date: 10/25/25
# Purpose: What does the program do? creating two list (length N)
#filled with random integers between 0-500.Combine them into a third list
#containing only distinct values.
#Print the contents of the final list, one number per line 
# List specific resources used to complete? Python doc: random.radiant and powerpoints

import random

def read_positive_int_greater_than_one(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("please enter a whole number greater than 1.")
            continue
        n= int(raw)
        if n <= 1:
            print("N must be greater than 1.")
            continue
        return n

def make_random_list(length: int, low: int = 0, high: int = 500)-> list[int]:
   lst = []
   for _ in range(length):
        lst.append(random.randint(low, high))
   return lst
def combine_distinct(a: list[int], b: list[int])->list[int]:
    c = []
    for value in a + b:
        if value not in c:
            c.append(value)
    return c

def main():
    n = read_positive_int_greater_than_one("Enter N (>1): ")
    a = make_random_list(n,0,500)
    b = make_random_list(n,0,500)
    c = combine_distinct(a,b)

    for number in c:
        print(number)

if __name__=="__main__":
    main()
