# 20. 100! 의 자릿수를 모두 더하면?
def factorial(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f

def main():
    num = factorial(100)
    s_num = str(num)
    sum = 0
    for i in s_num:
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()