#!/usr/bin/env python
# coding: utf-8

# # No-Show Appointments Data Set Analysis

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 
os.chdir("E:\\Learning Videos\\EGFWD Professional\\Project2")


# ## Read Data

# In[2]:


mdf=pd.read_csv("./noshowappointments-kagglev2-may-2016.csv")


# ## Check data

# In[3]:


mdf.head()


# In[4]:


mdf.dtypes


# ## Convert Columns' names to lower case 

# In[5]:


mdf=mdf.rename(axis='columns',mapper=lambda x:x.lower())
mdf.columns


# ## Check unique values for columns

# In[6]:


mdf['scholarship'].nunique()


# In[7]:


mdf['diabetes'].nunique()


# In[8]:


mdf['hipertension'].nunique()


# In[9]:


mdf['gender'].nunique()


# In[10]:


mdf['alcoholism'].nunique()


# In[11]:


mdf['sms_received'].nunique()


# In[12]:


mdf['handcap'].nunique()


# In[13]:


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

# In[14]:


mdf['scheduledday']=pd.to_datetime(mdf['scheduledday'])
mdf['appointmentday']=pd.to_datetime(mdf['appointmentday'])
mdf['sms_received']=mdf['sms_received'].astype(bool)
mdf['scholarship']=mdf['scholarship'].astype(bool)
mdf['handcap']=mdf['handcap'].astype(bool)
mdf['diabetes']=mdf['diabetes'].astype(bool)
mdf['alcoholism']=mdf['alcoholism'].astype(bool)
mdf['hipertension']=mdf['hipertension'].astype(bool)


# In[15]:


mdf.dtypes


# ## Extract the week day name & Hour & Hour & Month name from scheduledday column

# In[16]:


mdf['hour']=mdf['scheduledday'].dt.hour
mdf['month']=mdf['scheduledday'].dt.month_name()
mdf['week_day']=mdf['scheduledday'].dt.day_name()


# ## Analysis Phase :
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
# 

# In[127]:


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

# In[18]:


mdf['neighbourhood'].mode()[0]


# ##### What is the common gender in the dataset ?
# 

# In[19]:


get_common_gender(mdf)


# ##### What is the common month in the dataset ?

# In[20]:


get_common_month(mdf)


# ##### What is the common day in the dataset ?

# In[21]:


get_common_weekday(mdf)


# ##### was it is the common to receive_sms in the dataset ?

# In[22]:


is_it_common_to_receive_sms(mdf)


# In[23]:


mdf['no-show'].value_counts().plot(kind='pie',subplots='True')


# From the above figure it isn't common to make no-show appoointments.

# #### Scholarship Group:

# In[24]:


scholarshipdf=mdf[mdf['scholarship']==True]
scholarshipdf.head()


# ##### What is the common weekday for scholarship group?

# In[25]:


get_common_weekday(scholarshipdf)


# ##### What is the common Month for scholarship group?

# In[26]:


get_common_month(scholarshipdf)


# ##### What is the common Neighbourhood for scholarship group?

# In[27]:


get_common_neighbourhood(scholarshipdf)


# ##### What is the common gender for scholarship group?

# In[28]:


get_common_gender(scholarshipdf)


# ##### was it common to receive SMS for Scholarship group ?

# In[29]:


is_it_common_to_receive_sms(scholarshipdf)


# #### What is the gender distribution for scholarship group ?

# In[30]:


scholarship_gender_distribution=get_gender_distribution(scholarshipdf)
plt.title('Gender Distribution for scholarship group')
plt.pie(scholarship_gender_distribution['gender'],labels=['Female','Male'],colors=['pink','lightblue'])
plt.show()


# #### What is the SMS distribution for Scholarship Group ?

# In[31]:


sms_scholarship_distribution=get_sms_distribution(scholarshipdf)
sms_scholarship_distribution.head()


# In[32]:


plt.title("SMS Distribution ")
plt.pie(sms_scholarship_distribution['sms_received'],labels=['Not Received','Received'],colors=['red','green'])
plt.show()


# #### Which scholarship gender make show appointment more ?

# In[33]:


