from joblib import dump, load

def predict(x,y,z,k):
    model = load("model.ml")
    return model.predict([[x,y,z,k]])[0]

