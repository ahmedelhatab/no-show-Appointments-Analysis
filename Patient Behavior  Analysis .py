#!/usr/bin/env python
# coding: utf-8

# # No-Show Appointments Data Set Analysis

# ## What are the questions that we will answer in our Analysis phase for this data set ?

# This phase will be divied to two phases the first phase will answer some public questions related to the whole dataset.  
# 1. what is the common neighbourhood in the dataset ?  
# 2. what is the common month in the dataset?  
# 3. what is the common weekday in the dataset?  
# 4. what is the common gender in the dataset?
# 5. was it common to receive sms in the dataset or not ?
# 6. was it comon to make no-show appointments ?
# The second phase the dataset will be divided to small groups and some questions will be answered to each group.
# - The first dataset is derived from the main dataset based on scholarship.  
# - The second dataset is derived from the main dataset based on hipertension.  
# - The third dataset is derived from the main dataset based on diabetes. 
# - The fourth dataset is derived from the main dataset based on alcoholism.  
# - The fifth dataset is derived from the main dataset based on alcoholism & Handcap & Schloarship 
# for each each dataset we will answer the following questions:  
# 1- What is the common gender for the group ?  
# 2- what is the common day for the group?   
# 3- what is the common hour for the group in schedulededday column?  
# 4- what is the common neighbourhood for the group?   
# 5- was it common to receive SMS for the group?  
# 6- what is the gender distribution for the group?   
# 7- what is the receving SMS distribution for the group?    
# Each group is divided into show appointment / no-show appointment and each group get the above questions answered.

# In[366]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 
os.chdir("E:\\Learning Videos\\EGYFWD\\Project2")


# ## Read Data

# In[367]:


mdf=pd.read_csv("./noshowappointments-kagglev2-may-2016.csv")


# ## Check data

# In[368]:


mdf.head()


# In[369]:


mdf.dtypes


# ## Convert Columns' names to lower case 

# In[370]:


mdf=mdf.rename(axis='columns',mapper=lambda x:x.lower())
mdf.columns


# ## Check unique values for columns

# In[371]:


mdf['scholarship'].nunique()


# In[372]:


mdf['diabetes'].nunique()


# In[373]:


mdf['hipertension'].nunique()


# In[374]:


mdf['gender'].nunique()


# In[375]:


mdf['alcoholism'].nunique()


# In[376]:


mdf['sms_received'].nunique()


# In[377]:


mdf['handcap'].nunique()


# In[378]:


mdf['appointmentday']


# ## Convert data types  
# In this phase will convert datatypes for some columns :  
# 1. handcap to boolean  
# 2. scholarship to boolean.   
# 3. hipertension to boolean.    
# 4. alcoholism to boolean.  
# 5. sms_received to boolean.   
# 6. diabetes to boolean.  
# 7. handcap to boolean.  
# 8. scheduledday to datetime .
# 9. appointmentday to datetime.  
# 

# In[379]:


mdf['scheduledday']=pd.to_datetime(mdf['scheduledday'])
mdf['appointmentday']=pd.to_datetime(mdf['appointmentday'])
mdf['sms_received']=mdf['sms_received'].astype(bool)
mdf['scholarship']=mdf['scholarship'].astype(bool)
mdf['handcap']=mdf['handcap'].astype(bool)
mdf['diabetes']=mdf['diabetes'].astype(bool)
mdf['alcoholism']=mdf['alcoholism'].astype(bool)
mdf['hipertension']=mdf['hipertension'].astype(bool)


# In[380]:


mdf.dtypes


# ## Extract the week day name & Hour & Hour & Month name from scheduledday column

# In[381]:


mdf['hour']=mdf['scheduledday'].dt.hour
mdf['month']=mdf['scheduledday'].dt.month_name()
mdf['week_day']=mdf['scheduledday'].dt.day_name()


# ## Analysis Phase :

# In[382]:


def get_female(df):
    female_df=DateFrame(df[df['gender']=='F'])
    return female_df
def get_common_month(df):
    common_month=df['month'].mode()[0]
    return common_month
def get_common_weekday(df):
    common_weekday=df['week_day'].mode()[0]
    return common_weekday
def get_male(df):
    male_df=DateFrame(df[df['gender']=='F'])
    return male_df
def get_common_neighbourhood(df):
    common_neighbourhood=df['neighbourhood'].mode()[0]
    return common_neighbourhood
def get_no_show(df):
    no_showdf=pd.DataFrame(df[df['no-show']=='Yes'])
    return no_showdf
def get_show(df):
    showdf=pd.DataFrame(df[df['no-show']=='No'])
    return showdf
