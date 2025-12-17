from emoji import emojize

inp = input("Input: ").strip()
res = emojize(inp, language="alias")

print(f"Output: {res}")
