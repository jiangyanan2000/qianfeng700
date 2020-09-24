# s1 = input("请输入第一个单词：")
# s2 = input("请输入第二个单词：")
# #
#
# for i in s2:
#     if i in s1:
#         s1 = s1.split(i)
#         s1 = "".join(s1)
#
# print(s1)

word1 = input("please input the word:")
n = len(word1)
for i in range(n-1):
    if word1[i] == word1[i+1]:
        print("xiaoyi dont like this word!")
        break
else:
    print("xiaoyi like this word!")

# for i in s2:
#     s1 = s1.replace(i,"")
# print(s1)