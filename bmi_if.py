weight = input('請輸入體重(kg): ')
height = input('請輸入身高(cm): ')
weight = float(weight)
height = float(height)

bmi = weight / height ^ 2
# 過輕 正常 過重 輕度肥胖 中度肥胖 重度肥胖
if bmi < 18.5:
    print('過輕')
elif bmi < 24:
    print('正常')
elif bmi < 27:
    print('過重')
elif bmi < 30:
    print('輕度肥胖')
elif bmi < 35:
    print('中度肥胖')
else:
    print('重度肥胖')    