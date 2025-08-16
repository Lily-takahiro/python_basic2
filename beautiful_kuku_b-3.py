
rows = int(input("行数を入力してください:"))
cols = int(input("列数を入力してください:"))


for j in range(1, rows + 1):  # 行（左側の数）
    for i in range(1, cols + 1):  # 列（右側の数）
        print(f"{i} x {j} = {i*j:2}", end=" | ")
    print()  # 改行