def is_it_common_to_receive_sms(df):
    is_receving_sms=df['sms_received'].mode()[0]
    return is_receving_sms
def get_common_gender(df):
    common_gender=df['gender'].mode()[0]
    if common_gender=='F':
        return "Female"
    else:
        return "Male"
def is_common_noshow(df):
    is_common_noshowAppointment=df['no-show'].mode()[0]
    return is_common_noshowAppointment
def get_gender_distribution(df):
    gender_distribution=pd.DataFrame(df['gender'].value_counts())
    return gender_distribution
def get_sms_distribution(df):
    sms_distribution=pd.DataFrame(df['sms_received'].value_counts())
    return sms_distribution
def get_common_hour(df):
    common_hour=df['hour'].mode()[0]
    return common_hour
def get_neighbourhood_distribution(df,group):
    neighbourhood_distribution=pd.DataFrame(df['neighbourhood'].value_counts())
    neighbourhood_distribution=neighbourhood_distribution.head(10)
    title="Top 10 Neighbourhood Distribution "+str(group)+"Patient"
    plot_fig=neighbourhood_distribution.plot(kind='bar',ylabel="Number of Patients",xlabel='Neighbourhood',title=title)
    return plot_fig

    


# ### General Analysis

# ##### What is the common neighbourhood in the dataset ?

# In[383]:


mdf['neighbourhood'].mode()[0]


# ##### What is the common gender in the dataset ?
# 

# In[384]:


get_common_gender(mdf)


# ##### What is the common month in the dataset ?

# In[385]:


get_common_month(mdf)


# ##### What is the common day in the dataset ?

# In[386]:


get_common_weekday(mdf)


# ##### Was it is the common to receive_sms in the dataset ?

# In[387]:


is_it_common_to_receive_sms(mdf)


# In[388]:


mdf['no-show'].value_counts().plot(kind='pie',subplots='True')


# From the above figure it isn't common to make no-show appoointments.

# #### Scholarship Group:

# In[389]:


scholarshipdf=mdf[mdf['scholarship']==True]
scholarshipdf.head()


# ##### What is the common weekday for scholarship group?

# In[390]:


get_common_weekday(scholarshipdf)


# ##### What is the common Month for scholarship group?

# In[391]:


get_common_month(scholarshipdf)


# ##### What is the common Neighbourhood for scholarship group?

# In[392]:


get_common_neighbourhood(scholarshipdf)


# ##### What is the common gender for scholarship group?

# In[393]:


get_common_gender(scholarshipdf)


# ##### was it common to receive SMS for Scholarship group ?

# In[394]:


is_it_common_to_receive_sms(scholarshipdf)


# #### What is the gender distribution for scholarship group ?

# In[395]:


scholarship_gender_distribution=get_gender_distribution(scholarshipdf)
plt.title('Gender Distribution for scholarship group')
plt.pie(scholarship_gender_distribution['gender'],labels=['Female','Male'],colors=['pink','lightblue'])
plt.show()


# From the above figure the gender distribution for scholarship patients Females are more than Males.  

# #### What is the SMS distribution for Scholarship Group ?

# In[396]:


sms_scholarship_distribution=get_sms_distribution(scholarshipdf)
sms_scholarship_distribution.head()


# In[397]:


plt.title("SMS Distribution ")
plt.pie(sms_scholarship_distribution['sms_received'],labels=['Not Received','Received'],colors=['red','green'])
plt.show()


# From the above figure most of patients don't receive sms.  

# #### Which scholarship gender make show appointment more ?

# In[398]:


schloarship_showdf=scholarshipdf[scholarshipdf['no-show']=='No']
get_common_gender(schloarship_showdf)


# #### which neighbourhood that has show appointment for schlorship Patient?

# In[399]:


get_common_neighbourhood(schloarship_showdf)


# #### which month that has show appointment for scholarship Patient ?

# In[400]:


get_common_month(schloarship_showdf)


# #### which common_day for show appointment for scholarship Patient ?

# In[401]:


get_common_weekday(schloarship_showdf)


# #### which gender distribution for show appointment for scholarship Patient?

# In[402]:


show_scholarship_gender_df=get_gender_distribution(schloarship_showdf)
show_scholarship_gender_df


# In[403]:


plt.title("Gender Distribution for Scholarship Patients")
plt.pie(show_scholarship_gender_df['gender'],labels=['Female','Male'],colors=['pink','lightblue'])


# from the above figure females are more than males for scholarship show appointment patients.  

# In[404]:


schloarship_showdf.head()


# #### which hour is common for show schlarship Patient ? 

# In[405]:


get_common_hour(schloarship_showdf)


