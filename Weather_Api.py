from flask import Flask , render_template
import pandas as pd


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/v1/<station>/<date>")
def word(station, date):
    file = f"data-small/TG_STAID"+ str(station).zfill(6) +".txt"
    print(date)
    df = pd.read_csv(file, skiprows=20,)
    temperature = df.loc[["    DATE"] == "18600101"]["   TG"].squeeze()/10
    data = {"station" : station, "date": date, "temperature": temperature}
    return data

if __name__ == "__main__" :
    app.run(debug=True)