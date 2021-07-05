salamaList = list(input())
status = "nakhor lite" if salamaList.count("R") >= 3 or salamaList.count("G") == 0 or (
    salamaList.count("R") >= 2 and salamaList.count("Y") >= 2) else "rahat baash"
print(status)
