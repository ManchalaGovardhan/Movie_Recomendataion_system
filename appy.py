import streamlit as st
import pickle
import pandas as pd
movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')
def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movieslist=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]
  for i in movieslist:
      movie_id=i[0]
      # fetch poster from API
      recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies
selected_movie_name=st.selectbox('how woud you like to contacted?',movies['title'].values)
if st.button('Recommend'):
  recommendations=recommend(selected_movie_name)
  for i in recommendations:
    st.write(i)