schloarship_showdf=scholarshipdf[scholarshipdf['no-show']=='No']
get_common_gender(schloarship_showdf)


# #### which neighbourhood that has show appointment for schlorship Patient?

# In[34]:


get_common_neighbourhood(schloarship_showdf)


# #### which month that has show appointment for scholarship Patient ?

# In[35]:


get_common_month(schloarship_showdf)


# #### which common_day for show appointment for scholarship Patient ?

# In[36]:


get_common_weekday(schloarship_showdf)


# #### which gender distribution for show appointment for scholarship Patient?

# In[37]:


show_scholarship_gender_df=get_gender_distribution(schloarship_showdf)


# In[38]:


plt.title("Gender Distribution for Scholarship Patients")
plt.pie(show_scholarship_gender_df['gender'],labels=['Female','Male'],colors=['pink','lightblue'])


# In[39]:


show_scholarship_df.head()


# #### which hour is common for show schlarship Patient ? 

# In[40]:


get_common_hour(schloarship_showdf)


# #### No SHow appointment for Scholarship patient

# In[41]:


no_show_scholarship_df=scholarshipdf[scholarshipdf['no-show']=='Yes']


# #### Which gender is common to make no-show appointment for scholarship group ?

# In[42]:


get_common_gender(no_show_scholarship_df)


# #### Which neighbourhood is common to make no-show appointment for scholarship group?

# In[43]:


get_common_neighbourhood(no_show_scholarship_df)


# In[44]:


scholarship_no_show_sms=get_sms_distribution(no_show_scholarship_df)
scholarship_no_show_sms.head()


# In[45]:


plt.title("SMS Distribution for no-show Scholarship")
plt.pie(scholarship_no_show_sms['sms_received'],labels=['Not-Received','Recevied'],colors=['red','green'])
plt.show()


# #### what is the common day for no-show appointment for scholarship group?

# In[46]:


get_common_weekday(no_show_scholarship_df)


# #### what is the common month for no-show appointment for scholarship group?

# In[47]:


get_common_month(no_show_scholarship_df)


# #### Top 10 Neighbourhood for Scholarship

# In[73]:


neighbourhood_schlorship_distribution=get_neighbourhood_distribution(scholarshipdf)
neighbourhood_distribution.plot(kind='bar',ylabel='Number of Patients',xlabel='Neighbourhood',title='Common Scholarship Neighbourhood')


# ## Alcoholism

# In[49]:


alcoholism_df=mdf[mdf['alcoholism']==True]
alcoholism_df.head()


# In[ ]:


### what is the common Gender


# In[50]:


get_common_gender(alcoholism_df)


# In[56]:


gender_distribution_alcoholism=get_gender_distribution(alcoholism_df)
plt.title("Gender Distribution for Alcoholism")
plt.pie(gender_distribution_alcoholism['gender'],colors=['lightblue','pink'],labels=['Male','Female'])


# In[ ]:


####


# In[57]:


sms_alcoholism_distribtuion=get_sms_distribution(alcoholism_df)


# In[59]:


plt.title("SMS Distribution for Alcoholism")
plt.pie(sms_scholarship_distribution['sms_received'],colors=['red','green'],labels=['No-Received','Received'])


# In[60]:


get_common_month(alcoholism_df)


# In[61]:


get_common_weekday(alcoholism_df)


# In[62]:


get_common_hour(alcoholism_df)


# In[63]:


get_common_neighbourhood(alcoholism_df)


# In[71]:


neighbourhood_distribution=get_neighbourhood_distribution(alcoholism_df)
neighbourhood_distribution.plot(kind='bar',xlabel='Neighbourhood',ylabel='Number of Patients',title="Top 10 Alcoholism Neighbourhood")


# In[77]:


show_alcoholism_df=get_show(alcoholism_df)


# In[78]:


get_common_neighbourhood(show_alcoholism_df)


# In[79]:


get_common_weekday(show_alcoholism_df)


# In[80]:


get_common_month(show_alcoholism_df)


# In[81]:


get_common_hour(show_alcoholism_df)


# In[84]:


show_gender_distribtuion_alcoholism=get_gender_distribution(show_alcoholism_df)
show_gender_distribtuion_alcoholism


