# 사전 만들기
d = {
    "apple": "steve jobs"
    , "samsung": "je yong"
}

# 키가 없으면 오류가남
print(d["apple"])

# 키가 없어도 오류가안남
print(d.get("apple1", "--"))

# 키값들 가져오기
print(d.keys())

# value 값들 가져오기
print(d.values())

# key, value 형태로 가져오기
print(d.items())

# 값 꺼내오기 원본에서 가져와서 원본은 해당값 삭제된다
# print(d.pop("apple"))
# print(d)

# print(d.popitem())
# print(d)

# 사전에 값 추가하기
# d["new"] = "newValue"
d.update(new="abc")
print(d)

d.update({"new1": "abcd"})
print(d)

d1 = {"key1" : "value1" , "key2" : "value"}
d.update(d1)
print(d)

