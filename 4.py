# 4. 세자리 수를 곱해 만들 수 있는 가장 큰 대칭수

def main():
    arr = [i*j for i in range(100, 1000) for j in range(100, 1000) if str(i*j) == str(i * j)[::-1]]
    print(max(arr))

if __name__ == "__main__":
	main()