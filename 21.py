def sum_of_divisors(n: int):
    s = 1
    i = 2
    l = int(n ** 0.5)
    while i <= l:
        if n % i == 0:
            s += i + n // i
        i += 1
    if l * l == n:
        s -= l
    return s

def find_friend_number(n:int):
    k = sum_of_divisors(n)
    if k != n and sum_of_divisors(k) == n:
        return k
    return None

def sum_digit(num):
    num = str(num)
    sum = 0
    for n in num:
        sum += int(n)
    return sum

def main():
    result = set()
    for i in range(2, 10001):
        j = find_friend_number(i)
        if j is not None:
            result.add(i)
            result.add(j)
    
    s = sum(result)
    print("친화수의 합: ", s)
    print("각 자리수 합: ", sum_digit(s))

if __name__ == "__main__":
    main()