text = list(input())
if text[-1] == "s":
    text.append("es")
    print("".join(text))
else:
    text.append("s")
    print("".join(text))