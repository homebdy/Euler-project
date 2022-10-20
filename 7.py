#6. 10001번째 소수를 구해라.
import math
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def main():
    num = 2
    count = 0
    while(True):
        if is_prime(num):
            count += 1      
        if(count == 10001):
            print(num)
            break
        num +=1

if __name__ == "__main__":
	main()