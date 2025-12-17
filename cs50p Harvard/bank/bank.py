ans = input("Greetings: ").strip().lower()
ret = 100

if ans[0] == "h":
    ret = 20
if ans[0:5] == "hello":
    ret = 0

print(f"${ret}")
