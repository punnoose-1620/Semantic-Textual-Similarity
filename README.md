# Semantic-Textual-Similarity
 This code was a part of an assessment by Precily for Natural Language Processing

# The assignment was performed using the Sentence Transformer directory of pretrained models for Semantic Textual Analysis in Python3. The model used is called ROBERTA-large and is one of the best models in the directory for semantic similarity analysis. The basic steps involed include :

1. Importing dataset csv file
	This included opening the csv file in read mode using the csv module and then reading the data into a reader variable.

2. Pre-processing data from csv file into 2 list variables after excluding the titles of columns
	This included using a for loop to separate each row of the data imported to the reader variable and then further assigning parts of this list data into seaparate lists for first and second sentences.

3. Processing the list variables to generate embeddings using encoding
	This includes using the encode class to generate embedded values of each sentence from each list and store them in new lists separately.

4. Computing the similarity scores of corresponding embeddings and storing them to another list variable
	This includes using the util class of the Sentence Transformer module to calculate the similarity between corresponding two sentences from the two embedded lists.
	The generated value is a floating point value that lies between 0 and 1 depending on the similarity of the sentences.

5. Creating a new csv file to write output to
	This includes creating a csv file in write mode using the csv module.

6. Writing title of each column to csv file
	This includes writing the title of the output data into the csv file.

7. Writing Unique_ID and Similarity score to csv file
	This includes the usage of the for loop to write the Unique_ID and Similarity score of each row of input to the output file as rows.



