import sklearn
import pandas as pd


def read_data():
    data = "./data-studenten.csv"
    student_data = pd.read_csv(data)
    return student_data

def model_factory():
    learner = sklearn.linear_model.Ridge()
    learner.fit()
    return learner


if __name__ == "__main__":
    model = model_factory()