# #### No SHow appointment for Scholarship patient

# In[406]:


no_show_scholarship_df=scholarshipdf[scholarshipdf['no-show']=='Yes']


# #### Which gender is common to make no-show appointment for scholarship group ?

# In[407]:


get_common_gender(no_show_scholarship_df)


# #### Which neighbourhood is common to make no-show appointment for scholarship group?

# In[408]:


get_common_neighbourhood(no_show_scholarship_df)


# In[409]:


scholarship_no_show_sms=get_sms_distribution(no_show_scholarship_df)
scholarship_no_show_sms.head()


# In[410]:


plt.title("SMS Distribution for no-show Scholarship")
plt.pie(scholarship_no_show_sms['sms_received'],labels=['Not-Received','Recevied'],colors=['red','green'])
plt.show()


# From the above figure most of patients don't receive sms.  

# #### what is the common day for no-show appointment for scholarship group?

# In[411]:


get_common_weekday(no_show_scholarship_df)


# #### what is the common month for no-show appointment for scholarship group?

# In[412]:


get_common_month(no_show_scholarship_df)


# #### what is the common hour for no-show appointment for scholarship group?

# In[413]:


get_common_hour(no_show_scholarship_df)


# #### Top 10 Neighbourhood for Scholarship

# In[414]:


neighbourhood_schlorship_distribution=get_neighbourhood_distribution(scholarshipdf," Scholarship ")


# ## Alcoholism

# In[415]:


alcoholism_df=mdf[mdf['alcoholism']==True]
alcoholism_df.head()


# ### What is the common gender ?

# In[416]:


get_common_gender(alcoholism_df)


# In[417]:


gender_distribution_alcoholism=get_gender_distribution(alcoholism_df)
plt.title("Gender Distribution for Alcoholism")
plt.pie(gender_distribution_alcoholism['gender'],colors=['lightblue','pink'],labels=['Male','Female'])


# From the above figure the males are more than females for alcoholism patients

# In[418]:


sms_alcoholism_distribtuion=get_sms_distribution(alcoholism_df)


# In[419]:


plt.title("SMS Distribution for Alcoholism")
plt.pie(sms_scholarship_distribution['sms_received'],colors=['red','green'],labels=['No-Received','Received'])


# From the above figure most of patients don't receive sms.  

# In[420]:


get_common_month(alcoholism_df)


# In[421]:


get_common_weekday(alcoholism_df)


# In[422]:


get_common_hour(alcoholism_df)


# In[423]:


get_common_neighbourhood(alcoholism_df)


# In[424]:


neighbourhood_distribution=get_neighbourhood_distribution(alcoholism_df,"Alcoholism")


# In[425]:


show_alcoholism_df=get_show(alcoholism_df)


# In[426]:


get_common_neighbourhood(show_alcoholism_df)


# In[427]:


get_common_weekday(show_alcoholism_df)


# In[428]:


get_common_month(show_alcoholism_df)


# In[429]:


get_common_hour(show_alcoholism_df)


# In[430]:


show_gender_distribtuion_alcoholism=get_gender_distribution(show_alcoholism_df)
show_gender_distribtuion_alcoholism


# In[431]:


plt.pie(show_gender_distribtuion_alcoholism['gender'],labels=['Male','Female'],colors=['lightblue','pink'])


# From the above figure the males are more than females for make show appointments.

# In[432]:


neighbourhood_distribution_show_alcoholism=get_neighbourhood_distribution(show_alcoholism_df,"Alcoholism ")


# In[433]:


show_sms_distribution_alcoholism=get_sms_distribution(show_alcoholism_df)
show_sms_distribution_alcoholism


# ### No Show Alocoholism 

# In[434]:



alocholism_no_show=get_no_show(alcoholism_df)


# In[435]:


get_common_gender(alocholism_no_show)


# In[436]:


get_common_month(alocholism_no_show)


# In[437]:


get_common_weekday(alocholism_no_show)


# In[438]:


get_common_neighbourhood(alocholism_no_show)


# In[439]:


get_common_hour(alocholism_no_show)


# In[440]:


gender_distribution_no_show_alcoholism=get_gender_distribution(alocholism_no_show)
gender_distribution_no_show_alcoholism


# In[441]:


plt.title("Gender Distribtuion for no-show Alcoholism Patients")
plt.pie(gender_distribution_no_show_alcoholism['gender'],labels=['Male','Femal'],colors=['lightblue','pink'])


# From the above figure males are more than females for no show alcoholism patients.

# In[442]:


sms_distribution_for_no_show_alcoholism=get_sms_distribution(alocholism_no_show)
sms_distribution_for_no_show_alcoholism


