# a + b + c = 1000이 되는 피타고라스 수

def main():
    num = 1000
    for a in range(1, num+1):
        for b in range(a+1, num+1):
            c = num - a - b
            if a*a + b*b == c*c:
                print(a*b*c)

if __name__ == "__main__":
	main()