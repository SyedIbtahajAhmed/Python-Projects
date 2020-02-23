import random
import math
import matplotlib.pyplot as plt
#Defining Functions
#Plotting Function Of Line Graph
def LineGraph(y_arr, x_arr):
    temp_list = []
    for i in y_arr:
        temp_list.append(len(i))
    plt.plot(x_arr, temp_list, color = 'orange')
    plt.xlabel("X")
    plt.ylabel("Frequency")
    plt.title("Line Graph")
    plt.show()


#Plotting Function Of Bar Graph
def BarGraph(y_arr, x_arr):
    temp_list = []
    for i in y_arr:
        temp_list.append(len(i))
    plt.bar(x_axis, temp_list, label = 'Frequency', color = 'blue', width=1500, align = 'center')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Frequency')
    plt.title('Bar Graph')
    plt.show()

#Plotting Function Of Histogram
def PieChart(y_arr, x_arr):
    temp_list = []
    for i in y_arr:
        temp_list.append(len(i))
    cols = ['c','m','r','b', 'g']

    plt.pie(x_arr,
    labels=temp_list,
    colors=cols,
    startangle=90,
    shadow= True,
    autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

def frequencySum(f):
    x = 0       # frequency Sum ""x""
    for i in range(0,5):
        x = x + len(f[i])
    return x

def frequencyXSum(f,x):
    f_x_summ = 0        # fx summation = f_x_summ
    for i in range(0, 5):
        f_x_summ = f_x_summ + (len(f[i]) * x[i])
    return f_x_summ

def frequencyX2Sum(f, x):
    f_x2_summ = 0       # fx^2 summation = f_x2_summ
    for i in range(0,5):
        f_x2_summ = f_x2_summ + (len(f[i]) * pow(x[i], 2))
    return f_x2_summ

#Mean Calculation
def Mean(fx, f):
    temp_mean = fx / f
    return temp_mean

#Median Calculation
def Median(freq, x):
    temp = (freq + 1) / 2
    count = 0
    list_sum = x[0]
    for i in range(1, len(x)):
        if list_sum <= temp:
            list_sum += x[i]
            count += 1
        else:
            return x[count]

#Mode Calculation
def Mode(freqlist, x):
    largest = len(freqlist[0])
    temp = 0
    for i in range(0, 5):
        if largest < len(freqlist[i]):
            largest = len(freqlist[i])
            temp = i
    largest = x[temp]           #largest have the biggest frequency
    temp = 20000 / 5
    temporary = temp
    while(True):
        if largest < temp:
            return int(temp - 20000/5), int(temp)
        else:
            temp += temporary

#Variance Calculation
def Variance(f, fx, fxx):
    temp = fxx / f
    temp2 = pow((fx/f), 2)
    variance = temp - temp2
    return variance

#Standard Deviation Calculation
def Standard_Deviation(v):
    temp = math.sqrt(v)
    return temp

#Initializing All The Lists
random_list = []
x_axis = []
interval_1 = []
interval_2 = []
interval_3 = []
interval_4 = []
interval_5 = []
intervals_list = []

#Taking Input To Interact With User
any_key = str(input('Press Any Key To Continue Or Pres "q" To Quit The Program!\n'))
#Checking The Input To Be Not Equal To Q or q
while(any_key != chr(113) and any_key != chr(81)):
    #Taking Total Number Of Readings To Generate
    readings = int(input("How Many Random Readings Do You Want?\n"))
    if type(readings) == int:
        #Appending All Values In random_list List
        for i in range(0,readings):
            random_list.append(random.randint(1, 20000))
        #Making Intervals Of X-Axis
        inter_end = 20000 / 5    #Making 5 Intervals Of Every Reading
        inter_start = inter_end
        temp = inter_start
        #Storing Values In Every Interval List
        count = 0
        while(count < 5):
            if count == 0:
                for i in random_list:
                    if i < inter_end:
                        interval_1.append(i)
                count += 1
                inter_end = inter_end + temp
            elif count == 1:
                for i in random_list:
                    if i >= inter_start and i < inter_end:
                        interval_2.append(i)
                count += 1
                inter_end = inter_end + temp
                inter_start = inter_start + temp
            elif count == 2:
                for i in random_list:
                    if i >= inter_start and i < inter_end:
                        interval_3.append(i)
                count += 1
                inter_end = inter_end + temp
                inter_start = inter_start + temp
            elif count == 3:
                for i in random_list:
                    if i >= inter_start and i < inter_end:
                        interval_4.append(i)
                count += 1
                inter_end = inter_end + temp
                inter_start = inter_start + temp
            elif count == 4:
                for i in random_list:
                    if i >= inter_start and i <= inter_end:
                        interval_5.append(i)
                count += 1
                inter_end = inter_end + inter_start
                inter_start = inter_start + inter_start
        
        #Appending All Interval Lists To A Central List
        for i in range(0, 5):
            if i == 0:
                intervals_list.append(interval_1)
            if i == 1:
                intervals_list.append(interval_2)
            if i == 2:
                intervals_list.append(interval_3)
            if i == 3:
                intervals_list.append(interval_4)
            if i == 4:
                intervals_list.append(interval_5)
        
        #Now Making Table
        inter_end = 20000 / 5    #Again Making Intervals
        inter_start = inter_end
        temp = inter_end
        count = 0

        print("\n||------------------------------||--------------||----------------------||------------------------------||----------------------------------------------||")
        print("||                              ||              ||                      ||                              ||                                              ||")
        print("|| Range Of X:\t\t\t|| X\t\t|| freguency(f)\t\t|| f*X\t\t\t\t|| f*X^2\t\t\t\t\t||")
        print("||                              ||              ||                      ||                              ||                                              ||")
        print("||------------------------------||--------------||----------------------||------------------------------||----------------------------------------------||")
        while count < 5:
            x_axis.append(int((inter_end + (inter_start - temp)) / 2))
            if count < 2:
                print("||                              ||              ||                      ||                              ||                                              ||")
                print("||", int(inter_start - temp), " >= X < ", int(inter_end), "\t\t||", x_axis[count], "\t||", len(intervals_list[count]), "\t\t||", len(intervals_list[count]) * x_axis[count], "\t\t\t||", len(intervals_list[count]) * pow(x_axis[count], 2), "\t\t\t\t\t||")
            elif count == 2:
                print("||                              ||              ||                      ||                              ||                                              ||")
                print("||", int(inter_start - temp), " >= X < ", int(inter_end), "\t\t||", x_axis[count], "\t||", len(intervals_list[count]), "\t\t||", len(intervals_list[count]) * x_axis[count], "\t\t\t||", len(intervals_list[count]) * pow(x_axis[count], 2), "\t\t\t\t||")
            else:
                print("||                              ||              ||                      ||                              ||                                              ||")
                print("||", int(inter_start - temp), " >= X < ", int(inter_end), "\t||", x_axis[count], "\t||", len(intervals_list[count]), "\t\t||", len(intervals_list[count]) * x_axis[count], "\t\t\t||", len(intervals_list[count]) * pow(x_axis[count], 2), "\t\t\t\t||")
            inter_end += temp
            inter_start += temp
            count+=1
        print("||------------------------------||--------------||----------------------||------------------------------||----------------------------------------------||")
        print("||------------------------------||--------------||----------------------||------------------------------||----------------------------------------------||")
        #Printing All Summations:
        print("||------------------------------||--------------||\tn = ", frequencySum(intervals_list), "\t||Sum(fx) = ", frequencyXSum(intervals_list, x_axis), "\t\t||Sum(f*x^2) = ", frequencyX2Sum(intervals_list, x_axis), "\t\t\t||")
        print("||------------------------------||--------------||----------------------||------------------------------||----------------------------------------------||")
        print("||------------------------------||--------------||----------------------||------------------------------||----------------------------------------------||")

        #Printing All The Information
        print("\n\nMean Of The Generated Data Is : {}".format(Mean(frequencyXSum(intervals_list, x_axis), frequencySum(intervals_list))))
        print("\nMedian Of The Generated Data Is : {}".format(Median(frequencySum(intervals_list), x_axis)))
        print("\nMode Of The Generated Data Is : {} >= X < {}".format(Mode(intervals_list , x_axis)[0], Mode(intervals_list, x_axis)[1]))
        variance = Variance(frequencySum(intervals_list), frequencyXSum(intervals_list, x_axis), frequencyX2Sum(intervals_list, x_axis))
        print("\nVariance Of The Generated Data Is : {}".format(variance))
        print("\nStandard Deviation Of The Generated Data : {}".format(Standard_Deviation(variance)))

        ##Now Plotting Graphs
        graph_input = int(input("\n\nWhich Graph Do You Want?\n1. For Line Graph Press 1\n2. For Bar Graph Press 2\n3. For Pie Chart Press 3\n4. For All Three Press 4\n5. Press 5 To Not Generate Graph\n"))
        while graph_input != 5:
            try:
                if graph_input == 1:
                    print("Line Graph Plotted!")
                    LineGraph(intervals_list, x_axis)
                    break
                elif graph_input == 2:
                    print("Bar Graph Plotted!")
                    BarGraph(intervals_list, x_axis)
                    break
                elif graph_input == 3:
                    print("Pie Chart Plotted!")
                    PieChart(intervals_list, x_axis)
                    break
                elif graph_input == 4:
                    print("All Graphs Plotted!")
                    LineGraph(intervals_list, x_axis)
                    BarGraph(intervals_list, x_axis)
                    PieChart(intervals_list, x_axis)
                    break
                else:
                    break
            except:
                raise print("\nSomething Went Wrong While Plotting Graph!")
            finally:
                print("\nGraph Plotted Successfully.")
        #Again Asking For Input To Generate Data Again
        any_key = str(input('\nPress Any Key To Generate Data Again Or Pres "q" To Quit The Program!\n'))
print("\nThanks For Using The Program! BYE")