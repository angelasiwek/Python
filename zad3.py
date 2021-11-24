def roman2int(s: str):
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' :100 , 'D' : 500, 'M' :1000 }
    result = 0
    for i in range(0, len(s)-1):
        if dictionary[s[i+1]] > dictionary[s[i]]:
            result -= dictionary[s[i]]
        else:
            result += dictionary[s[i]]
    result += dictionary[s[len(s)-1]]
    return result

print(roman2int('MCDXIX'))
print(roman2int('MCCXVII'))