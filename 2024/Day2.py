

if __name__ == "__main__":
    with open('input.txt') as file:
        data = file.read().splitlines()
    instructions = []
    for x in data:
        instructions.append(data.split())
    print(instructions)
    instructions = [int(x) for x in instructions]
    ans = len(instructions)
    for i in data:
        j = 0
        while j < len(i) -1:
            if not(i[j] < i[j+1]) and not((i[j+1]-3) <= i[j]):
                ans -= 1
                continue
            else:
                j+=1
    print(ans)
