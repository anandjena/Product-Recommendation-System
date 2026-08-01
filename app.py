import streamlit as st
import pickle
import joblib

st.title('Product Recomendation System')

with open('product.pickle','rb') as m:
    product = pickle.load(m)

similarity = joblib.load('similarity.joblib','rb')

product_name = product['name'].values

def reccomend(item_name,top_n = 5):
    product_index = product[product['name'] == item_name].index[0]
    recomendation = similarity[product_index]
    product_list = sorted(enumerate(recomendation),key=lambda x: x[1],reverse=True)[1:top_n+1] 
    
    l = []
    for i in product_list:
        l.append(product.iloc[i[0]]['name'])
    return l

pr_name = st.selectbox("Enter the movie name",product_name)

if st.button("Recommend"):
    r = reccomend(pr_name)
    st.write("The recomended products are:")
    for i in r:
        st.write(i)