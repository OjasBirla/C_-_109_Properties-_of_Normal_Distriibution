import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")

math = dict(df)["math score"]
reading = dict(df)["reading score"]
writing = dict(df)["writing score"]

def getMean(data):
    mean = sum(data)/len(data)
    return mean

def getMedian(data):
    median = statistics.median(data)
    return median

def getMode(data):
    mode = statistics.mode(data)
    return mode

def getStDev(data):
    stDev = statistics.stdev(data)
    return stDev


def findFirstStDev(data):
    firstStDevStart, firstStDevEnd = getMean(data) - getStDev(data), getMean(data) + getStDev(data)
    firstStDev = [result for result in data if(result > firstStDevStart and result < firstStDevEnd)]
    return "{}%".format(len(firstStDev)*100/len(data))

def findSecondStDev(data):
    secondStDevStart, secondStDevEnd = getMean(data) - (2 * getStDev(data)), getMean(data) + (2 * getStDev(data))
    secondStDev = [result for result in data if(result > secondStDevStart and result < secondStDevEnd)]
    return "{}%".format(len(secondStDev)*100/len(data))

def findThirdStDev(data):
    thirdStDevStart, thirdStDevEnd = getMean(data) - (3 * getStDev(data)), getMean(data) + (3 * getStDev(data))
    thirdStDev = [result for result in data if(result > thirdStDevStart and result < thirdStDevEnd)]
    return "{}%".format(len(thirdStDev)*100/len(data))

def makeGraph(data, label):
    graph = ff.create_distplot([data], [label], show_hist=False)
    graph.show()

# makeGraph(math, "Math Score")
# makeGraph(reading, "Reading Score")
# makeGraph(writing, "Writing Score")

print("Math \n\nMean: " + str(getMean(math)) + "\nMedian: " + str(getMedian(math)) + "\nMode: " + str(getMode(math)) + "\n\n1st Standard Deviation: " + str(findFirstStDev(math)) + "\n2nd Standard Deviation: " + str(findSecondStDev(math)) + "\n3rd Standard Deviation: " + str (findThirdStDev(math)))

print("\nReading \n\nMean: " + str(getMean(reading)) + "\nMedian: " + str(getMedian(reading)) + "\nMode: " + str(getMode(reading)) + "\n\n1st Standard Deviation: " + str(findFirstStDev(reading)) + "\n2nd Standard Deviation: " + str(findSecondStDev(reading)) + "\n3rd Standard Deviation: " + str (findThirdStDev(reading)))

print("\nWriting \n\nMean: " + str(getMean(writing)) + "\nMedian: " + str(getMedian(writing)) + "\nMode: " + str(getMode(writing)) + "\n\n1st Standard Deviation: " + str(findFirstStDev(writing)) + "\n2nd Standard Deviation: " + str(findSecondStDev(writing)) + "\n3rd Standard Deviation: " + str (findThirdStDev(writing)))