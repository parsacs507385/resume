total = input("How much was the meal? ")
total = total.replace("$", "")
total = float(total)

perc = input("What percentage would you like to tip? ")
perc = perc.replace("%", "")
perc = int(perc)

ans = (perc/100) * (total)
ans = "{0:.2f}".format(ans)
print(f"${ans}", end="")
