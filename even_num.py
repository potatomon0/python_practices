even = 0
for n in range(1,10):
    if n%2==0:
        print(n)
        even += 1 
    else:
        continue
print(f"We have {even} even numbers")
