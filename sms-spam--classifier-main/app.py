# import streamlit as st
# import pickle
# import string
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
# from sklearn.naive_bayes import MultinomialNB
# nltk.download('punkt')
#
# # ps = PorterStemmer()
# #
# # def transform_text(text):
# #     text = text.lower()
# #     text = nltk.word_tokenize(text)
# #     y = []
# #     for i in text:
# #         if i.isalnum():
# #             y.append(i)
# #     text = y[:]
# #     y.clear()
# #     for i in text:
# #         if i not in stopwords.words('english') and i not in string.punctuation:
# #             y.append(i)
# #     text = y[:]
# #     y.clear()
# #     for i in text:
# #         y.append(ps.stem(i))
# #     return " ".join(y)
# #
# # # Load the fitted model
# # # model_pipeline = pickle.load(open('/home/shubh/sms-spam-classifier/pythonProject1/pkl_files/model.pkl', 'rb'))
# #
# # tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
# # model = pickle.load(open('model.pkl', 'rb))
# # st.title("Email/SMS Spam Classifier")
# #
# # input_sms = st.text_area("Enter the message!")
# #
# # if st.button('Predict'):
# #
# #    # 1. preprocess
# #     transformed_sms = transform_text(input_sms)
# #     result = model_pipeline.predict([transformed_sms])[0]
# #
# #     if result == 1:
# #         st.header("It's a spam!")
# #     else:
# #         st.header("It's not a spam!")
#
#
# #
# # import streamlit as st
# # import pickle
# # import string
# # from nltk.corpus import stopwords
# # import nltk
# # from nltk.stem.porter import PorterStemmer
#
# ps = PorterStemmer()
#
#
# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
#
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
#
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
#
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         y.append(ps.stem(i))
#
#     return " ".join(y)
#
# tfidf = pickle.load(open('/home/shubh/sms-spam-classifier/pythonProject1/pkl_files/vectorizer.pkl','rb'))
# model = pickle.load(open('/home/shubh/sms-spam-classifier/pythonProject1/pkl_files/model.pkl','rb'))
#
# st.title("Email/SMS Spam Classifier")
#
# input_sms = st.text_area("Enter the message")
#
# if st.button('Predict'):
#
#     # 1. preprocess
#     transformed_sms = transform_text(input_sms)
#     # 2. vectorize
#     vector_input = tfidf.transform([transformed_sms])
#     # 3. predict
#     result = model.predict(vector_input)[0]
#     # 4. Display
#     if result == 1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")




import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.exceptions import NotFittedError

# Downloading the necessary NLTK data
nltk.download('punkt')

# Initializing Porter Stemmer
ps = PorterStemmer()

# Preprocessing the input text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [ps.stem(word) for word in text if word.isalnum() and word not in stopwords.words('english')]
    return " ".join(text)

# Loading the vectorizer and model
tfidf = pickle.load(open('/home/shubh/sms-spam-classifier/pythonProject1/pkl_files/vectorizer2.pkl', 'rb'))
model = pickle.load(open('/home/shubh/sms-spam-classifier/pythonProject1/pkl_files/model2.pkl', 'rb'))



from sklearn.utils.validation import check_is_fitted

try:
    check_is_fitted(model)
    print("Model is fitted.")
except NotFittedError:
    print("Model is not fitted.")


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("The given message is a 'Spam'!")
    else:
        st.header("The given message is a 'Not Spam'!")
