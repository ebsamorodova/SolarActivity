def GetFileName(city, case):
    suf = {"max": "X", "min": "N", "mean": "G"}
    return "T{}_{}.txt".format(suf[case], city)

def SkipFirstLines(file):
    cnt = 0
    for line in file:
        cnt += 1
        if cnt == 19:
            return

cities = ["Bologna", "Prague", "Uccle", "Milan"]
cases = {"Bologna": ["max", "min", "mean"], 
         "Prague": ["max", "min", "mean"], 
         "Uccle": ["max", "min"], 
         "Milan": ["max", "min", "mean"]}

for city in cities:
    for case in cases[city]:
        file_input = GetFileName(city, case)
        file_output = file_input[:-4] + "_formatted.txt"
        f_in = open(file_input, "r")
        f_out = open(file_output, "w")
        SkipFirstLines(f_in)        
        for line in f_in:
            row = line.split(",")
            date, temperature = row[2], float(row[3]) / 10
            year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
                    
            # если данные вообще есть
            if int(row[4]) != 9 and (month, day) != (2, 29):
                print(line, end="", file=f_out)        
        
        f_in.close()
        f_out.close()