file = "/home/anthony/Documents/github/Advent-Of-Code/2023/sample"
document = []

with open(file) as source:
    for line in source:
        line = line.strip("\n")
        document.append(line)

# part one
def getCalibrationValue(document):
    calibration_value = 0
    for line in document:
        value = [num for num in line if num.isnumeric()]
        calibration_value += int(value[0]+value[-1])
    return calibration_value

if __name__ == "__main__":
    part_one = getCalibrationValue(document)
    print("Part One:",part_one)