

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


def get_lines(linedict):
    
    #Island Line.txt
    #Tsuen Wan Line.txt
    #Tuen Ma Line.txt
    #Kwun Tong Line.txt
    #East Rail Line.txt
    
    to_get = [ "Island Line", "Tsuen Wan Line",
    "Tuen Ma Line", "Kwun Tong Line", "East Rail Line"]
    
    for line in to_get:
        TEMP_stationList = []
        stations = open(line+".txt")
        
        for station in stations:
            if station[-1] == "\n":
                TEMP_stationList.append(station[0:len(station)-1])
            else:
                TEMP_stationList.append(station)
        
        linedict[line] = TEMP_stationList

def search_a_station_in_a_line(linelist, stationtofind):
    #BINARY SEARCH OF A SORTED LIST
    tosearch = list(enumerate(sorted(linelist)))
    a = 0
    b = len(linelist) - 1 
    while a <= b:
        m = (a + b)//2
        if tosearch[m][1] == stationtofind:
            return m
        else:
            if stationtofind < tosearch[m][1]:
                b = m-1
            else:
                a = m+1
    return -1


def find_lines(linedict, tosearch):
    foundlinelist = list()
    found = False
    for line, stations in linedict.items():
        if (search_a_station_in_a_line(stations, tosearch) != -1):
            foundlinelist.append(line)
            found = True

    if found:
        print(f"{tosearch} Station found")
    else:
        print("Station not found")
            
    return foundlinelist #a list of found lines

    
def find_interchanges(targetline, linedict):
    interchanges = list()
    for station in linedict[targetline]:
        for linename, stationlists in linedict.items():
            if (search_a_station_in_a_line(stationlists, station) != -1) and (linename != targetline): 
                interchanges.append(station)
                break
    interchanges.sort()
    print(f": {', '.join(interchanges)}", end="")
    print()

#search_a_station_in_a_line(linelist, station_to_find)
#find_lines(linedict, tosearch)
#find_interchanges(targetline, linedict)


def main():
    lines_and_stations = dict()
    get_lines(lines_and_stations)
    tosearch = standardize(input("Station to be searched for: "))
    found_lines = find_lines(lines_and_stations, tosearch)
    found_lines.sort()
    for line in found_lines:
        print(line, end="")
        find_interchanges(line, lines_and_stations)

main()
