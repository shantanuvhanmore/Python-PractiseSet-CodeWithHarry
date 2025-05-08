with open("log.txt" , "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        count +=1
        if "python" in line.lower():
            print("YES python is present in the log file at line",count)
            break
    else:
        print("ON python is absent in the log file")