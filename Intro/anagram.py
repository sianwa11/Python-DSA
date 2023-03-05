# def anagramSolution1(s1,s2):
#     stillOK = True
#     if len(s1) != len(s2):
#         stillOK = False

#     alist = list(s2)
#     pos1 = 0

#     while pos1 < len(s1) and stillOK:
#         pos2 = 0
#         found = False
#         while pos2 < len(alist) and not found:
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1

#         if found:
#             alist[pos2] = None
#         else:
#             stillOK = False

#         pos1 = pos1 + 1

#     return stillOK

# print(anagramSolution1('abcd','dcba'))

c1 = [0]*26
c2 = [0]*26
s1 = 'apple'
s2 = 'pleap'
for i in range(len(s1)):
    pos = ord(s1[i])-ord('a')
    c1[pos] = c1[pos] + 1

for i in range(len(s2)):
      pos = ord(s2[i])-ord('a')
      c2[pos] = c2[pos] + 1
      
print(c1)
print(c2)