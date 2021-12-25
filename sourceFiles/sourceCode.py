import csv
import pylab
import numpy


#Reading file data
def getData(fileName):
    rows = []
    with open(fileName, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    year = []
    pov = []
    for i in rows:
        year.append(float(i[2]))
        pov.append(float(i[3]))
    return [year,pov]
 
# year, pov = getData("World.csv")
# print(year)
# pov = pylab.array(pov) 
# year = pylab.array(year)
# print(year)
     
     
#Plotting file data           
def plotData(inputFile):
     year, pov = getData(inputFile)
     pov = pylab.array(pov) 
     year = pylab.array(year)
     pylab.plot(year, pov,'bo')
     pylab.title('Poverty in the '+inputFile)
     pylab.xlabel('Years')
     pylab.ylabel('Number of people')
     pylab.show()


# print(plotData("Brazil.csv"))
# print(plotData("India.csv"))
# print(plotData("Japan.csv"))
# print(plotData("USA.csv"))
# print(plotData("World.csv"))

#Goodness of fit
def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))

#Code for fitting data
def fitData(inputFile,n):
     year, pov = getData(inputFile)
     pov = pylab.array(pov) 
     year = pylab.array(year)
     pylab.plot(year, pov,'bo')
     pylab.title('Poverty in the '+inputFile[:-4])
     pylab.xlabel('Years')
     pylab.ylabel('Number of people')
     fit = pylab.polyfit(year, pov,n)
     predictedDistances = pylab.polyval(fit, year)
     error = rSquared(pov,predictedDistances)
     pylab.plot(year, predictedDistances, 'k:', label = 'cubic fit')
     pylab.show()
     print(inputFile[:-4] + ":")
     print(error)


#Used Leave one out Cross Validation

fitData("Brazil.csv",3) #0.8547360275026763
fitData("India.csv",5) #0.9861537727432116
fitData("Japan.csv",10) #0.4880933829352849
fitData("USA.csv",4) #0.9464210431927702
fitData("World.csv",4) #0.9880902214619804





# for i in range(20):
#       print(fitData("World.csv",i))

#Leave one out cross validation
# Testing the data

def testData(inputFile,n):
     result = []
     year, pov = getData(inputFile)
     a = len(pov)
     for i in range(a):
         year, pov = getData(inputFile)
         pov = numpy.delete(pylab.array(pov),i) 
         year = numpy.delete(pylab.array(year),i)
         fit = pylab.polyfit(year, pov,n)
         predictedDistances = pylab.polyval(fit, year)
         # pylab.plot(year, predictedDistances, 'k:', label = 'cubic fit')
         # pylab.show()
         error = rSquared(pov,predictedDistances)
         result.append(error)
     return result
    


# print(testData("World.csv",3))

# L = numpy.mean(testData("World.csv",1))
# print(L)


def allFit(inputFile,n):
    D= {}
    for i in range (1,n+1):
        D[i] = numpy.mean(testData(inputFile,i))
    return D


# print(allFit("Brazil.csv",15)) #3
# print(allFit("India.csv",10)) #5
# print(allFit("Japan.csv",10)) #10
# print(allFit("USA.csv",15)) #4
# print(allFit("World.csv",10)) #4








