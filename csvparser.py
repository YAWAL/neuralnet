import csv


def csv_parser(filename):
    result = list()
    try:
        file = open(filename,"r")
        csv_reader = csv.reader(file)
        for row in csv_reader:
            result.append((int(float(row[196])), list(map(lambda x: float(x)/255, row[0:195]))))
            # result.append((float(row[196]), row[0:195]))
        file.close()
    except OSError:
        print('can not read file')
    return result


# print(len(csv_parser("dataset/test.csv")))
# print(csv_parser("dataset/test.csv")[0])
# print(len(csv_parser("dataset/test.csv")[0]))
