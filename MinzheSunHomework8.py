#MinzheSunHomework8
#(import modules)
import pandas as pd
import datetime
import matplotlib.pyplot as plot
from PIL import Image


# 1st fuction for searching expired date(Python function)
def Exdate(License):
        file=pd.read_csv('new_dog.csv',header=0)
       
        find=0
        while License!='' and find==0:# a loop can leave the fuction by input enter
            try:
                License=int(License)# data type change
                for num in file['Number']:
                    if num==License:
                        row=file[(file['Number']==num)]# which row it locates at
                        Exdate=row['ExpiredDate'].values[0]
                        result='The dog license will expire at\t'+Exdate
                        return(result)
                        find=1# change the status to end the loop
                if find==0:
                    License=input('The number is wrong, please input again.\nPlease input the dog license number:\n>>')
                    # input another number after not finding number
            except ValueError:# help to control the correct data type
                print('You input a wrong number form')
                License=input('Please input the dog license number or enter to exit:\n>>')
                continue

#----------------------cite from STOCKOVERFLOW-------------------------------------------------
def validate(a):
    try:
        datetime.datetime.strptime(a, '%m/%d/%Y')
        return (True)
    except ValueError:
        return (False)             #  to help me find is it a valid date format
#-----------------------------------------------------------------------------------------
#Because the original dataset is too big, so I randomly select 20000 samples from the original dataset
dog_url="NYC_Dog.csv"
file=pd.read_csv(dog_url,header=0)
file['Number']=file['Number'].astype(int)
file=file.set_index(['Number'])
sampleFile=file.sample(n=20000)
testNumber=sampleFile.index.values.tolist()[0:4]
sampleFile.to_csv('new_dog.csv')
print('Hi,welcome to the New York Dog Dataset,please input which kind of information you would like to serach:\n')
print('1.When does your dog\'s dog license expire?')
print('2.Add a new dog license to the dataset')
print('3.The numbers of dogs birth in different years?')
print('4.Which district is more suitable to advertise the products about dogs?')
#print('5.which place is more suitable to establish a dog hospital?')     
#f.user input and a.data type
inputnumber=input('Please enter the function number you want to use:\n>>')
##c.control flow: if
if inputnumber=='1':
     print('You can use randomly selected number:',testNumber,' or input by yourselt to test the function')
     License=input('Please input the dog license number or enter to exit:\n>>')
     #call my own fuction
     exdate=Exdate(License)
     print(exdate)
#------------------------------------function2----------------------------------------------
elif inputnumber=='2':
    number=input('Please input your dog\'License number or enter to exit:\n>>')
    Name=input('Please input your dog\'License name:\n>>')
    Gen=input('Please input your dog\'License gender:\n>>')
    Birth=input('Please input your dog\'License birth:\n>>')
    Breed=input('Please input your dog\'License breed:\n>>')
    Zip=input('Please input your dog\'License zipcode:\n>>')
    Issue=input('Please input your dog\'License Issuedate, date form like:9/12/2014:\n>>')
    Expire=input('Please input your dog\'License Expiredate,date form like:9/12/2014:\n>>')
    statusNum=False
    statusBirth=False
    numberList=sampleFile.index.values.tolist()
    while number!='' and statusNum==False:
        try:
            number=int(number)
            if number in numberList:
                print('The number has already exited')
                statusNum=False
            else:
                statusNum=True
                Number=number
            if statusNum==False:
                number=input('Please input your dog\'License number again or enter to exit:\n>>')             
        except ValueError:# help to control the correct data type
                print('You input a wrong number form')
                number=input('Please input the dog license number or enter to exit:\n>>')
                continue
    while Name=='':
        print('Name cannot be null')
        Name=input('Please input your dog\'License name again:\n>>')
    while Gen=='':
        print('Gender cannot be null')
        Gen=input('Please input your dog\'License gender again(F OR M):\n>>')
    while Gen not in ['F','M']:
        print('Gender form is wrong')
        Gen=input('Please input your dog\'License gender again(F OR M):\n>>')
    while statusBirth==False:# loop to choose the correct year and format
        try:
            if Birth!='' and int(Birth)>2005 and int(Birth)<2019:
                Birth=Birth
                statusBirth=True
            else:
                print('Wrong Birthday date')
                Birth=input('Please input your dog\'License birth again:\n>>')
        except ValueError:# help to control the correct data type
            print('You input a wrong Birth form')
            Birth=input('Please input your dog\'License birth again:\n>>')
            continue
    while Breed==''or Breed.isdigit()==True:
        print('Wrong breed name')
        Breed=input('Please input your dog\'License breed name again:\n>>')
    while Zip=='' or Zip.isdigit()==False or len(Zip)!=5:
        print('Wrong Zipcode')
        Zip=input('Please input your dog\'License zipcode again:\n>>')
    while Issue=='' or validate(Issue)==False:
        print('Wrong Issue date')
        Issue=input('Please input your dog\'License Issuedate again,date form like:9/12/2014:\n>>')
    while Expire =='' or validate(Expire)==False:
        print('Wrong Expire date')
        Expire=input('Please input your dog\'License Expiredate again,date form like:9/12/2014:\n>>')
    sampleFile.index.append(pd.Index([Number]))
    sampleFile.loc[Number,'Name']=[Name]
    sampleFile.loc[Number,'Gender']=[Gen]
    sampleFile.loc[Number,'Birth']=[Birth]
    sampleFile.loc[Number,'Breed']=[Breed]
    sampleFile.loc[Number,'ZipCode']=[int(Zip)]
    sampleFile.loc[Number,'IssuedDate']=[Issue]
    sampleFile.loc[Number,'ExpiredDate']=[Expire]
    sampleFile.to_csv('new_dog.csv')
    print('Number:',Number,'Name:',Name,'Gender:',Gen,'Birth:',Birth,'Breed:',Breed,'ZipCode:',Zip,'IssuedDate:',Issue,'ExpiredDate:',Expire)
    print('record added successfully')