# In[86]:


plt.pie(show_gender_distribtuion_alcoholism['gender'],labels=['Male','Female'],colors=['lightblue','pink'])


# In[89]:


neighbourhood_distribution_show_alcoholism=get_neighbourhood_distribution(show_alcoholism_df)
neighbourhood_distribution_show_alcoholism.plot(kind='bar',title='Top 10 Neighbourhood Show Distribution Alcoholism ',xlabel="Neighbourhood",ylabel='Number of Patients')


# In[103]:


show_sms_distribution_alcoholism=get_sms_distribution(show_alcoholism_df)
show_sms_distribution_alcoholism


# In[ ]:


### No Show Alocoholism 


# In[90]:



alocholism_no_show=get_no_show(alcoholism_df)


# In[91]:


get_common_gender(alocholism_no_show)


# In[92]:


get_common_month(alocholism_no_show)


# In[93]:


get_common_weekday(alocholism_no_show)


# In[94]:


get_common_hour(alocholism_no_show)


# In[97]:


gender_distribution_no_show_alcoholism=get_gender_distribution(alocholism_no_show)
gender_distribution_no_show_alcoholism


# In[99]:


plt.title("Gender Distribtuion for no-show Alcoholism Patients")
plt.pie(gender_distribution_no_show_alcoholism['gender'],labels=['Male','Femal'],colors=['lightblue','pink'])


# In[101]:


sms_distribution_for_no_show_alcoholism=get_sms_distribution(alocholism_no_show)
sms_distribution_for_no_show_alcoholism


# In[ ]:


### Handcap Patient


# In[104]:


handcap_df=mdf[mdf['handcap']==True]


# In[105]:


get_common_gender(handcap_df)


# In[106]:


get_common_neighbourhood(handcap_df)


# In[107]:


get_common_month(handcap_df)


# In[108]:


get_common_hour(handcap_df)


# In[109]:


get_common_weekday(handcap_df)


# In[112]:


neighbourhood_distribution_handcap=get_neighbourhood_distribution(handcap_df)
neighbourhood_distribution_handcap.plot(kind='bar',ylabel="Number of Patient",title="Top 10 handcap Neighbourhood",xlabel="Neighbourhood")


# In[113]:


get_sms_distribution(handcap_df)


# In[114]:


handcap_show_df=get_show(handcap_df)


# In[115]:


get_common_hour(handcap_show_df)


# In[116]:


get_common_month(handcap_show_df)


# In[117]:


get_common_hour(handcap_show_df)


# In[118]:


get_common_weekday(handcap_show_df)


# In[137]:


get_neighbourhood_distribution(handcap_show_df,"Handcap show appointment ")


# In[ ]:


### No show handcap


# In[129]:


no_show_handcap=get_no_show(handcap_df)


# In[130]:


get_sms_distribution(no_show_handcap)


# In[131]:


get_common_gender(no_show_handcap)


# In[132]:


get_common_weekday(no_show_handcap)


# In[133]:


get_common_hour(no_show_handcap)


# In[134]:


get_common_month(no_show_handcap)


# In[138]:


get_neighbourhood_distribution(no_show_handcap,"Handcap no show appointment ")


# ### Diabetes

# In[136]:


diabetes_df=mdf[mdf['diabetes']==True]


# In[141]:


get_common_gender(diabetes_df)


# In[139]:


get_common_weekday(diabetes_df)


# In[140]:


get_common_month(diabetes_df)


# In[142]:


get_sms_distribution(diabetes_df)


# In[143]:


get_neighbourhood_distribution(diabetes_df,'Diabetes ')


# In[144]:


get_gender_distribution(diabetes_df)


# In[ ]:


### show diabetes


# In[145]:


show_diabetes=get_show(diabetes_df)


# In[146]:


get_common_gender(show_diabetes)


# In[147]:


get_common_weekday(show_diabetes)


# In[148]:


get_common_month(show_diabetes)


# In[149]:


get_common_hour(show_diabetes)


# In[152]:


get_common_neighbourhood(show_diabetes)


# In[151]:


get_neighbourhood_distribution(show_diabetes,"Show appointment diabetes ")


