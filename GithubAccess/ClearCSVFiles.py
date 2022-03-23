print("\nClearing data.csv...")
fileVariable = open('data.csv', 'r+')
fileVariable.truncate(0)
fileVariable.close()

print("Clearing user.csv...")
fileVariable = open('user.csv', 'r+')
fileVariable.truncate(0)
fileVariable.close()