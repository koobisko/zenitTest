hw = "5 5"

rows = [
    "10010",
    "10000",
    "00110",
    "10000",
    "01000"
]
print(rows)
heigth = int(hw.split(" ")[0])
width = int(hw.split(" ")[1])

rows = [list(map(int, row)) for row in rows]

holes = [0 for i in range(0, width)]


for row in range(0, heigth):
    for a in range(0, width):
        holeSize = 0
        hole = rows[row][a]
    
        if hole != -1:
            if hole == 0:
                holeSize += 1

                for b in range(a + 1, width):
                    if rows[row][b] == 0:
                        rows[row][b] = -1
                        holeSize += 1
                    else:
                        break

        if holeSize != 0:
            holes[holeSize - 1] += 1

for i in range(0, len(holes)):
    if holes[i] != 0:
        print(i + 1, holes[i])