#-------------------------------------function3-------------------------------------------------------------------------------------------
elif inputnumber=='3':
    file=pd.read_csv('NYC_Dog.csv',header=0)
#I can pick the year from csv in a list,however,the year picked is not in order,and because limit of time, I dirctly write all the year.
    yearList=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
    birthList=[]
    n=0
    while n<len(yearList):
        birth=file[file.Birth==yearList[n]].Number.count()
        birthList.append(birth)
        n+=1
#------------------cited from the web analytic assignment1-------------------------------------------------------------
    plot.ylabel('The numbers of Birth')
    plot.xlabel('The different year')
    plot.plot(yearList,birthList,color='red',marker='o',linestyle='solid')
    plot.title('the numbers of Dog\'s birth in different years')
    plot.show()
#-----------------------------------------------function4-------------------------------------------------------
elif inputnumber=='4':
    file=pd.read_csv('NYC_Dog.csv',header=0)
    zipList=[]
    for code in file['ZipCode']:
        if code not in zipList:
            zipList.append(code)
    n=0
    value=0
    zipdict={}
    while n<len(zipList):
        zipNum=file[file.ZipCode==zipList[n]].Number.count()
        zipdict[zipList[n]]=zipNum
        if zipNum>value:
            value=zipNum
        n+=1
    for key in zipdict:
        if zipdict[key]==value:
            zipcode=key
    ziplace={10025:'10025.png'}
    print('The most suitable district to advertise dog products is',zipcode,'\nBecause the number of dogs is the most in this district, it has',zipdict[zipcode],'dogs')
    description={10025:'''ZIP code 10025 is located in southeast New York and covers a slightly less than average land area compared to other ZIP codes in the United States.
It also has an extremely large population density.The people living in ZIP code 10025 are primarily white.
The number of people in their late 20s to early 40s is extremely large while the number of young adults is large.
There are also an extremely large number of single adults and an extremely small number of families.
The percentage of children under 18 living in the 10025 ZIP code is extremely small compared to other areas of the country.'''}
    print(description[zipcode])
#----------------------------cited from cnblogs.com-----------------------------------------------------------
    img=Image.open(ziplace[zipcode])
    plot.figure("Dog-District")
    plot.imshow(img)
    plot.show()
#--------------------------------------------------------------------------------------------------------------    
#At first, I want to plot a heatmap by using folium package, however, it is hard for me to learn before the deadline.
#So I used the screenshot to diplay the final result. Because there are too many zipcode and description about them
#I just choose the most one, but I store it in a dictionary, so except the final picture, all code can use in the future when
#I learn how to plot heatmap.    
else:
    print('We do not have this function, program end')
    
    

   
            
    
    

        
    
       
     

                   
        
    
    
    
    
