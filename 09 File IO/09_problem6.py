with open("log.txt" , "r") as f:
    content = f.read()
    if "python" in content:
        print("YES python is present in the log file")
    else:
        print("ON python is absent in the log file")