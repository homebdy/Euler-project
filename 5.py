# 5. 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
def gcd(num1, num2):
    i=1
    gcd = 1
    while i < num2:
        if num1%i==0 and num2%i==0:
            gcd=i
        i+=1
    return gcd

def main():
    n = int(input())
    res = 1
    for i in range(1, n+1):
        res *= i//gcd(i, res)
    print(res)

if __name__ == "__main__":
	main()