# 숫자는 0이면 거짓이다
# 문자는 공백이면 거짓이다

t = 0
b = 0

if not (t or b):
    print(True)

# 삼항연산자
    t = 0
    ps1 = t or "printable"
    print(ps1)

    t = 2;
    if t == 1:
        print(1)
    elif t == 3:
        print(3)
    else:
        print("else")

bcd = 0
kosta = "python" if bcd == 1 else"java"
print(kosta)
