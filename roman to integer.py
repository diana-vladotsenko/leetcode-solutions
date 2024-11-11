u = len(s)
fi = 0
s = ["I","V","X","L","C","D","M"]
dictionary = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
for l in range(u):
    if  l + 1 < u and dictionary[s[l]] < dictionary[s[l + 1]] :
       fi = fi - dictionary[s[l]]
    else:
        fi = fi + dictionary[s[l]]
return fi