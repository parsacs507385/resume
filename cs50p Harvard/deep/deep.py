ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()
ans = ans.replace("forty two", "42").replace("forty-two", "42")
if ans == "42" or ans == 42:
    ans = 42
if ans != 42:
    ans = 0
ans = int(ans)

if ans == 42:
    print("Yes")
else:
    print("No")
