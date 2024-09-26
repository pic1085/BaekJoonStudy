N = int(input())
count = 0
Fact_N = 1
Fact_len = 0

for i in range(1, N+1):
    Fact_N *= i

Fact_N = str(Fact_N)
Fact_len = len(Fact_N)

for i in range(0, Fact_len):
    if Fact_N[Fact_len - i - 1] == '0':
        count += 1
    else:
        break
print (count)