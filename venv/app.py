from flask import Flask,render_template,request
import encryption as enc
import pandas as pd
import numpy as np
import create_html as c_html

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
    response = c_html.create_html(df,docs)

    return render_template("index.html",r0 = response[0],r1 = response[1],r2= response[2])


if __name__ == "__main__":
    app.run(port=8000, debug=True)