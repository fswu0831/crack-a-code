import pandas as pd
import numpy as np

def create_html(df,docs):
    textarea_class = "result_box"
    res_count_df = df[df['percentage'] >0.0]
    res_count = min(len(res_count_df),5)
    response_text =[]
    response_percent = []
    response_shift = []
    if res_count < 0:
        response = '<h2 class="result_box">候補なし<h2>'
    else:
        for i in range(res_count):
            response_text.append(str(docs[df.iloc[i].name]))
            response_percent.append(str(df.iloc[i]['percentage']))
            response_shift.append(str(df.iloc[i].name))
    response = []
    response.append(response_text)
    response.append(response_percent)
    response.append(response_shift)
    return response
        