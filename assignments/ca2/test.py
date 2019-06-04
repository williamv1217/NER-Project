words = []
with open('wpFreq', 'r') as f:
    for line in f:
        words.append(line.split())
# print(words)


pps = []
with open('pFreq', 'r') as f:
    for line in f:
        pps.append(line.split())

print(pps)

for x in pps:
    if len(x) == 2:
        print(x[1])

# for x in words:
#     if len(x) == 3:
#         print(x[2])
# print(words)
#
# x2 = []
#
for w in words:
    if len(w) == 3:
        count = w[2]