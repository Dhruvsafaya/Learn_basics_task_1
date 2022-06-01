import pandas as pd
import numpy as np

k=1
t=int(input('Enter the number of test cases\n')) #number of test cases
while(t):
    instr=input('Enter the file name\n') #name of the file with .xlsx extension

    ins = pd.read_excel(instr, engine='openpyxl') 

    #lists to store the data from the excel file
    Name=[]
    Username=[]
    Chapter_Tag=[]
    Test_name=[]
    answered=[]
    correct=[]
    score=[]
    skipped=[]
    time_taken=[]
    wrong=[]

    #iterating through the dataframe
    for index, row in ins.iterrows():
        if(row['Concept Test 1 - score']!='-'):#if condition to check if the cell is empty
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Concept Test 1')
            answered.append(row['Concept Test 1 - answered'])
            correct.append(row['Concept Test 1- correct'])
            score.append(row['Concept Test 1 - score'])
            skipped.append(row['Concept Test 1- skipped'])
            time_taken.append(row['Concept Test 1 - time-taken (seconds)'])
            wrong.append(row['Concept Test 1- wrong'])

        if(row['Concept Test 2 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Concept Test 2')
            answered.append(row['Concept Test 2 - answered'])
            correct.append(row['Concept Test 2- correct'])
            score.append(row['Concept Test 2 - score'])
            skipped.append(row['Concept Test 2- skipped'])
            time_taken.append(row['Concept Test 2 - time-taken (seconds)'])
            wrong.append(row['Concept Test 2- wrong'])

        if(row['Concept Test 3 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Concept Test 3')
            answered.append(row['Concept Test 3 - answered'])
            correct.append(row['Concept Test 3- correct'])
            score.append(row['Concept Test 3 - score'])
            skipped.append(row['Concept Test 3- skipped'])
            time_taken.append(row['Concept Test 3 - time-taken (seconds)'])
            wrong.append(row['Concept Test 3- wrong'])

        if(row['Concept Test 4 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Concept Test 4')
            answered.append(row['Concept Test 4 - answered'])
            correct.append(row['Concept Test 4- correct'])
            score.append(row['Concept Test 4 - score'])
            skipped.append(row['Concept Test 4- skipped'])
            time_taken.append(row['Concept Test 4 - time-taken (seconds)'])
            wrong.append(row['Concept Test 4- wrong'])

        if(row['Concept Test 5 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Concept Test 5')
            answered.append(row['Concept Test 5 - answered'])
            correct.append(row['Concept Test 5- correct'])
            score.append(row['Concept Test 5 - score'])
            skipped.append(row['Concept Test 5- skipped'])
            time_taken.append(row['Concept Test 5 - time-taken (seconds)'])
            wrong.append(row['Concept Test 5- wrong'])

        if(row['Full Chapter Test 1 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Full Chapter Test 1')
            answered.append(row['Full Chapter Test 1 - answered'])
            correct.append(row['Full Chapter Test 1- correct'])
            score.append(row['Full Chapter Test 1 - score'])
            skipped.append(row['Full Chapter Test 1- skipped'])
            time_taken.append(row['Full Chapter Test 1 - time-taken (seconds)'])
            wrong.append(row['Full Chapter Test 1- wrong'])

        if(row['Full Chapter Test 2 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Full Chapter Test 2')
            answered.append(row['Full Chapter Test 2 - answered'])
            correct.append(row['Full Chapter Test 2- correct'])
            score.append(row['Full Chapter Test 2 - score'])
            skipped.append(row['Full Chapter Test 2- skipped'])
            time_taken.append(row['Full Chapter Test 2 - time-taken (seconds)'])
            wrong.append(row['Full Chapter Test 2- wrong'])

        if(row['Topic Test 1 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Topic Test 1')
            answered.append(row['Topic Test 1 - answered'])
            correct.append(row['Topic Test 1- correct'])
            score.append(row['Topic Test 1 - score'])
            skipped.append(row['Topic Test 1- skipped'])
            time_taken.append(row['Topic Test 1 - time-taken (seconds)'])
            wrong.append(row['Topic Test 1- wrong'])

        if(row['Topic Test 2 - score']!='-'):
            Name.append(row['Name'])
            Username.append(row['id'])
            Chapter_Tag.append(row['Chapter Tag'])
            Test_name.append('Topic Test 2')
            answered.append(row['Topic Test 2 - answered'])
            correct.append(row['Topic Test 2- correct'])
            score.append(row['Topic Test 2 - score'])
            skipped.append(row['Topic Test 2- skipped'])
            time_taken.append(row['Topic Test 2 - time-taken (seconds)'])
            wrong.append(row['Topic Test 2- wrong'])

    #making a dictionary from the lists previously made
    dict1={
        'Name': Name,
        'Username': Username,
        'Chapter Tag': Chapter_Tag,
        'Test_Name': Test_name,
        'answered': answered,
        'correct': correct,
        'score': score,
        'skipped': skipped,
        'time taken': time_taken,
        'wrong': wrong
    }

    out='output_'
    out += str(k)
    out += '.xlsx' #out represents the name of the file
    fil=pd.DataFrame(dict1) #making of dataframe from the dictionary
    fil.to_excel(out, index=False) #exporting a excel file from the dataframe
    t=t-1
    k=k+1 #here k is used to keep track of the number of outputs
