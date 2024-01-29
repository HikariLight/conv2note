import os
import wget
import csv

def get_dataset():

    result = []

    train_dataset_path = "https://raw.githubusercontent.com/abachaa/MTS-Dialog/main/Main-Dataset/MTS-Dialog-TrainingSet.csv" 
    
    if not os.path.exists("./train.csv"):
        wget.download(train_dataset_path, "./train.csv")

    with open("./train.csv", encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            data = {}
            data["summary"] = row[2]
            data["conversation"] = row[3]
            data["topic"] = row[1]
            
            result.append(data)

    result.pop(0)
    return result
