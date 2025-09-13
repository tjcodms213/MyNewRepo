# Greatest Common Divisor algorithm
def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# 함수 사용 예시
if __name__ == "__main__":
    num1 = 60
    num2 = 24
    result = gcd_euclidean(num1, num2)
    print(f"{num1}과 {num2}의 최대공약수는 {result}입니다.") # 출력: 60과 24의 최대공약수는 12입니다.
