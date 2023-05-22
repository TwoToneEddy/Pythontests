





def replaceSingleQuotes(input):
    
    input = input.replace('""','*')
    input = input.replace('"','')
    input = input.replace('*','""')

    return input







string = 'Testing "" or " '

print(f"Before:\n {string}\n After:\n {replaceSingleQuotes(string)}")

