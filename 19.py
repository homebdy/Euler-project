#19. 20세기에서, 매월 1일이 일요일인 경우는 몇 번?

def main():
    daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
    total=0
    count=0
    
    for y in range(1900,2001):
        for m in range(12):
            day=daylist[m]
            if y%4==0 and m==1: 
                day+=1
            for d in range(day):
                if y>1900 and d==0 and total%7==6:
                    count+=1
                total+=1
    print(count)

if __name__ == "__main__":
    main()