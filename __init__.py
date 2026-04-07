import sklearn


def model_factory():
    learner = sklearn.linear_model.Ridge()
    return learner


if __name__ == "__main__":
    model = model_factory()
