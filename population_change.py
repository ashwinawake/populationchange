import collections
import matplotlib.pyplot as plt



population_dict_2010 = collections.defaultdict(int)
population_dict_2100 = collections.defaultdict(int)
with open('C:\Users\Ashwin\Desktop\Thinkful\lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1]=='Total National Population':
            population_dict_2010[line[0]] += line[5]
            population_dict_2100[line[0]] += line[6]

print(population_dict_2010)
print(population_dict_2100)


#Looping through 2 dictionaries and computing the difference between the 2 populations
population_change = collections.defaultdict(int)
population_change = population_dict_2010

for (k,v),(k2,v2) in zip(population_dict_2010.items(),population_dict_2100.items()):
    population_change[k] = population_dict_2100[k2] - population_dict_2010[k]

print(population_change)


#plotting a bar chart

plt.bar(range(len(population_change)), population_change.values(), align='center')
plt.xticks(range(len(population_change)), population_change.keys())
plt.title('Population change in 90 years(2100)')
plt.show()


#Writing result to a csv file
with open('C:\Users\Ashwin\Desktop\Thinkful\population_change.csv','w') as outputFile:
    outputFile.write('Continent,Population Difference\n')
    for k,v in population_change.iteritems():
        outputFile.write(k+','+str(v)+'\n')
