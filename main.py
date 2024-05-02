height = int(input(f"Enter the number of rows: "))
#Asterisk Triangle Generator
if height > 0:
    for i in range(1, height+1):
        print(i * "*")
else:
    print("please inter a postive Number.")