import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

enc=pickle.load(open('encoder.pkl','rb'))
encz=pickle.load(open('encoderz.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))
classifier=pickle.load(open('linearreg.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    predict = list(request.form.values())


    part_a = pd.DataFrame.from_records(
        enc.transform(np.array([[predict[0].ljust(50, " ")]])),
        columns=enc.get_feature_names(['boro'])
    )
    part_b = pd.DataFrame.from_records(
        encz.transform(np.array([[predict[1]]])),
        columns=encz.get_feature_names(['zip'])
    )
    part_c=pd.DataFrame.from_records(
        scaler.transform(np.array([[int(predict[2]),float(predict[3]),float(predict[4]),float(predict[5]),float(predict[6])]])),
        columns=(['beds', 'baths', 'sq_ft', 'Unemployment_rate', 'income_rate'])
    )

    model_input = pd.concat([part_c,part_a,part_b], axis="columns")

     
    prediction = classifier.predict(model_input.values)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted housing price is: $ {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)