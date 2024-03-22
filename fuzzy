import matplotlib.pyplot as plt
import numpy as np

def graph(fuzzy_set, title, xlabel, ylabel='Membership'):
    x = np.linspace(0, 255, 1000)

    for key, value in fuzzy_set.items():
        shape, a, b, c = value
        if(shape=='tri'):
            y = np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))
            plt.plot(x, y, label=key)
        elif(shape=='trap'):
            y = np.maximum(0, np.minimum((x-a)/(b-a), 1, (c-x)/(c-b)))
            plt.plot(x, y, label=key)
    plt.xticks([0, 31, 61, 95, 127, 159, 191, 223, 255])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

rules=[['NL','ZE','PL'],['ZE','NL','PL'],['NM','ZE','PM'],['NS','PS','PS'],['PS','NS','NS'],['PL','ZE','NL'],['ZE','NS','PS'],['ZE','NM','PM']]

Speed_fuzzy={'NL':['trap',0,31,61],'NM':['tri',31,61,95],'NS':['tri',61,95,127],'ZE':['tri',95,127,159],'PS':['tri',127,159,191],'PM':['tri',159,191,223],'PL':['trap',191,223,255]}

Acc_fuzzy={'NL':['trap',0,31,61],'NM':['tri',31,61,95],'NS':['tri',61,95,127],'ZE':['tri',95,127,159],'PS':['tri',127,159,191],'PM':['tri',159,191,223],'PL':['trap',191,223,255]}


Thro_fuzzy={'NL':['trap',0,31,61],'NM':['tri',31,61,95],'NS':['tri',61,95,127],'ZE':['tri',95,127,159],'PS':['tri',127,159,191],'PM':['tri',159,191,223],'PL':['trap',191,223,255]}


graph(Speed_fuzzy, 'Speed', 'Fuzzy Speed Sets')
graph(Acc_fuzzy, 'Acceleration', 'Fuzzy Acceleration Sets')


speed = int(input("Enter the speed difference:"))
acc = int(input("Enter the acceleration difference:"))

actual_speed={}
actual_acc={}

for i in Speed_fuzzy.keys():
    if(speed >= Speed_fuzzy[i][1] and speed<=Speed_fuzzy[i][3]):

        print("Fuzzy sets having Speed",speed," is :",i)
        actual_speed[i]=''

for i in actual_speed.keys():
    member_value=0
    shape, a, b, c = Speed_fuzzy[i]

    if (speed>=a and speed<=b):
        member_value=(speed-a)/(b-a)
    elif(speed>=b and speed<=c):
        member_value=(c-speed)/(c-b)

    actual_speed[i]=member_value
print("Membership value for given Speed is : ",actual_speed)


for i in Acc_fuzzy.keys():
    if(acc >= Acc_fuzzy[i][1] and acc<=Acc_fuzzy[i][3]):
        print("Fuzzy sets having Acc.",acc," is :",i)
        actual_acc[i]=''


for i in actual_acc.keys():
    member_value=0
    shape, a, b, c = Acc_fuzzy[i]

    if (acc>=a and acc<=b):
            member_value=(acc-a)/(b-a)
    elif(acc>=b and acc<=c):
            member_value=(c-acc)/(c-b)
    actual_acc[i]=member_value
print("Membership value for given Acc is : ",actual_acc)


speed_rule=[]
acc_rule=[]

for i in actual_speed.keys():
    for j in range(len(rules)):
        if i in rules[j][0]:
            #print(rules[j])
            speed_rule.append(j+1)  

for i in actual_acc.keys():
    for j in range(len(rules)):
        if i in rules[j][1]:
            #print(rules[j])
            acc_rule.append(j+1)

common_rule = list(set(speed_rule) & set(acc_rule))
print("The rules satisfying are: ",common_rule)


#find the min -> speed and acc
rule_memb=[0,0]
for i in range(len(common_rule)):
    rule_memb[i]=min(actual_speed[rules[common_rule[i]-1][0]], actual_acc[rules[common_rule[i]-1][1]])

    print("For Rule ",common_rule[i]," speed-> ",actual_speed[rules[common_rule[i]-1][0]]," acc-> ",actual_acc[rules[common_rule[i]-1][1]]," the minimum is :",rule_memb[i])

#find the max of the rules selected
if rule_memb[0]==rule_memb[1]:
    print("Both the rules satisfy")
    throt_out=[rules[common_rule[0]-1][2],rules[common_rule[1]-1][2]]
    print("Throttle is in :",throt_out)
else:
    res=max(rule_memb[0],rule_memb[1])
    print(res)

'''DEFUZZIFICATION'''
print(throt_out[0]," -> ",Thro_fuzzy[throt_out[0]][1:])
print(throt_out[1]," -> ",Thro_fuzzy[throt_out[1]][1:])

# Define the triangle coordinates
PM = [159, 191, 223]
PS = [127, 159, 191]

PM_membership = 0.15625
PS_membership = 0.15625

x = np.linspace(100, 250, 1000)


a, b, c = PM
PM_y = np.maximum(0, np.minimum((x - PM[0]) / (PM[1] - PM[0]), (PM[2] - x) / (PM[2] - PM[1])))
a, b, c = PS
PS_y = np.maximum(0, np.minimum((x - PS[0]) / (PS[1] - PS[0]), (PS[2] - x) / (PS[2] - PS[1])))

# Calculate the centroid of sums
centroid_of_sums = (sum(x * PM_y) + sum(x * PS_y)) / (sum(PM_y) + sum(PS_y))

plt.figure(figsize=(10, 6))
plt.plot(x, PM_y, label='PM')
plt.axhline(y=0.15625, color='b', linestyle='--', label='Intersection Membership Value')
plt.plot(x, PS_y, label='PS')

plt.axvline(x=centroid_of_sums, color='red', linestyle='--', label='Centroid of Sums')

plt.scatter([centroid_of_sums], [0.15625], color='green', label='Intersection')

plt.xlabel('Throttle')
plt.ylabel('Membership')
plt.title('Fuzzy Speed Sets')
plt.legend()
plt.grid(True)
plt.show()

print("Defuzzified value (centroid of sums):", centroid_of_sums)
