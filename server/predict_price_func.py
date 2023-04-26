import numpy as np
import helper
data_columns = helper.get_data_columns()
print(data_columns)
def predict_price(_cols, _model, Neighborhood,
                  BldgType, OverallQual,
                  LotArea, BedroomAbvGr,
                  Bathrooms, GarageCars) -> float:
    """
    Function to make price predictions using the trained Decision Tree model.
    """
    # Create a numpy array with the input data
    x = np.zeros(len(_cols))
    x[0] = LotArea
    x[1] = OverallQual
    x[2] = BedroomAbvGr
    x[3] = Bathrooms
    x[4] = GarageCars

    # Find the index of the neighborhood and building type in the feature matrix
    try:
        # neighborhood_index = np.where(X.columns == Neighborhood)[0][0]
        neighborhood_index = _cols.index(Neighborhood.lower())
    except:
        neighborhood_index = -1
    try:
        # bldgtype_index = np.where(X.columns == BldgType)[0][0]
        bldgtype_index = _cols.index(BldgType.lower())
    except:
        bldgtype_index = -1

    # Set the values for the neighborhood and building type columns to 1
    if neighborhood_index >= 0:
        x[neighborhood_index] = 1
    if bldgtype_index >= 0:
        x[bldgtype_index] = 1

    # Make price predictions using the trained Decision Tree model
    return round(_model.predict([x])[0], 2)