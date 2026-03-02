#WordIndex.py
#Name: Kansas Nygaard
#Date: 03/01/26
#Assignment: Lab 6

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  lineNumber = 0 
  for line in textFile:
    lineNumber = lineNumber + 1
    line = line.lower()
    wordList = line.split()
    for word in wordList:
      if word in words:
        words[word].append(lineNumber)
      else:
        words[word] = [lineNumber]
  print("Word Index:")
  for word in words:
    print(word, ":", words[word])


if __name__ == '__main__':
  main()
