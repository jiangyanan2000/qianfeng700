s = "张三19345943493493李四39534953943x王五4594549549594x柳柳638434834阿里啊53954359牛逼的34463啊哈哈3959姜亚南3383573843发粑粑353534阿里35353"
# print(s)
s1 = s + "你好"
n = len(s1)
while True:
    for i in range(n-1):
        if (s1[i].isdigit() or s1[i] == "x") and not s1[i+1].encode("utf-8").isalnum():
            t = s1[:i+1]
            s1 = s1[i+1:]
            print(t)
            # print(i)
            n = len(s1)

            break
        # else:
        #     print(s)




