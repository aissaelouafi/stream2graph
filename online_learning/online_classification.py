import pandas as pd
from river import datasets 
from river import compose
from river import linear_model
from river import metrics
from river import preprocessing
from pprint import pprint
import os


if __name__ == "__main__":
    print("Online classification using river ... ")
    #es_url = os.getenv("ES_OUTPUT_INDEX")
    print("")

    # generate a fake dataset
    dataset = datasets.Phishing()

    # model pipeline (preprocessing + model)
    model = compose.Pipeline(
        preprocessing.StandardScaler(),
        linear_model.LogisticRegression()
    )

    metric = metrics.Accuracy()

    for x, y in dataset:
        y_pred = model.predict_one(x)      # make a prediction
        metric = metric.update(y, y_pred)  # update the metric
        model = model.learn_one(x, y)      # make the model learn

    print(f"The accuracy is : {metric}")