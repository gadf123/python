# i = 1
# j = 4

# print(i + j)
# print(i - j)
# print(i * j)
# # 실수 나눗셈
# print(i / j)

# # 정수형 나눗셈
# print(i // j)

# print(i * j)
# print(i * j)

# # 정수형 나눗셈만 처리한다
# # 실수형은 지원하지 않는다
# print(divmod(i, j))

# # 파이썬 에서는 문자가 하나이건 두개이건 문자열로 인식한다
# s = "Hello Python"
# s1 = 'Hello Guido Van Rossum'

# s = "I'm"
# s1 = '오늘은 "날씨가 좋아요"'

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

# print(len(s))

# # 슬라이싱 방법
# print(s[0:7])
# print(s[0:6])
# print(s[:7])
# print(s[:6])

# #s[startValue : endValue : 건너뛰는값]
# print(s[0::2])

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

# s = "Hello {0} {1}"
# print(s.format("abc", 45))

# s = "Hello {} {}"
# print(s.format("abc", 45))

# #안에 들어가있는 메소드 들을 보여준다
# print(dir(s))

# #100 자 안에 가운데 위치해준다
# print(s.center(100))
# print(s.center(100,"*"))


# s = "Hello {0} {1}"

# print(s.count('l'))
# print(s.count(' '))

# 파이썬 에서 서버를 통해 밖으로 나갈경우 반드시 utf-8로 변경해야한다
# 3.XX 대 버전 부터 한국어 인코딩 안해줌그래서 꼭 해야함!
# s = "한국"

# 인코딩 된것은 바이트 데이터 타입으로 넘어온다!
# b = s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))

# b = s.encode('euc-kr')
# print(b)
# print(b.decode('euc-kr'))


# s = "한국사 한국사 한국사"
# #어떤 문자로 시작하는지
# print(s.startswith("한"))

# #어떤 문자로 종료되는지
# print(s.endswith("국"))

# #몇번째에 위치하고있는지
# print(s.find("한"))
# 두번째 위치하고 있는애 찾기
# print(s.find(" ",s.find(" ")+1))

# #몇번째에 위치하고있는지
# print(s.index("한"))

# s = "AaaA"

# # 알파벳 또는 숫자로 구성 되어있는지 확인하는 메소드
# print(s.isalnum());
# # 알파벳 인지만 확인
# print(s.isalpha());
# # 숫자 인지만 확인
# print(s.isdecimal());
# print(s.isdigit());

# # 변수 이름으로 사용할수 있는지
# print(s.isidentifier());

# # 소문자로만 구성되어있는지
# print(s.islower())
# # 대문자로만 구성되어있는지
# print(s.isupper())

# # 화면상에 출력할수 있는지 확인하는 함수
# print(s.isprintable())

# # 소문자변환
# print(s.lower())
# # 대문자변환
# print(s.upper())

# s = '           AaaA             '
# # 양쪽 공백제거
# print(s.strip())
# # 왼쪽 공백제거
# print(s.lstrip())
# # 오른쪽 공백 제거
# print(s.rstrip())

# s = '1|2|3|4|5'
# print(s.split("|"))
# print(s.split("|", 3))

# s = """가
# 나
# 다
# 라
# 마
# 바사
# """
# print(s.splitlines())

# s = "한국은\n좋은나라\n503은 무기징역\n음.. 다른사람은?"
# s1 = s.splitlines()
# print(s1)
# #배열을 특정 문자열로 잘라 문자열로 만든다
# print(",".join(s1))

# s = "한국은\n좋은나라\n503은 무기징역\n음.. 다른사람은?"
# print(s.replace("은","가"))

s = "22"
print(s.zfill(5))
