f = 0.2
angle = [0.0875,0.1763,0.364,0.5774,0.8391,1.1918,1.7321,2.7475,5.6713]
results = []
def calculate(a):
    global f
    result = round((1/(1+(f/a))),2)
    results.append(result)

for ang in angle:
    calculate(ang)
print(results)

