#12. 500개 이상의 약수를 갖는 가장 작은 삼각수는?

def cal_triangle_num(seq) :
    num = 0
    arr = [num]
    for i in range(1, seq) :
        num += i
        arr.append(num)
    return arr

def cal_factors(triangle_num):
    factors = set([1, triangle_num])
    for i in range(2, triangle_num):
        if i in factors:
            return factors
        if triangle_num % 2 != 0: 
            break
        elif triangle_num % i == 0:
            factors.add(i)
            factors.add(triangle_num/i)
    return factors

def main():
    for triangle_num in cal_triangle_num(1000000):
        if len(cal_factors(triangle_num)) > 500:
            print(triangle_num)
            break

if __name__ == "__main__":
	main()