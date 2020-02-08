import numpy as np
import pandas as pd
import matplotlib.pyplot as mplot
data=pd.read_csv('ks-projects.csv')
data=data.drop(['ID','usd pledged','usd_pledged_real','usd_goal_real'],axis=1)
i=data[((data.state == 'live') | (data.state == 'undefined') )].index
data=data.drop(i)

'''def barsuccessplotfor(x):
    bardata=data.x
    x = bardata
    x=x.values
    s_f=data['state']
    s_f=s_f.values
    b=list(set(x))
    scount=0
    fcount=0
    success_num=[]
    for i in range(len(b)):
        for j in range(len(x)):
            if b[i]==x[j]:
                if s_f[j]=='successful':
                    scount=scount+1
                else :
                
                    fcount=fcount+1
    
        success_num.append((scount/(fcount+scount))*100)
        fcount=0
        scount=0
            
    mplot.bar(b,success_num)
    
barsuccessplotfor(country)'''

#For country
country = data['country']
country=country.values
s_f=data['state']
s_f=s_f.values
b=list(set(country))
success_num=[]
for i in range(len(b)):
    fcount=0
    scount=0
    for j in range(len(country)):
        if b[i]==country[j]:
            if s_f[j]=='successful':
                scount=scount+1
            else :
                
                fcount=fcount+1
    
    success_num.append((scount/(fcount+scount))*100)
    

maxC=max(success_num) 
i=success_num.index(maxC)

#mplot.figure(0)  
mplot.figure(figsize=(12, 5))  # width:20, height:3  
mplot.bar(b,success_num, align='edge', width=0.5, alpha=0.9)

mplot.ylabel('Success Percentage')
mplot.title('Success percentage by country')
 
mplot.show()

print("The index of max success percentage country is",i)
print("The max successful country is",b[i])
print("The max success percentage is",maxC)

'''
#For category
category = data['category']
category=category.values
s_f=data['state']
s_f=s_f.values
b1=list(set(category))
scount=0
fcount=0
success_num1=[]
for i in range(len(b1)):
    for j in range(len(category)):
        if b1[i]==category[j]:
            if s_f[j]=='successful':
                scount=scount+1
            else :
                
                fcount=fcount+1
    
    success_num1.append((scount/(fcount+scount))*100)
    fcount=0
    scount=0
mplot.figure(1)            
mplot.bar(b1,success_num1)



print(data.goal)
print(data.state)
state=data.state
a=list(set(state))
print(a)
goal=data.goal
goal=goal.values
maxGoal=max(goal)
minGoal=min(goal)
print("The maximum Goal value is", maxGoal)
print("The minium Goal value is", minGoal)

goal = data.goal
goal=goal.values
print(goal)
s_f=data.state
s_f=s_f.values


success_num2=[]
for i in range(len(goal)):
    scount=0
    fcount=0
    for j in range(len(category)):
        if b1[i]==category[j]:
            if s_f[j]=='successful':
                scount=scount+1
            else :
                
                fcount=fcount+1
    
    success_num1.append((scount/(fcount+scount))*100)
  
    '''
#For main category    
main_category = data['main_category']
main_category=main_category.values
s_f=data['state']
s_f=s_f.values
d=list(set(main_category))

success_num3=[]
for i in range(len(d)):
    scount=0
    fcount=0
    for j in range(len(main_category)):
        if d[i]==main_category[j]:
            if s_f[j]=='successful':
                scount=scount+1
            else :
                
                fcount=fcount+1
    
    success_num3.append((scount/(fcount+scount))*100)
mplot.figure(2)            
   

mplot.figure(figsize=(16, 6))  # width:20, height:3  
mplot.bar(d,success_num3, align='center', width=0.5, alpha=0.9)


mplot.ylabel('Success Percentage')
mplot.title('Success Percentage by main category')
 
mplot.show()

'''
#for pledge/goal ratio
data1= data[data.state == 'successful']
print(data1.values)
ratio=[]
for i in range(len(data1)):
    ratio=ratio.append((data[i].pledge)/(data[i].goal))
print(ratio.values)


#for date difference
data=pd.read_csv("ks-projects.csv")
data=data.drop(data.columns[[0,1]],axis=1)
i=data[((data.state == 'live') | (data.state == 'undefined') )].index
data=data.drop(i)

data.launched=pd.to_datetime(data.launched)
data.deadline=pd.to_datetime(data.deadline)

launched=data.launched                           
launched=launched.values


deadline=data.deadline
deadline=deadline.values


print(deadline[0]-launched[0])

s_f=data['state']
s_f=s_f.values
scount=0
fcount=0
days=[]
for i in range(len(data)):
    
    insec=deadline[i]-launched[i]
    #x = np.timedelta64(insec, 'ns')
    #days = x.astype('timedelta64[D]')
    #indays=days / np.timedelta64(1, 'D')
    indays=insec/1000000000/60/60/24
    days.append(indays)
   #find for certain amount of days
    #if indays>30:
    if s_f[i]=='successful':
        scount=scount+1
    else :
        fcount=fcount+1

print (scount)
#print("The days difference between deadline and launched date is\n",days)
 


print("The days difference is ", days[0])'''



