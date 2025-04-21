import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#question number 1
#1.1  Read
data=pd.read_csv("bikes.csv")
#1.2 Check head 
print(data.head())
#1.3 Check summary statistics
print(data.describe())

#1.4 plot the daily attendance of two tracks, 'Berri1', 'PierDup
x=data['Date']
y=data[['PierDup','Berri1']]
plt.plot(x,y)

#1.5 Check index , explore weekday_name attributes
#here to.datetime() method is use to create date object to string format day/month/year
data['Date']=pd.to_datetime(data['Date'],format="%d/%m/%Y")
#based on the date calculated the day using day_name() thus we get the weekday_name and created extra attributes
#inside the data
data['weekday_name']=data['Date'].dt.day_name() 

#1.6  Get sum of all attendance as a function of the weekday
weekday_attendance=data.groupby('weekday_name')
weekday_attendance=weekday_attendance[["Berri1","CSC","Mais1","Mais2","Parc","PierDup","Rachel1","Totem_Laurier" ]].sum()

#1.7 Display this in figure , what is the inference?
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_attendance.plot(kind='bar')
plt.xlabel('Weekday')
plt.ylabel('Total Attendance')

#question number 2 Titanic-https://www.kaggle.com/c/titanic/data Database of whether somebody survived or notCan you infer who has survived ?
#2.1. Load the data
titanic=pd.read_csv("titanic_train.csv")
print(titanic.head())
2. Which gender survived more 
df=pd.DataFrame(titanic)
df =titanic.groupby('sex')['survived'].sum()
print(df.idxmax())

#3. Does it depend on pclass? as passenger belong to one of the class so all the 
#passenger have three types class 1 class 2 class3
per=titanic.groupby(['pclass','sex']).count()
print(per['survived'])
print(per['survived'].sum())

#4. can we see % of survival of each gender and pclass What is your inference? 
# percentage for class 1 female passanger
per=titanic.groupby(['pclass','sex']).count()
pclass1female=per.loc[(1,'female')]
print((pclass1female['survived']/per['survived'].sum())*100)

# percentage for class 1 male passanger
pclassmale1=per.loc[(1,'male')]
print((pclassmale1['survived']/per['survived'].sum())*100)

# percentage for class 2 female passanger
per=titanic.groupby(['pclass','sex']).count()
pclass1female=per.loc[(2,'female')]
print((pclass1female['survived']/per['survived'].sum())*100)

# percentage for class 2 male passanger
pclassmale1=per.loc[(2,'male')]
print((pclassmale1['survived']/per['survived'].sum())*100)

# percentage for class 3 female passanger
per=titanic.groupby(['pclass','sex']).count()
pclass1female=per.loc[(3,'female')]
print((pclass1female['survived']/per['survived'].sum())*100)

# percentage for class 3 male passanger
pclassmale1=per.loc[(3,'male')]
print((pclassmale1['survived']/per['survived'].sum())*100)

#question 3 Roger Federer database Each row corresponds to a ATP match played by Roger Federer
#Can you infer anything on Roger Federer performance? player = 'Roger Federer'
#1. Read and check data 
data=pd.read_csv("federer.csv")
df=pd.DataFrame(data)
print(df.head(5))

# 2. How many % of matched won by our player? ('winner')

match_win=df[df['winner']=='Roger Federer']
win_per=(len(match_win)/df_len)*100
print(win_per)

# 3. Proportion of double faults wrt total points in each match This number is an indicator of the player's state of mind,
# his level of self-confidence,his willingness to take risks while serving, and other parameters.columns:
#'player1 double faults' and 'player1 total points total'Display simple stats of above 
df['double_fault_ratio'] = df['player1 double faults'] / df['player1 total points total']
print(df['double_fault_ratio'].describe())

# 4. Average Win per surface
df['Roger_Federer_win']=df['winner']=='Roger Federer'
surface=df.groupby('surface')['Roger_Federer_win'].mean()*100
print(surface)

#5. Display the proportion of double faults as a function of the tournament date, 'start date'
# Trend: display average double faults in each year 
df['start date'] = pd.to_datetime(df['start date'], format='%d.%m.%Y')
df['year'] = df['start date'].dt.year
df['double_fault_ratio'] = df['player1 double faults'] / df['player1 total points total']
avg_double_faults_per_year = df.groupby('year')['double_fault_ratio'].mean()
avg_double_faults_per_year.plot(kind='line', marker='o')
plt.title('Average Double Fault Ratio per Year')
plt.xlabel('Year')
plt.ylabel('Average Double Fault Ratio')

# question no 4 Create two frequencies 5Hz and 50Hz sin signals Draw FFT components 
#4.1 sin signals frequencies 5Hz 
fs=1000
t=np.linspace(0,1,fs)
sig_5hz=np.sin(2*np.pi*5*t)
plt.plot(t,sig_5hz)
#4.2 sin signals frequencies 50Hz sin signals
fs=1000
t=np.linspace(0,1,fs)
sig_50hz=np.sin(2*np.pi*50*t)
plt.plot(t,sig_50hz)
#4.3 FFT frequencies 5Hz 
fs=1000
t=np.linspace(0,1,fs)
sig_5hz=np.sin(2*np.pi*5*t)
fft_5hz=np.fft.fft(sig_5hz)
fft_mag_5hz=np.abs(fft_5hz)
freq_5hz=np.fft.fftfreq(len(t),1/fs)
plt.plot(freq_5hz[:fs//2],fft_mag_5hz[:fs//2])
#4.4 FFT frequencies 50Hz
fs=1000
t=np.linspace(0,1,fs)
sig_50hz=np.sin(2*np.pi*50*t)
fft_50hz=np.fft.fft(sig_50hz)
fft_mag_50hz=np.abs(fft_50hz)
freq_50hz=np.fft.fftfreq(len(t),1/fs)
plt.plot(freq_50hz[:fs//2],fft_mag_50hz[:fs//2])

# 5 questionPlotting normal random numbers and show that addition of two Gaussian is Gaussian and addition of all is Gaussian
#first gaussian
size=1000
mean=0
std=1
gau1=np.random.normal(mean,std,size)
plt.hist(gau1,bins=50,alpha=0.6)
plt.xlabel("Value")
plt.ylabel("Density")

#second gaussian

size=1000
mean=2
std=3
gau2=np.random.normal(mean,std,size)
plt.hist(gau2,bins=50,alpha=0.6)
plt.xlabel("Value")
plt.ylabel("Density")

# sum of two gaussian
sum=gau1+gau2
plt.hist(sum,bins=50,alpha=0.6)
plt.xlabel("Value")
plt.ylabel("Density")

# adding all the gaussian
all=sum+gau1+gau2
all=sum+gau1+gau2
size=1000
mean=2
std=3
plt.hist(all,bins=50,alpha=0.6)
plt.xlabel("Value")
plt.ylabel("Density")