# ### Handcap Patient

# In[443]:


handcap_df=mdf[mdf['handcap']==True]


# In[444]:


get_common_gender(handcap_df)


# In[445]:


get_common_neighbourhood(handcap_df)


# In[446]:


get_common_month(handcap_df)


# In[447]:


get_common_hour(handcap_df)


# In[448]:


get_common_weekday(handcap_df)


# In[449]:


neighbourhood_distribution_handcap=get_neighbourhood_distribution(handcap_df,"Handcap ")


# In[450]:


get_sms_distribution(handcap_df)


# In[451]:


handcap_show_df=get_show(handcap_df)


# In[452]:


get_common_hour(handcap_show_df)


# In[453]:


get_common_month(handcap_show_df)


# In[454]:


get_common_neighbourhood(handcap_show_df)


# In[455]:


get_common_weekday(handcap_show_df)


# In[456]:


get_common_gender(handcap_show_df)


# In[457]:


get_sms_distribution(handcap_show_df)


# In[458]:


get_neighbourhood_distribution(handcap_show_df,"Handcap show appointment ")


# In[459]:


### No show handcap


# In[460]:


no_show_handcap=get_no_show(handcap_df)


# In[461]:


get_sms_distribution(no_show_handcap)


# In[462]:


get_common_gender(no_show_handcap)


# In[463]:


get_common_weekday(no_show_handcap)


# In[464]:


get_common_hour(no_show_handcap)


# In[465]:


get_common_month(no_show_handcap)


# In[466]:


get_common_neighbourhood(no_show_handcap)


# In[467]:


get_sms_distribution(no_show_handcap)


# In[468]:


get_neighbourhood_distribution(no_show_handcap,"Handcap no show appointment ")


# ### Diabetes

# In[469]:


diabetes_df=mdf[mdf['diabetes']==True]


# In[470]:


get_common_gender(diabetes_df)


# In[471]:


get_common_weekday(diabetes_df)


# In[472]:


get_common_month(diabetes_df)


# In[473]:


get_sms_distribution(diabetes_df)


# In[474]:


get_neighbourhood_distribution(diabetes_df,'Diabetes ')


# In[475]:


get_gender_distribution(diabetes_df)


# ### show diabetes

# In[476]:


show_diabetes=get_show(diabetes_df)


# In[477]:


get_common_gender(show_diabetes)


# In[478]:


get_common_weekday(show_diabetes)


# In[479]:


get_common_month(show_diabetes)


# In[480]:


get_common_hour(show_diabetes)


# In[481]:


get_common_neighbourhood(show_diabetes)


# In[482]:


get_sms_distribution(show_diabetes)


# In[483]:


get_neighbourhood_distribution(show_diabetes,"Show appointment diabetes ")


# ## No show diabetes

# In[484]:


no_show_diabetes=get_no_show(diabetes_df)


# In[485]:


get_sms_distribution(no_show_diabetes)


# In[486]:


get_common_weekday(no_show_diabetes)


# In[487]:


get_common_month(no_show_diabetes)


# In[488]:


get_common_hour(no_show_diabetes)


# In[489]:


get_gender_distribution(no_show_diabetes)


# In[490]:


get_sms_distribution(no_show_diabetes)


# In[491]:


get_common_neighbourhood(no_show_diabetes)


# In[492]:


get_neighbourhood_distribution(no_show_diabetes,"No Show Appointment Diabetes ")


# In[493]:


### Handcap & Scholarship & Diabetes


# In[494]:


scholarship_hand_diabetes_df=mdf[mdf['diabetes']==True]
scholarship_hand_diabetes_df=scholarship_hand_diabetes_df[scholarship_hand_diabetes_df['scholarship']==True]
scholarship_hand_diabetes_df[scholarship_hand_diabetes_df['handcap']== True]


# In[495]:


get_common_gender(scholarship_hand_diabetes_df)


# In[496]:


get_common_neighbourhood(scholarship_hand_diabetes_df)


# In[497]:


get_neighbourhood_distribution(scholarship_hand_diabetes_df,"Handcap & Diabetes & Scholarship Patient ")


# In[498]:


get_sms_distribution(scholarship_hand_diabetes_df)


# In[499]:


show_diabetes_hand_scholarship_df=get_show(scholarship_hand_diabetes_df)


# In[500]:


get_common_gender(show_diabetes_hand_scholarship_df)


# In[501]:


get_common_hour(show_diabetes_hand_scholarship_df)


# In[502]:


get_common_weekday(show_diabetes_hand_scholarship_df)


# In[503]:


get_common_neighbourhood(show_diabetes_hand_scholarship_df)


