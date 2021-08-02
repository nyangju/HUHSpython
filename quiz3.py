url = "http://naver.com"
rule1 = url.replace("http://", "")
rule1 = rule1[:rule1.index(".")]
# print(rule1)
rule2 = rule1[:3] + str(len(rule1)) + str(rule1.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url , rule2))