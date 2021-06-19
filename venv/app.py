from flask import Flask,render_template,request
import encryption as enc
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    return render_template('index.html', message="OK")

@app.route('/encryption',methods=['POST', 'GET'])
def encryption():
    text = request.form["code"]
    encryption = enc.Encryption(text)
    docs = encryption.get_docs()
    score_list = np.array(enc.calc_score(docs))
    df = pd.DataFrame({'number':score_list})
    df = df.sort_values(by='number',ascending=False)
    df['percentage'] = df['number']/df['number'].sum()
    if df['percentage'].isnull().count()!=len(df):
        response = {
            'message':'NG'
        }
    else:
        response = {
            'message':'OK',
            'data':{
                'index':{
                    '0':df.iloc[0].name,
                    '1':df.iloc[1].name,
                    '2':df.iloc[2].name,
                    '3':df.iloc[3].name,
                    '4':df.iloc[4].name
                },
                'percentage':{
                    '0':df.iloc[0]['percentage'],
                    '1':df.iloc[1]['percentage'],
                    '2':df.iloc[2]['percentage'],
                    '3':df.iloc[3]['percentage'],
                    '4':df.iloc[4]['percentage']
                },
                'text':{
                    '0':docs[df.iloc[0].name],
                    '1':docs[df.iloc[1].name],
                    '2':docs[df.iloc[2].name],
                    '3':docs[df.iloc[3].name],
                    '4':docs[df.iloc[4].name]
                }
            }
        }
    return render_template("index.html",results = response)


if __name__ == "__main__":
    app.run(port=8000, debug=True)