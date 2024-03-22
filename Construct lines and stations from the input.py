'''
1) Ask the user for the number of lines to be constructed.
2) For each line, ask for the name of a line and the names of stations on the line, until the
stop code '-1' is entered.
3) Format the names according to the requirements described in Level 1.
4) Create a text file using the formatted name of the line.
5) Store in the file the formatted names of stations in input order, one station per line.
Below is an example text file of "Tsuen Wan Line" as shown in Figure 1. Note that one file is created for each line.
6) Read the created files in input order.
7) For each file, print the name of the line followed by the names of stations.
'''

def standardize(name):
    
    if name.lower() == "hku":
        formatted = "HKU"
    else:
        formatted = list(name)

        if formatted[0].islower():
            formatted[0] = formatted[0].upper()
    
        for i in range(1, len(formatted)):
            if (formatted[i-1] == " "):
                if (formatted[i].islower()):
                    formatted[i] = formatted[i].upper()
            else:
                if (formatted[i].isupper()):
                    formatted[i] = formatted[i].lower()
        
        formatted = "".join(formatted)
    
    return formatted
    
    
def construct_lines(lines):
    nLines = int(input("Number of lines: "))
    
    for line in range(1, nLines+1):
        print(f"Name of line {line}: ", end="")
        nameLine = standardize(input())
        lines.append(nameLine)
        
        linefile = open((nameLine+".txt"), "w")
        
        nStations = 1
        while True:
            print(f"Name of station {nStations} on {nameLine}: ", end="")
            stationInput = input()
            if stationInput == "-1":
                break
            nameStation = standardize(stationInput)
            if nStations != 1:
                linefile.write("\n")
            linefile.write(nameStation)
            nStations += 1
        
        linefile.close()

def output_lines(lines):
    for line in lines:
        print(f"{line}: ", end="")
        linefile = open(line+".txt")
        
        stationList = []
        for station in linefile:
            if station[-1] == "\n":
                stationList.append(station[0:len(station)-1])
            else:
                stationList.append(station)
        
        for i in range(len(stationList)):
            print(stationList[i], end="")
            if (i+1) != len(stationList):
                print("<->", end="")
        
        linefile.close()
        print()
    

def main():
    linelist = []
    construct_lines(linelist)
    output_lines(linelist)

main()
