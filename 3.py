# 3. 가장 큰 소인수 찾기
def smallest_prime(num):
    i=1
    while i < num:
        if num % i == 0:
            num = num/i
        i = i+1
    return int(num)

def main():
    n = int(input("수를 입력하시오: "))
    print(smallest_prime(n))

if __name__ == "__main__":
	main()