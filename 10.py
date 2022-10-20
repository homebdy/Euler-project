#10. 이백만 이하 소수의 합
import math

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def main():
    sum = 0
    for i in range(1,2000000):
        if is_prime(i):
            sum += i
    print(sum)

if __name__ == "__main__":
	main()