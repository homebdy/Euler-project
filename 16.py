# 2^1000의 각 자릿수를 모두 더하면?
def main():
    num = 2**1000
    s_num = str(num)
    sum = 0
    for i in range(len(s_num)):
        sum += int(s_num[i])
    print(sum)

if __name__ == "__main__":
	main()