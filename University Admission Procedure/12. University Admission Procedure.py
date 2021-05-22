full_lt = []
applicants_lt = []
biotech = []
engineering = []
chemistry = []
mathematics = []
physics = []

accepted = int(input())

with open("applicants.txt", "r") as f:
    for i in f:
        name, surname, phy, che, math, cs, spe, choice1, choice2, choice3 = i.split()
        applicants_lt.append([name + " " + surname, float(phy), float(che), float(math), float(cs), float(spe), choice1, choice2, choice3])
        full_lt.append([name + " " + surname])

    # applicants_lt.sort(key=lambda x: (-x[1], x[2], x[3], x[4], x[0]))

    for i in range(6, 9):
        for j in sorted(applicants_lt, key=lambda x: (min((-(x[2] + x[1]) / 2), -x[5]), x[0])):
            if j[i] == "Biotech" and j[:1] in full_lt and j[5] <= ((j[2] + j[1]) / 2):
                if len(biotech) == accepted:
                    continue
                lt = [j[0], ((j[1] + j[2]) / 2)]
                biotech.append(lt)
                full_lt.remove(j[:1])
            elif j[i] == "Biotech" and j[:1] in full_lt and j[5] > ((j[2] + j[1]) / 2):
                if len(biotech) == accepted:
                    continue
                lt = [j[0], j[5]]
                biotech.append(lt)
                full_lt.remove(j[:1])

        for j in sorted(applicants_lt, key=lambda x: (min((-(x[3] + x[4]) / 2), -x[5]), x[0])):
            if j[i] == "Engineering" and j[:1] in full_lt and j[5] <= ((j[3] + j[4]) / 2):
                if len(engineering) == accepted:
                    continue
                lt = [j[0], ((j[3] + j[4]) / 2)]
                engineering.append(lt)
                full_lt.remove(j[:1])
            elif j[i] == "Engineering" and j[:1] in full_lt and j[5] > ((j[3] + j[4]) / 2):
                if len(engineering) == accepted:
                    continue
                lt = [j[0], j[5]]
                engineering.append(lt)
                full_lt.remove(j[:1])

        for j in sorted(applicants_lt, key=lambda x: (min(-x[2], -x[5]), x[0])):
            if j[i] == "Chemistry" and j[:1] in full_lt and j[2] < j[5]:
                if len(chemistry) == accepted:
                    continue
                lt = [j[0], j[5]]
                chemistry.append(lt)
                full_lt.remove(j[:1])
            elif j[i] == "Chemistry" and j[:1] in full_lt and j[2] >= j[5]:
                if len(chemistry) == accepted:
                    continue
                lt = [j[0], j[2]]
                chemistry.append(lt)
                full_lt.remove(j[:1])

        for j in sorted(applicants_lt, key=lambda x: (min(-x[3], -x[5]), x[0])):
            if j[i] == "Mathematics" and j[:1] in full_lt and j[5] <= j[3]:
                if len(mathematics) == accepted:
                    continue
                lt = [j[0], j[3]]
                mathematics.append(lt)
                full_lt.remove(j[:1])
            elif j[i] == "Mathematics" and j[:1] in full_lt and j[5] > j[3]:
                if len(mathematics) == accepted:
                    continue
                lt = [j[0], j[5]]
                mathematics.append(lt)
                full_lt.remove(j[:1])

        for j in sorted(applicants_lt, key=lambda x: (min((-(x[3] + x[1]) / 2), -x[5]), x[0])):
            if j[i] == "Physics" and j[:1] in full_lt and j[5] <= ((j[3] + j[1]) / 2):
                if len(physics) == accepted:
                    continue
                lt = [j[0], ((j[3] + j[1]) / 2)]
                physics.append(lt)
                full_lt.remove(j[:1])
            elif j[i] == "Physics" and j[:1] in full_lt and j[5] > ((j[3] + j[1]) / 2):
                if len(physics) == accepted:
                    continue
                lt = [j[0], j[5]]
                physics.append(lt)
                full_lt.remove(j[:1])

biotech.sort(key=lambda x: (-x[1], x[0]))
chemistry.sort(key=lambda x: (-x[1], x[0]))
engineering.sort(key=lambda x: (-x[1], x[0]))
mathematics.sort(key=lambda x: (-x[1], x[0]))
physics.sort(key=lambda x: (-x[1], x[0]))

print("Biotech")
for i in biotech:
    print(i[0], i[1])

print("\nChemistry")
for i in chemistry:
    print(i[0], i[1])

print("\nEngineering")
for i in engineering:
    print(i[0], i[1])

print("\nMathematics")
for i in mathematics:
    print(i[0], i[1])

print("\nPhysics")
for i in physics:
    print(i[0], i[1])

with open("biotech.txt", "w") as f:
    for i in biotech:
        text = f"{i[0]} {i[1]}\n"
        f.write(text)

with open("engineering.txt", "w") as f:
    for i in engineering:
        text = f"{i[0]} {i[1]}\n"
        f.write(text)

with open("mathematics.txt", "w") as f:
    for i in mathematics:
        text = f"{i[0]} {i[1]}\n"
        f.write(text)

with open("chemistry.txt", "w") as f:
    for i in chemistry:
        text = f"{i[0]} {i[1]}\n"
        f.write(text)

with open("physics.txt", "w") as f:
    for i in physics:
        text = f"{i[0]} {i[1]}\n"
        f.write(text)
