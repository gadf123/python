# i = 1
# j = 4
#
# print(i + j)
# print(i - j)
# print(i * j)
# # 실수 나눗셈
# print(i / j)
#
# # 정수형 나눗셈
# print(i // j)
#
# print(i * j)
# print(i * j)
#
# # 정수형 나눗셈만 처리한다
# # 실수형은 지원하지 않는다
# print(divmod(i, j))
#
# # 파이썬 에서는 문자가 하나이건 두개이건 문자열로 인식한다
# s = "Hello Python"
# s1 = 'Hello Guido Van Rossum'
#
# s = "I'm"
# s1 = '오늘은 "날씨가 좋아요"'
#
# s = "오늘은 \"강조\"해야 합니다"
# #s = "한아국오은나살가기자좋사은이나감라사가고됐두어에요"
# # 파이썬은 한글이건 영문이건 순서로대로 접근한다
# # 일부 타 언어에서는
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
#
# print(len(s))
#
# # 슬라이싱 방법
# print(s[0:7])
# print(s[0:6])
# print(s[:7])
# print(s[:6])
#
# #s[startValue : endValue : 건너뛰는값]
# print(s[0::2])
#
# print(s[::-1])
# print(s[::-2])
# print(s[::-3])

# print(s.replace(s[5],"123"))

# s = "Hello %s %s"
# print(s % ("abc","dcd"))
# print(s % (11,1.3))

## 문자열 받는거
# s = "Hello {1} {0}"
# print(s.format("abc", 45))
#
# s = "Hello {0} {1}"
# print(s.format("abc", 45))
#
# s = "Hello {} {}"
# print(s.format("abc", 45))
#
# #안에 들어가있는 메소드 들을 보여준다
# print(dir(s))
#
# #100 자 안에 가운데 위치해준다
# print(s.center(100))
# print(s.center(100,"*"))


# s = "Hello {0} {1}"

# print(s.count('l'))
# print(s.count(' '))

#파이썬 에서 서버를 통해 밖으로 나갈경우 반드시 utf-8로 변경해야한다
#3.XX 대 버전 부터 한국어 인코딩 안해줌그래서 꼭 해야함!
s = "한국"

#인코딩 된것은 바이트 데이터 타입으로 넘어온다!
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

b = s.encode('euc-kr')
print(b)
print(b.decode('euc-kr'))




