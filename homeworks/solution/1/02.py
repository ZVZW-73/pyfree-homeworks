number = 3
data=[str,str,str]
problem=[str,str,str]
for i in range(number):
    data[i]=input("Введите дату:");
    problem[i]=input("Введите задачу:")
for i in range(number):
    print(data[i], " ", problem[i])