import numpy as np
import pandas as pd


def init_data():
    data_df = pd.read_csv("celsius_to_fahrenheit.csv")
    data = data_df.to_numpy()

    return data_df, data


def main():
    data_df, data = init_data()  # inner row in big list: sample


if __name__ == "__main__":
    main()
