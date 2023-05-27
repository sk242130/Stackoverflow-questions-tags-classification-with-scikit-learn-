import pickle
def basic_bot(text):
    return text.split(" ")[2]

# METHOD TO INSTANCIATE A VECTORIZER
def predict_bot(user_text):
    clf_svm= pickle.load(open("/Users/souha_kassab/OC_P5/code/notebooks/classifieur3_svm.p", "rb"))
    vectorizer = pickle.load(open("/Users/souha_kassab/OC_P5/code/notebooks/vectorizer3_tfidf.p", "rb"))
    text_to_predict = vectorizer.transform([user_text]) 
    return clf_svm.predict(text_to_predict)[0]

# METHOD TO INSTANCIATE A PIPELINE WITH A CLASSIFIER
def predict_most_common(user_text):
    clf_svm= pickle.load(open("/Users/souha_kassab/OC_P5/code/notebooks/pipeline_most_common_tags.p", "rb"))
    text_to_predict = [user_text]
    return clf_svm.predict(text_to_predict)[0]

# if __name__ == "__main__":
#     anss = predict_bot("What is python")
#     print (anss[0])