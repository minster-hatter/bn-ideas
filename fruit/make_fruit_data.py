import pandas as pd


def make_fruit_data():
    "Make some data."
    data = pd.DataFrame(
        data={
            "fruit": [
                "banana",
                "apple",
                "banana",
                "apple",
                "banana",
                "apple",
                "banana",
                "apple",
                "apple",
                "apple",
                "banana",
                "banana",
                "apple",
                "banana",
            ],
            "tasty": [
                "yes",
                "no",
                "yes",
                "yes",
                "yes",
                "yes",
                "yes",
                "yes",
                "yes",
                "yes",
                "yes",
                "no",
                "no",
                "no",
            ],
            "size": [
                "large",
                "large",
                "large",
                "small",
                "large",
                "large",
                "large",
                "small",
                "large",
                "large",
                "large",
                "large",
                "small",
                "small",
            ],
        }
    )
    return data
