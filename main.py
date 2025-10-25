def getPivot(number):
    avg = (number[0] + number[1] + number[2] + number[3] + number[4] + number[5]) // 5
    
    pivot = number[0]
    mindiff = number[0] - avg
    
    for num in number[1:]:
        difference = num - avg
        if difference < mindiff:
            mindiff = difference
            pivot = num   
            
    return pivot
    
left_sublist = []
right_sublist = []
    
def split(number):
    for x in number[1:]:
        if x <= pivot:
            left_sublist.append(x)
        else:
            right_sublist.append(x)
            
    new_list = left_sublist + pivot + right_sublist
    return new_list
            
    
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
