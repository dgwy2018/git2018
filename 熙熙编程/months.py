7months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份数(1-12):")
pos = (int(n)-1)*3
monthAbbrve = months[pos:pos+3]
print("月份简写是"+monthAbbrve+".")
4