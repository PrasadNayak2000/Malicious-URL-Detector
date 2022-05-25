from keras_malicious_url_detector.library.bidirectional_lstm import BidirectionalLstmEmbedPredictor
from keras_malicious_url_detector.library.utility.url_data_loader import load_url_data


def main():

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
    notexit=True
    while notexit:
        url=input("enter an url:")
        predicted_label = predictor.predict(url)
        result="Unsafe"
        if predicted_label==0:
            result="Safe"
        
        print('predicted: ' + result)
        exitornot=input("1.Enter e to exit \n2.Press enter to continue: ")
        if exitornot=='e':
            notexit=False
        
    
    

if __name__ == '__main__':
    main()