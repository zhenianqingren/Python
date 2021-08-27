# 缩进相当于{} 规定了代码的层次

# 字符串的序号 正向递增序号和反向递减序号
# 索引：返回字符串中的单个字符 例如 TempStr[0](请) TempStr[-1](:)
# 切片：返回字符串的字串 <字符串>[M:N]返回的是索引[M,N)的一段字串 （即不取<字符串>[N]）

# 列表：使用[]表示，用,分割元素 使用in判断一个元素是否在列表中

# if elif else 条件的末尾要加:

# input()从控制台获得用户输入的函数 括号内可以输入提示信息，提示信息并不作为变量的一部分
# 在print()中，{}表示槽，后续变量填充到槽中，{:.2f}表示将变量C填充到这个位置时取小数点后两位
# 评估函数 eval(<字符串或字符串变量>)去掉参数最外层引号并执行余下语句 例：eval('print("HelloWorld")')



TempStr =input("请输入带有符号的温度值:")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")