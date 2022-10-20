# 1부터 100까지 "제곱의 합"과 "합의 제곱"의 차는?
def square_sum(num):
    sum = 0
    for i in range(1, num+1):
        sum += i**2
    return sum

def sum_square(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    sum = sum**2
    return sum

def main():
    suqare_s = square_sum(100)
    sum_s = sum_square(100)
    print(sum_s - suqare_s)

if __name__ == "__main__":
	main()