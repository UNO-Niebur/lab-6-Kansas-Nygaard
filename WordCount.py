#WordCount.py
#Name: Kansas Nygaard
#Date: 03/01/26
#Assignment: Lab 5

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  charCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    charCount = charCount + len(line) # count characters
    words = line.split()
    wordCount = wordCount + len(words)
    
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", charCount)
  

if __name__ == '__main__':
  main()
