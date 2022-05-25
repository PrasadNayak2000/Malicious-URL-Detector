from flask import Flask, request, render_template 
from keras_malicious_url_detector.library.bidirectional_lstm import BidirectionalLstmEmbedPredictor
from keras_malicious_url_detector.library.utility.url_data_loader import load_url_data

  
# Flask constructor
app = Flask(__name__,template_folder='templates')   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       #first_name = request.form.get("fname")
        data_dir_path = './data'
        model_dir_path = './models'

        predictor = BidirectionalLstmEmbedPredictor()
        predictor.load_model(model_dir_path)

        url_data = load_url_data(data_dir_path)
        count = 0
        for url, label in zip(url_data['text'], url_data['label']):
            predicted_label = predictor.predict(url)
            print('url: '+url+'\npredicted: ' + str(predicted_label) + ' actual: ' + str(label)+'\n')
            count += 1
            if count > 20:
                break
        url=request.form.get("url")
        if url=="" or url==None:
            return render_template("mainform.html")
        predicted_label = predictor.predict(url)
        result="Unsafe"
        if predicted_label==0:
            result="Safe"
        return render_template("form.html",line1="The requested URL \""+url+"\" is "+result+" to browse")
    return render_template("mainform.html")
  
if __name__=='__main__':
   app.run()