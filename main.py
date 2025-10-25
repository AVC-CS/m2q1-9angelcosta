def getPivot(number):
    avg = (number[0] + number[1] + number[2] + number[3] + number[4] + number[5]) // 5
    
    closenum = number[0]
    mindiff = number[0] - avg
    
    for num in number[1:]:
        difference = num - avg
        if difference < mindiff:
            mindiff = difference
            closenum = num   
    """
    ########################################
    Code Your Program here
    ########################################
    """

def split(number):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
