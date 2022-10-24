import pandas as pd

def readData():   
    try:
        fileName = input("Enter a file name: ")
        inFile = open(fileName, 'r')    
    except FileNotFoundError:
        print("File not found.")
        fileName = input("Enter a file name: ")
        inFile = open(fileName, 'r')   
    for line in inFile:
        strip = line.strip('\n')
        data = strip.split(', ')
    data = [int(num) for num in data]
    return data

def classWidth(data, numClasses):
    return int((max(data) - min(data)) / numClasses) + 1

def lowerClassLimit(data, clsWidth, i):
    return min(data) + (clsWidth * i)

def upperClassLimit(data, clsWidth, i):
    return min(data) + (clsWidth * (i+1)) - 1

def lowerClassBoundary(lcLimit):
    return lcLimit - 0.5

def upperClassBoundary(ucLimit):
    return ucLimit + 0.5

def classMidpoint(lcLimit, ucLimit):
    return (lcLimit + ucLimit) / 2

def classFrequency(data, lcLimit, ucLimit):
    freq = 0
    for num in data:
        if num in range(lcLimit, ucLimit + 1):
            freq += 1
    return freq

def cumulativeFrequency(freqs):
    freq = 0
    for clsFreq in freqs:
        freq += clsFreq
    return freq
    
def relativeFrequency(freqs, i, data):
    return round(freqs[i] / len(data), 3)

def cumRelatFrequency(rel_freqs):
    freq = 0
    for relatFreq in rel_freqs:
        freq += relatFreq
    return round(freq, 3)

def main():
    data = readData()
    print(f"Data Set:\n{data}")
    print('')
    print(f'Largest num: {max(data)}\nSmallest num: {min(data)}')
    print('')
    numClasses = int(input("How many classes are there? "))
    clsWidth = classWidth(data, numClasses)
    print('')
    print(f"Class Width: {clsWidth}")
    print('')
    columns = {
        "Class Limits (Lower-Upper)": [],
        "Class Boundaries (Lower-Upper)": [],
        "Class Midpoints": [],
        "Frequencies": [],
        "Cumulative Frequencies": [],
        "Relative Frequencies": [],
        "Cumulative Relative Frequencies": []
    }
    freqs = columns["Frequencies"]
    rel_freqs = columns["Relative Frequencies"]
    for i in range(numClasses):
        lcLimit = lowerClassLimit(data, clsWidth, i)
        ucLimit = upperClassLimit(data, clsWidth, i)
        columns["Class Limits (Lower-Upper)"] += [f"{lcLimit}-{ucLimit}"]
        lcBound = lowerClassBoundary(lcLimit)
        ucBound = upperClassBoundary(ucLimit)
        columns["Class Boundaries (Lower-Upper)"] += [f"{lcBound}-{ucBound}"]
        clsMidpoint = classMidpoint(lcLimit, ucLimit)
        columns["Class Midpoints"] += [clsMidpoint]
        clsFreq = classFrequency(data, lcLimit, ucLimit)
        columns["Frequencies"] += [clsFreq]
        cumFreq = cumulativeFrequency(freqs)
        columns["Cumulative Frequencies"] += [cumFreq]
        relatFreq = relativeFrequency(freqs, i, data)
        columns["Relative Frequencies"] += [relatFreq]
        cumRelatFreq = cumRelatFrequency(rel_freqs)
        columns["Cumulative Relative Frequencies"] += [cumRelatFreq]
    df = pd.DataFrame(columns)
    print(df)

if __name__ == '__main__':
    main()