import random

# 入力を受け取る
sides = int(input("サイコロの面の数は?: "))
round = int(input("何回振りますか?: "))

# サイコロを振る
results = [random.randint(1, sides) for _ in range(round)]

# 結果を表示
print(results)

