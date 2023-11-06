a = 5
st = ""
lst = []
for i in range(a + 1, 1, -1):
    if i == 0:
        break
    
    for j in range(a + 1, 1, -1):
        st = str(a) + st
        # print(st, str(a))
        raw = st[::-1]
        a = int(a) - 1
        lst.append(raw)
# print(st)
# print(lst)
newlst = lst[::-1]
# for i in lst:
#     print(i[::-1])
# print(newlst)
lst = []
for i in newlst:
    lst.append(i+i[::-1])

# print(lst)

for i in range(5):
    print(i* " ", lst[i])

    