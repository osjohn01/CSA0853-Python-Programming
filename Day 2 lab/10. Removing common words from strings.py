s1=(input("ENTER STRING 1 --> ")).split()
s2=(input("ENTER STRING 2 --> ")).split()
for i in s1:
    if i in s2:
        s2.remove(i)
        s1.remove(i)
print(" ".join(s1))
print(" ".join(s2))
