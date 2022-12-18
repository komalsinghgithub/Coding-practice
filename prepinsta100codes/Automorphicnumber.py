n = int(input( ))
print("YES" if int(str(n**2)[-len(str(n))::]) == n else "No")