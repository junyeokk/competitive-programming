def f(x):
    if x % 2 == 0: return x + 1
    
    # f-string을 사용해 문자 포맷팅, f''
    # f'0{}'은 2진수 값 앞에 0을 붙임. ex) 5 -> 0101
    x = f'0{bin(x)[2:]}' # 중괄호 안, 슬라이싱으로 순수하게 2진수 값만 남김
    
    # 10 왼쪽: 마지막 0이 나오기 이전의 비트들
    # 10 오른쪽: 마지막 0이 나오고 난 위치에서 2개 이후의 나머지 비트들
    x = f"{x[:x.rindex('0')]}10{x[x.rindex('0') + 2:]}"
    
    # 2진수 -> 10진수 변환
    return int(x, 2)

def solution(numbers):
    # 리스트 numbers의 각 요소 number에 대해 함수 f를 호출
    # 결과는 새로운 리스트로 만듬 (in numbers)
    return [f(number) for number in numbers]