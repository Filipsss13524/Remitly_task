## Remitly Internship 2024 - task
Write a method verifying the input JSON data. Input data format is defined as AWS::IAM::Role Policy. Input JSON might be read from a file. 

Method should return logical false if an input JSON Resource field contains a single asterisk and true in any other case. 

## Table of Contents
* [General info](#general info)
* [Setup](#setup)
* [Technologies](#technologies)

## General info
The project was made in two versions, with and without the use of the pandas library.
*resource_checker_pandas - using pandas (you can comment out this part of the code if needed)
*resource_checker_function - without using pandas

Sample test files have also been prepared:
*date.json - "*" in Resource
*date_v1.json - "text" in Resource
*date_v2.json - Error in name PolicyDocument
*date_v3.json - ["*"] in Resource - one element with []
*date_v4.json - ["*","text"] in Resource - two element with []

## Setup
To run this project,provide your own path or use the prepared ones by pasting it here
```
if __name__ == "__main__":
    path = '' # the path to the file
    print(resource_checker_function(path))
    print(resource_checker_pandas(path))
```
(You may need to install the pandas library you can comment resource_checker_pandas if you dont want use pandas)

to run the tests, run the main_test.py file

## Technologies
Project created using:
*Python 3.10
*Pandas
*Pytest

 