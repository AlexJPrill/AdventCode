import os
def main():
    file = fr'{os.path.dirname(os.path.abspath(__file__))}/input.txt'
    print(file)



if __name__=='__main__':
    main()