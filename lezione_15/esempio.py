PATH : str = "lezione_15/esempio.txt"
mode : str = "r"
encoding : str = "utf-8"

file = open(PATH)

print(file)

output: str = file.read()

print(output)