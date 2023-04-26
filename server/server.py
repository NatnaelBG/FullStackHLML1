from flask import Flask, request, jsonify
import helper
import predict_price_func
import csv

data = []

# Read the CSV file when the Flask app starts up
with open("../model/final_data.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

app = Flask(__name__)
col_file_path = "./artifacts/columns.json"
model_file_path = "./artifacts/final_house_prices_model1.pickle"

data_columns = helper.get_data_columns()
model = helper.get_model()


@app.route("/get_neighbourhood_names")
def get_neighbourhood_names():
    response = jsonify({"names":helper.get_neighbourhood_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/query_results", methods=["GET", "POST"])
def data_query():
    _neighborhood = str(request.form["Neighborhood"])
    _bldgType = str(request.form["BldgType"])
    _overallQual = int(request.form["OverallQual"])
    _lotArea = int(request.form["LotArea"])
    _bedroomAbvGr = int(request.form["BedroomAbvGr"])
    _bathrooms = float(request.form["Bathrooms"])
    _garageCars = int(request.form["GarageCars"])

    estimated_price = predict_price_func.predict_price(data_columns, model, _neighborhood,
                                                       _bldgType, _overallQual,
                                                       _lotArea, _bedroomAbvGr,
                                                       _bathrooms, _garageCars)

    query_results = []
    for _row in data:
        if (not _neighborhood or _row["Neighborhood"].lower() == _neighborhood.lower()) and \
                (not _bedroomAbvGr or int(_row["BedroomAbvGr"]) == _bedroomAbvGr):
        # if (not _neighborhood or _row["Neighborhood"].lower() == _neighborhood.lower()):
            query_results.append(_row)
    response = jsonify({
        "estimated_price": estimated_price,
        "query_results": query_results})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run()
