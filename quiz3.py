url = "http://naver.com"
rule1 = url.replace("http://", "")
rule1 = rule1[:rule1.index(".")]

rule_2 = rule_1[:rule_1.index('.')]

password = rule_2[: 3] + str(len(rule_2)) + str(rule_2.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(site, password))