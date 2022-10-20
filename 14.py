#14. 백만 이하로 시작하는 우박수 중 가장 긴 과정을 거치는 것은?

from cgitb import reset


def calculate(num):
    count = 0
    while(num != 1):
        if num % 2 == 0:
            num= num / 2
        else:
            num = 3*num +1
        count += 1    
    return count

def main():
    arr = []
    for i in range(1, 1000001):
        arr.insert(i, calculate(i))
    result = max(arr)
    print(arr.index(result)+1)

if __name__ == "__main__":
	main()