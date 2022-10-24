import pandas as pd

def read_data():   
    try:
        file_name = input("Enter a file name: ")
        in_file = open(file_name, 'r')    
    except FileNotFoundError:
        print("File not found.")
        file_name = input("Enter a file name: ")
        in_file = open(file_name, 'r')   
    for line in in_file:
        strip = line.strip('\n')
        data = strip.split(', ')
    data = [int(num) for num in data]
    return data

def calc_class_width(data, num_classes):
    return int((max(data) - min(data)) / num_classes) + 1

def calc_lc_limit(data, cls_width, i):
    return min(data) + (cls_width * i)

def calc_uc_limit(data, cls_width, i):
    return min(data) + (cls_width * (i+1)) - 1

def calc_lc_boundary(lc_limit):
    return lc_limit - 0.5

def calc_uc_boundary(uc_limit):
    return uc_limit + 0.5

def calc_class_midpoint(lc_limit, uc_limit):
    return (lc_limit + uc_limit) / 2

def calc_class_frequency(data, lc_limit, uc_limit):
    freq = 0
    for num in data:
        if num in range(lc_limit, uc_limit + 1):
            freq += 1
    return freq

def calc_cumulative_frequency(freqs):
    freq = 0
    for class_freq in freqs:
        freq += class_freq
    return freq
    
def calc_relative_frequency(freqs, i, data):
    return round(freqs[i] / len(data), 3)

def calc_cumulative_relative_frequency(rel_freqs):
    freq = 0
    for relatFreq in rel_freqs:
        freq += relatFreq
    return round(freq, 3)

def main():
    data = read_data()
    print(f"Data Set:\n{data}")
    print('')
    print(f'Largest num: {max(data)}\nSmallest num: {min(data)}')
    print('')
    num_classes = int(input("How many classes are there? "))
    class_width = calc_class_width(data, num_classes)
    print('')
    print(f"Class Width: {class_width}")
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
    for i in range(num_classes):
        lc_limit = calc_lc_limit(data, class_width, i)
        uc_limit = calc_uc_limit(data, class_width, i)
        columns["Class Limits (Lower-Upper)"] += [f"{lc_limit}-{uc_limit}"]
        lc_boundary = calc_lc_boundary(lc_limit)
        uc_boundary = calc_uc_boundary(uc_limit)
        columns["Class Boundaries (Lower-Upper)"] += [f"{lc_boundary}-{uc_boundary}"]
        class_midpoint = calc_class_midpoint(lc_limit, uc_limit)
        columns["Class Midpoints"] += [class_midpoint]
        class_frequency = calc_class_frequency(data, lc_limit, uc_limit)
        columns["Frequencies"] += [class_frequency]
        cumulative_frequency = calc_cumulative_frequency(freqs)
        columns["Cumulative Frequencies"] += [cumulative_frequency]
        relative_frequency = calc_relative_frequency(freqs, i, data)
        columns["Relative Frequencies"] += [relative_frequency]
        cum_rel_frequency = calc_cumulative_relative_frequency(rel_freqs)
        columns["Cumulative Relative Frequencies"] += [cum_rel_frequency]
    df = pd.DataFrame(columns)
    print(df)

if __name__ == '__main__':
    main()