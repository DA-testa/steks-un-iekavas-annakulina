# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
          opening_brackets_stack.append(Bracket(next, i + 1)) 
            

        if next in ")]}":
          if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
            return i+1
          opening_brackets_stack.pop()
    if opening_brackets_stack:
      return opening_brackets_stack[0].position
    else:
      return "Success"

        


def main():
    text = input("Ievadiet F testiem vai I manuālai iekavu pārbaudei: ")
    if "F" in text:
      tests = input("Ievadiet 'test/' + variants no 0-5, piemēram test/0: ")
      if tests == "test/0" or tests == "test/1" or tests == "test/2" or tests == "test/3" or tests == "test/4" or tests == "test/5":
        with open(tests, "r") as f:
            text1 = f.read().strip()
            print(find_mismatch(text1))
      else:
        print("Tāda testa nav")  
    elif "I" in text:
      parbaude = input("Ievadiet iekavas: ")
      print(find_mismatch(parbaude))
    else:
        print("nepareiza komanda")

if __name__ == "__main__":
    main()
