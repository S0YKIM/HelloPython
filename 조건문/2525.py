#[2525]조건문, 오븐시계

a, b=map(int, input().split()) #현재 시각
c=int(input()) #요리하는 데 걸리는 시간

a += c // 60 #요리 시간을 받아와 시와 분으로 나눠 각각에 더해준다.
b += c % 60

if b>=60: # B(분) 값이 60이 넘어가면 A(시)에 1을 더해주고, B(분)에 60을 뺀다.
    a+=1
    b-=60
    
if a>=24: #23시 59분에서 1분이 지나면 0시 0분이 되는 부분을 처리하기 위해 A(시)가 24와 같거나 커지면 24를 빼준다.
    a-=24
    
print('%d %d'%(a,b)) #%d : 정수 