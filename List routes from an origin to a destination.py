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
    for line, stations in linedict.items():
        if (search_a_station_in_a_line(stations, tosearch) != -1):
            foundlinelist.append(line)
            continue
    return foundlinelist #a list of found lines

    
def find_interchanges(targetline, linedict):
    interchanges = list()
    for station in linedict[targetline]:
        for linename, stationlists in linedict.items():
            if (search_a_station_in_a_line(stationlists, station) != -1) and (linename != targetline): 
                interchanges.append(station)
                break
    interchanges.sort()
    return interchanges


#consider hku to admiralty
#Island Line: Admiralty, Central
#Island Line: Admiralty, Central
#Tsuen Wan Line: Admiralty, Central, Mong Kok, Yau Ma Tei

def returnsecond(element):
    return element[1]


def find_common_interchanges(interdictO, interdictD):
    #assuming different lines of origin and destination
    #i.e. must have at least 1 interchange 
    
    """
    e.g.
    Admiralty: {"Island Line": [Admiralty, Central],
                "East Rail Line": [Admiralty, Kowloon Tong, ...]}
    Choi Hung: {"Kwun Tong Line": [HMT, ...,Kowlooon Tong, ...]}
    how to get "east rail line', "kowloon tong", and "kwun tong line"?
    """
    
    common = list()
    for lineO in interdictO.keys():   
        temp = list()
        for interchangeO in interdictO[lineO]:
            for lineD, interchangesD in interdictD.items():
                if search_a_station_in_a_line(interchangesD, interchangeO) != -1:
                    temp.append(lineO)
                    temp.append(interchangeO)
                    temp.append(lineD)
                    common.append(temp[:])
                    #print(temp)
                    #print(common)
                    temp.clear()
    common.sort(key=returnsecond)
    return common #list of lists: initial line, common interchanges, final line
    

#search_a_station_in_a_line(linelist, station_to_find)
#find_lines(linedict, tosearch)
#find_interchanges(targetline, linedict)
#find_common_interchanges(interO, interD)



def main():
    lines_and_stations = dict()
    get_lines(lines_and_stations)
    origin = standardize(input("Origin station: "))
    dest = standardize(input("Destination station: "))
    
    found_lines_origin = find_lines(lines_and_stations, origin)
    found_lines_dest = find_lines(lines_and_stations, dest)
    L_o = len(found_lines_origin)
    L_d = len(found_lines_dest)
    
    if ( L_o == 0 ) or ( L_d == 0 ):
        print("Station(s) not found")
    else:
        found_lines_origin.sort()
        found_lines_dest.sort()
        
        intersect = False
        intersecting = list()
        for foundline in found_lines_origin:
            if foundline in found_lines_dest:
                intersect = True
                intersecting.append(foundline)
        
        if intersect:
            #1: no interchange
            print("\n".join(intersecting))
        
        else:
            #2: 1 interchange
            #3: >1 interchange
            
            #E.G ADMIRALTY TO CHOI HUNG
            #ADMIRALTY: ISLAND LINE, EAST RAIL LINE 
            #CHOI HUNG: KWUN TONG LINE
            #ONLY INTERCHANGE: KOWLOON TONG (EAST RAIL -> KWUn)
            
            interchanges_O = dict()
            interchanges_D = dict()
            for line in found_lines_origin:
                interchanges_O[line] = find_interchanges(line, lines_and_stations)
            for line in found_lines_dest:
                interchanges_D[line] = find_interchanges(line, lines_and_stations)
            
            common_interchanges = find_common_interchanges(interchanges_O, interchanges_D)
            #print(common_interchanges)
            if len(common_interchanges) == 0:
                print("More than one change or no route found")
            else:
                for route in common_interchanges:
                    for interchange in route[1:len(route)-1]:
                        print(f"{route[0]}: {origin}->{interchange}")
                        print(f"{route[-1]}: {interchange}->{dest}")


                #consider hmt to sha tin
                # 1: hmt -> hh -> sha tin 
                # 2: hmt -> klt -> sha tin
                # 3: hmt -> tai wai -> sha tin

main()
