#Assignment for Semantic Text Similarity


#Necessary imports

from sentence_transformers import SentenceTransformer, util
import numpy as np
import csv


#Loading Model
model = SentenceTransformer('stsb-roberta-large')


#Initialize all necessary variables in this section to debug run-time errors

sim_score_line = [0.0]*5000
fields = ['Unique_ID','Similarity_Score']
count = 0


#Loading and Transforming Dataset

print("Ln.No : Similarity Score")                                               #Print Line for Debugging purposes 
with open('Text_Similarity_Dataset.csv',newline='') as File :                   #CSV Dataset file has been opened into the variable 'File'
    reader = csv.reader(File)                                                   #Data from CSV file has been loaded to 'reader' variable in read format    
    for row in reader :
        if(row[0]!="Unique_ID") :
            first_line = row[1]
            second_line = row[2]
            emb1 = model.encode(first_line, convert_to_tensor=True)             #Encoding list of sentences to get their embeddings
            emb2 = model.encode(second_line, convert_to_tensor=True)
            cos_score = util.pytorch_cos_sim(emb1,emb2).item()                  #Computing Similarity score of two embeddings as cos_score
            sim_score_line[count] = cos_score
            print([count,sim_score_line[count]])                                #Print line to keep track of program running
            count = count + 1


#Write output scores with input number as "input_line_number : score" into CSV file

with open('Precily_Assessment_Punnoose.csv', 'w') as OpFile :
    writer = csv.writer(OpFile)                                                 #Creating Writer Object
    writer.writerow(fields)                                                     #Writing headings of fields
    for i in range(count) :
        writer.writerow([i,sim_score_line[i]])                                  #Writing Each row iteratively to Output File
        print("write complete : ",i)
