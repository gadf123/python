import copy
import functools

# 어떠한 형식도 같이 배열안에 들어갈수있다
# l1 = [1, "1", [], []]
# l1 = [1, 2, 3, 1]
# 리스트 맨 끝에 요소 추가
# l1.append("F")

# 지정한 곳에 해당 문자열을 넣어준다
# l1.insert(1,"F")
# print(l1)

# 리스트 맨 끝에 요소 꺼내온다
# !! 꺼내온 후에 맨 끝에 요소를 삭제한다
# print(l1.pop())
# print(l1)
#
# #슬라이싱 가능
# print(l1[0:2])
#
# # 해당 문자열이 리스트에 존재하는지
# print(l1.index(2))
#
# # 해당 문자열이 리스트에 몇개가 존재하는지
# print(l1.count(1))

# #안에 있는 값을 다 삭제한다
# l1.clear()
# print(l1)

# 배열 복사 해준다 부모를 컨트롤하면 자식까지 영향을 받는다 반대로 하면 영향 안받음
# l2=l1.copy()
# l1.clear()
# print(l1)
# print(l2)

# 배열 복사 해준다 부모를 컨트롤하면 자식까지 영향을 받는다 반대로 하면 영향 안받음
# l2 = copy.deepcopy(l1)
# l1.clear()
# print(l1)
# print(l2)

# 리스트 통합 해주는거
# l2 = [4, 6, 8]
# print(l1 + l2)
# print(l1)
#
# #똑같은 급으로 통합
# l1.extend([4, 6, 8])
# print(l1)

# 지우는거
# l1.remove(1)
# print(l1)

# # 거꾸로 돌리는거
# l1.reverse()
# print(l1)
#
# # 정렬해주는거
# print(l1.sort())
# print(l1)
# l1.sort(reverse=True)
# print(l1)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1)
l1 = [i * 2 for i in l1]
print(l1)

print(functools.reduce(lambda x, y: x * y, l1))
