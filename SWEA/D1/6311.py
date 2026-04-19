code = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
sum_num = 0

print(sum(map(lambda x: sum_num + 4 if x == 'A' else sum_num + 3 if x == 'B' else sum_num + 2 if x == 'C' else sum_num + 1, code)))
