import numpy as np
import pandas as pd


def init_data():
    data_df = pd.read_csv("celsius_to_fahrenheit.csv")
    data = data_df.to_numpy()

    return data_df, data


def init_parameters(data):

    rng = np.random.default_rng()

    X = data

    w1 = rng.normal(loc=0, scale=np.sqrt(2))
    b1 = 0
    w2 = rng.normal(loc=0, scale=np.sqrt(2))
    b2 = 0

    return X, w1, b1, w2, b2


def main():
    data_df, data = init_data()  # inner row in big list: sample


if __name__ == "__main__":
    main()
