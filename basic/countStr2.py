def count_str(statement):
    print(f"The sentence is: {statement}")
    count = 0
    for i in range(len(statement)-1):
        count = count + statement[i: i+6] == 'Starla'
        return count
count = count_str("Starla is a good developer")
print(f"Starla appeared {count} times")