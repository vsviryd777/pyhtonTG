"""
Volha Svirydzenka,lab8.2
Write a modular python program that asks the user to enter a series of single-digit numbers as a string of any length 
with nothing separating the numbers.
The program should then display the sum of all the single digit numbers in the string.
For example, if 2514 is input, program should return 12, the sum of 2, 5, 1 and 4.
Keep the program running until told to stop by user input.
"""

def main():
    try:
# ask user enter his numbers
        numbers = request()
        total = 0
# read each digit by index number.
        index = 0
        while index < len(numbers):
            total += int(numbers[index])
            index += 1

        print("The sum of your numbers ",numbers, "is", total)

# exception if enter letters or whitespace
    except ValueError:
        print("Enter ONLY numbers and without whitespace. Try again!")
        main()
    restart()
# ask user enter his numbers
def request():
    numbers = input("Enter your  numbers without whitespace.(Example: 1598 ): ")
    return numbers

def restart():
  again = input("Would you like enter new numbers again? Enter (y or n):  ").lower()
  if again == "y":
      main()
  else:
      print('Goodbye. The program exit.')

# call the main function
main()