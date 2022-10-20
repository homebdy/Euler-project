# 15. 20×20 격자의 좌상단에서 우하단으로 가는 경로의 수

def factorial(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f

def main():
    a,b= 20, 20
    print(int(factorial(a+b)/(factorial(a)*factorial(b))))

if __name__ == "__main__":
	main()