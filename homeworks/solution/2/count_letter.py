tasks = []

def count_letter(letter):
    n = 0
    for task in tasks:
        word = task
        for lit in list(word):
            if lit == letter:
               n = n + 1
               print(word, n)
               break
    print(n)

# Добавляем слова
tasks.append("хлеб")
tasks.append("друг")
tasks.append("собака")
tasks.append("белка")

# Считаем количество слов с буквой
count_letter("а")