# In[ ]:


## No show diabetes


# In[153]:


no_show_diabetes=get_no_show(diabetes_df)


# In[154]:


get_sms_distribution(no_show_diabetes)


# In[156]:


get_common_weekday(no_show_diabetes)


# In[157]:


get_common_month(no_show_diabetes)


# In[158]:


get_common_hour(no_show_diabetes)


# In[159]:


get_gender_distribution(no_show_diabetes)


# In[160]:


get_sms_distribution(no_show_diabetes)


# In[161]:


get_common_neighbourhood(no_show_diabetes)


# In[163]:


get_neighbourhood_distribution(no_show_diabetes,"No Show Appointment Diabetes")


# In[ ]:


### Handcap & Scholarship & Diabetes


# In[165]:


scholarship_hand_diabetes_df=mdf[mdf['diabetes']==True]
scholarship_hand_diabetes_df=scholarship_hand_diabetes_df[scholarship_hand_diabetes_df['scholarship']==True]
scholarship_hand_diabetes_df[scholarship_hand_diabetes_df['handcap']== True]


# In[166]:


get_common_gender(scholarship_hand_diabetes_df)


# In[167]:


get_common_neighbourhood(scholarship_hand_diabetes_df)


# In[169]:


get_neighbourhood_distribution(scholarship_hand_diabetes_df,"Handcap & Diabetes & Scholarship Patient ")


# In[170]:


get_sms_distribution(scholarship_hand_diabetes_df)


# In[171]:


show_diabetes_hand_scholarship_df=get_show(scholarship_hand_diabetes_df)


# In[172]:


get_common_gender(show_diabetes_hand_scholarship_df)


# In[173]:


get_common_hour(show_diabetes_hand_scholarship_df)


# In[174]:


get_common_weekday(show_diabetes_hand_scholarship_df)


# In[175]:


get_common_neighbourhood(show_diabetes_hand_scholarship_df)


# In[177]:


get_neighbourhood_distribution(show_diabetes_hand_scholarship_df,"Show Handcap & Scholarship & diabetes Patients ")


# In[178]:


no_show_diabetes_hand_scholarship_df=get_no_show(scholarship_hand_diabetes_df)


# In[181]:


get_common_gender(no_show_diabetes_hand_scholarship_df)


# In[180]:


get_gender_distribution(no_show_diabetes_hand_scholarship_df)


# In[182]:


get_common_neighbourhood(no_show_diabetes_hand_scholarship_df)


# In[184]:


get_neighbourhood_distribution(no_show_diabetes_hand_scholarship_df,"No Show appointment for handcap & diabetes & scholarship Patient ")


# ### Hipertension Group 

# In[185]:


hipertesion=mdf[mdf['hipertension']==True]


# In[ ]:


get_common_gender(hipertesion)


# In[186]:


get_common_hour(hipertesion)


# In[187]:


get_common_neighbourhood(hipertesion)


# In[189]:


get_common_weekday(hipertesion)


# In[190]:


get_common_month(hipertesion)


# In[191]:


get_gender_distribution(hipertesion)


# In[192]:


get_sms_distribution(hipertesion)


# ### Show Hipertension

# In[193]:


show_hipertension=get_show(hipertesion)


# In[195]:


get_common_hour(show_hipertension)


# In[197]:


get_common_weekday(show_hipertension)


# In[198]:


get_common_month(show_hipertension)


# In[199]:


get_common_gender(show_hipertension)


# In[200]:


get_gender_distribution(show_hipertension)


# In[208]:


get_neighbourhood_distribution(show_hipertension,'Show Hipertnesion Appointment ')


# ### No SHow Hipertension 

# In[201]:


no_show_hipertension=get_no_show(hipertesion)


# In[202]:


get_common_hour(no_show_hipertension)


# In[203]:


get_common_month(no_show_hipertension)


# In[204]:


get_common_weekday(no_show_hipertension)


# In[205]:


get_sms_distribution(no_show_hipertension)


# In[206]:


get_gender_distribution(no_show_hipertension)


# In[207]:


get_neighbourhood_distribution(no_show_hipertension,"No Show Hipertension Appointment ")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




