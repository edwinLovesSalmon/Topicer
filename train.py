# s206534 WONG CHI KEUNG EDWIN senior project
from top2vec import Top2Vec
import pandas as pd
import joblib, os, argparse, ast

# a function to train a top2vec model
def train_top2vec(data_path, columns ,trained_model_path):

    try:
        if not os.path.exists(data_path):
            raise Exception('The passed model path doesn;t exists')
        df = pd.read_csv(data_path)
        if len(columns) == 0:
          raise Exception('Please pass at least one column name')
        # appending all columns into a single string for training
        data = df[columns[0]]
        for col in columns[1:]:
            if not col in df.columns:
                raise Exception(f"The mentioned column name {col} is not present in the passed file")
            data += df[col]
# dropping dupicated and empty records from the data
        data = data.dropna()
        data = data.drop_duplicates().to_list()
        print('Please be patient, model is being trained')
        # start training
        model = Top2Vec(documents= data, speed='learn')
# saving the model
        saved_path = os.path.join(trained_model_path, 'top2vec.jl')
        joblib.dump(model, saved_path )

        print('Trained model has been stored at: ', saved_path)

    except Exception as e:
        print(e)

import json
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--dataFilePath", required=True, help="path to input data file",type=str)
    parser.add_argument("--columns",required=True, help="Name of Columns on top2vec needs to be trained",type=str)
    parser.add_argument("--outputFolderPath",required=True, help="Name of the output Folder where weights are to be saved",type=str)
    args = parser.parse_args()
    columns = args.columns[1:-1].split(',')
    train_top2vec(args.dataFilePath, columns, args.outputFolderPath)
