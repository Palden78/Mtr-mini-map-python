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
    
    print("Formatted name:", formatted)
    return formatted
    
def main():
    name = standardize(input("Name: "))
    
main()
