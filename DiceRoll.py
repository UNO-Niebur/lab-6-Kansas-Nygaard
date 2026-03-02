#DiceRoll.py
#Name: Kansas Nygaard
#Date: 03/01/26
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for i in range(10000):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2 #find the sum total of the two dice
    rolls[total - 2] = rolls[total - 2] + 1 #update counts
  
  #print statictics for dice rolls
  print("Dice Roll Statistics: ")
  percent_total = 0
  for i in range(11):
    percent = (rolls[i] / 10000) * 100
    percent_total = percent_total + percent
    print("Sum of", i + 2, ":", percent, "%")
  print("Total Percent:", percent_total, "%")


if __name__ == '__main__':
  main()
