import uvicorn
from fastapi import FastAPI
import pickle
from pydantic import BaseModel


class attributes(BaseModel):
    meanfreq : float
    sd : float
    median : float
    Q25 : float
    Q75 : float
    IQR : float
    skew : float
    kurt : float
    sp_ent : float
    sfm : float
    mode : float
    centroid : float
    meanfun : float
    minfun : float
    maxfun : float
    meandom : float
    mindom : float
    maxdom : float
    dfrange : float
    modindx : float


app = FastAPI()

pickle_in = open('/home/sarim/Desktop/Code/Projects/Notebook/Data Science Internship/Voice_Classification/final_model.pkl','rb')
model = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message' : 'Hello Everyone!'}

@app.get("/{name}")
def greet(name : str):
    return {'message' : f"Welcome {name}!"}


@app.post('/predict')
def predict_gender(data : attributes):
    data = data.dict()
    print(data)

    meanfreq = data['meanfreq']
    sd = data['sd']
    median = data['median']
    Q25 = data['Q25']
    Q75 = data['Q75']
    IQR = data['IQR']
    skew = data['skew']
    kurt = data['kurt']
    sp_ent = data['sp_ent']
    sfm = data['sfm']
    mode = data['mode']
    centroid = data['centroid']
    meanfun = data['meanfun']
    minfun = data['minfun']
    maxfun = data['maxfun']
    meandom = data['meandom']
    mindom = data['mindom']
    maxdom = data['maxdom']
    dfrange = data['dfrange']
    modindx = data['modindx']

    print(model.predict([[meanfreq, sd, median, Q25, Q75, IQR, skew, 
    kurt, sp_ent, sfm, mode, centroid, meanfun, minfun, maxfun, meandom, 
    mindom, maxdom, dfrange, modindx]]))

    prediction = model.predict([[meanfreq, sd, median, Q25, Q75, IQR, skew,
     kurt, sp_ent, sfm, mode, centroid, meanfun, minfun, maxfun, meandom,
      mindom, maxdom, dfrange, modindx]] )

    if prediction[0] == 1:
        prediction = 'This is the voice of a Male'
    else:
        prediction = 'This is the voice of a Female'
    return {
        'prediction' : prediction
    }

    if __name__ == '__main':
        uvicorn.run(app, host = '127.0.0.1', port = 8000)

# To run the following file write the following file in the terminal but be sure that they are in the same path/root as the file
    # uvicorn app:app --reload
