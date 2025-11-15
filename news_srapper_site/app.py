from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
@app.route('/')
def home():
    data=pd.read_csv("news_articles.csv")
    kaler_data=pd.read_csv("news_kaler_kontho.csv")
    amardesh_data=pd.read_csv("news_daily_amardesh.csv")
    data_by_source=pd.concat([data,kaler_data, amardesh_data],ignore_index=True)
    #Show top 5 from each source
    top_5_data = pd.concat([data.head(5), kaler_data.head(5), amardesh_data.head(5)], ignore_index=True)
    return render_template('home.html',articles=top_5_data.to_dict(orient='records'))
@app.route('/prothom_alo')
def prothom_alo():
    data=pd.read_csv("news_articles.csv")
    return render_template('prothomalo.html',articles=data.to_dict(orient='records'))
@app.route('/kaler_kontho')
def kaler_kontho():
    kaler_data=pd.read_csv("news_kaler_kontho.csv")
    return render_template('kalerkontho.html',articles=kaler_data.to_dict(orient='records'))


@app.route('/amar_desh')
def amar_desh():
    amar_desh_data=pd.read_csv("news_daily_amardesh.csv")
    return render_template('amardesh.html',articles=amar_desh_data.to_dict(orient='records'))
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
