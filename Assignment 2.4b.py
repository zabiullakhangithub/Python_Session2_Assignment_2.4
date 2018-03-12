# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:56:25 2018

@author: zabiulla.khan

Problem Statement 2:
Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
"""

def filter_long_words(inputList,n):
    #instantiate a new empty list
    listOfWords = []

    # Loop through all the list items recieved as input
    for i in range(len(inputList)):
        # if the length if the list items is greater than input n, add it to the listOfWords
        if len(inputList[i]) > n:
            listOfWords.append(inputList[i])
    # return the filtered words greater then n
    return listOfWords

# Invoke the filter_long_words function and see the output
print(str(filter_long_words( ['Apple','Banana','Pineapple','Fig','Strawberry'],5)))