# In[504]:


get_neighbourhood_distribution(show_diabetes_hand_scholarship_df,"Show Handcap & Scholarship & diabetes ")


# In[505]:


no_show_diabetes_hand_scholarship_df=get_no_show(scholarship_hand_diabetes_df)


# In[506]:


get_common_gender(no_show_diabetes_hand_scholarship_df)


# In[507]:


get_gender_distribution(no_show_diabetes_hand_scholarship_df)


# In[508]:


get_common_neighbourhood(no_show_diabetes_hand_scholarship_df)


# In[509]:


get_neighbourhood_distribution(no_show_diabetes_hand_scholarship_df,"No Show appointment for handcap & diabetes & scholarship  ")


# ### Hipertension Group 

# In[510]:


hipertesion=mdf[mdf['hipertension']==True]


# In[511]:


get_common_gender(hipertesion)


# In[512]:


get_common_hour(hipertesion)


# In[513]:


get_common_neighbourhood(hipertesion)


# In[514]:


get_common_weekday(hipertesion)


# In[515]:


get_common_month(hipertesion)


# In[516]:


get_gender_distribution(hipertesion)


# In[517]:


get_sms_distribution(hipertesion)


# ### Show Hipertension

# In[518]:


show_hipertension=get_show(hipertesion)


# ### What is the common hour for hipertension patients?

# In[519]:


get_common_hour(show_hipertension)


# ### What is the common day for hipertension patients?

# In[520]:


get_common_weekday(show_hipertension)


# ### What is the common month for hipertension patients?

# In[521]:


get_common_month(show_hipertension)


# ### What is the common gender for hipertension patients?

# In[522]:


get_common_gender(show_hipertension)


# In[523]:


get_gender_distribution(show_hipertension)


# In[524]:


get_sms_distribution(show_hipertension)


# ### What is the common neighbourhood for hipertension patients?

# In[525]:


get_common_neighbourhood(show_hipertension)


# In[526]:


get_neighbourhood_distribution(show_hipertension,'Show Hipertnesion Appointment ')


# ### No Show hipertension Patients

# In[527]:


no_show_hipertension=get_no_show(hipertesion)


# ### What is the common hour for No Show hipertension  patients?

# In[528]:


get_common_hour(no_show_hipertension)


# ### What is the common month for No Show hipertension  patients?

# In[529]:


get_common_month(no_show_hipertension)


# ### What is the common weekday for No Show hipertension  patients?

# In[530]:


get_common_weekday(no_show_hipertension)


# In[531]:


get_sms_distribution(no_show_hipertension)


# In[532]:


get_gender_distribution(no_show_hipertension)


# In[533]:


get_common_neighbourhood(no_show_hipertension)


# In[534]:


get_neighbourhood_distribution(no_show_hipertension,"No Show Hipertension Appointment ")


# ## Show Appointment For Hipertension Patients

# In[535]:


hipertension_show=get_show(hipertesion)
hipertension_show


# In[536]:


gender_distribution_hipertension_show=get_gender_distribution(hipertension_show)
gender_distribution_hipertension_show


# In[537]:


sms_distribution_show_hipertension=get_sms_distribution(hipertension_show)
sms_distribution_show_hipertension


# In[538]:


neighbourhood_show_hipertension_distribution=get_neighbourhood_distribution(hipertension_show,"show hipertension ")


# ### What is the common neighbourhood in show hipertension pateints?

# In[539]:


get_common_neighbourhood(hipertension_show)


# ### What is the common hour in show hipertension pateints?

# In[540]:


get_common_hour(hipertension_show)


# ### What is the common month in show hipertension patients ?

# In[541]:


get_common_month(hipertension_show)


# ## Conclusions

# - The most common show appointment is done on ***Tuesday*** 
# - The most common show appointment is done in ***May***
# - The most common show appointment is done at ***7 AM.***
# - Sending SMS to the patients has no impact and recommended to stop sending it and save this cost where most of show patients don't receive the SMS and come to the hospital.
# - it is recommended to reduce the vacations of medical staff on **Tuesday** or at least keep the full manpower in hospitals between **7 and 10 AM**.
# - Increase public Transportation to **"JARDIM DA PENHA"** Neighbourhood on Tuesday between **7 AM. and 11 AM.** since those times hipertension & Diabetes made most show appointment for this neighbourhood.
# - Increase police forces on Wednesday in **"SANTA MARTHA"** neighbourhood since alcoholism patients make their show appointments at 7 AM.
# - Incease  public Transportation with aids for hancap patients on Tuesday to **"SANTA MARTHA"** between 7 and 10 AM. since common handcap show appointment was in that time.
