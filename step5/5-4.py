#3052 나머지
e = [] #나머지들을 모을 공간배열을 먼저 만들기

for i in range(10):  #10번 반복
     n=int(input()) #숫자 입력
     e.append(n%42) #42로 나눈 난머지들 넣기

e = set(e) #나머지가 든 배열 e를 set으로 집합 자료형으로 만들어주기

print(len(e)) # 서로 다른 나머지가 몇 개 있는지 집합 자료형의 길이로 출력하여 알 수 있음
     