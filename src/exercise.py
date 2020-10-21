def main():
    #write your code below this line
    intList = []
    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)
    sum = 0
    for i in range(len(intList)):
      sum+=intList[i]
    print("Sum: %s"%sum)
if __name__ == '__main__':
    main()
