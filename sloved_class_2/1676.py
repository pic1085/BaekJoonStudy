N = int(input())
count = 0
Fact_N = 1

for i in range(1, N+1):
    Fact_N *= i

Fact_N = str(Fact_N)
for i in range(len(Fact_N)):
    if Fact_N[i] == '0':
        count += 1
print (count)