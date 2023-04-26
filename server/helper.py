import json
import pickle
import sklearn

columns_file_path = "./artifacts/columns.json"
model_file_path = "./artifacts/final_house_prices_model1.pickle"

_data_columns = None
_model = None


def load_data_columns(_col_file_path) -> None:
    global _data_columns
    try:
        with open(_col_file_path, "r") as f:
            _data_columns = json.load(f)["data_columns"]
    except FileNotFoundError:
        return None


def load_model(_model_file_path) -> None:
    global _model
    try:
        with open(_model_file_path, "rb") as f:
            _model = pickle.load(f)
    except FileNotFoundError as e:
        return None


def get_neighbourhood_names():
    return _data_columns[4:15]


def get_data_columns():
    return _data_columns


def get_model():
    return _model


if __name__ == "__main__":
    print()
else:
    columns_file_path = "./artifacts/columns.json"
    model_file_path = "./artifacts/final_house_prices_model1.pickle"

    # load columns
    load_data_columns(columns_file_path)

    #load model
    load_model(model_file_path)

