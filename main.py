def getPivot(number):
    total_sum = sum(number)
    avg = total_sum / len(number)
    
    pivot = number[0]
    mindiff = abs(number[0] - avg)
    
    for num in number[1:]:
        difference = abs(num - avg)
        if difference < mindiff:
            mindiff = difference
            pivot = num   
            
    return pivot
    

    
def split(number):
    left_sub = []
    right_sub = []
    middle = []
    
    for num in number:
        if num < pivot:
            left_sub.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right_sub.append(num)
    return left_sub + middle + right_sub
            


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
