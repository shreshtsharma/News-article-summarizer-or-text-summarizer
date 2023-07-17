import streamlit as st
import requests
import summarizer

response = requests.get("https://newsdata.io/api/1/news?apikey=pub_2634068e49b82074f0cb222ae8ba59b6690f2&language=en&country=in")
data = response.json()
articles=data['results']
st.set_page_config( page_icon="📰",page_title="News Summarizer")
st.title("News article summarizer")
st.write("")
st.write("")

num_articles = len(articles)


current_article_index = st.session_state.get('current_article_index', 0)

# Function to display the current article
def display_article(index):
    try:
            article = articles[index]
            # st.subheader(f"News {index + 1}:")

            st.header(article['title'])
            try:
                st.image(article['image_url'], use_column_width=True)
            except:
                st.image("news.jpg",use_column_width=True)
    
            st.subheader("Summary of the article:")
            st.write(summarizer.summarize(article['content']))
            st.subheader("Full article:")
            st.write("content:",article['content'])
            st.write("Visit article at:",article['link'])

    except:
        st.error("""NOT ABLE TO LOAD THIS ARTICLE!!!
                 sorry for the incovenience😥 please see other articles""")
        

# Add navigation buttons
col1, col2 = st.columns(2)
with col1:
    if current_article_index > 0:   
        if col1.button("⬅️📰 PREVIOUS ARTICLE"):
            current_article_index -= 1
           
with col2:
    if current_article_index < num_articles - 1:
        if col2.button("NEXT ARTICLE 📰➡️"):
            current_article_index += 1
           


# Save the current article index in session state
st.session_state['current_article_index'] = current_article_index
display_article(current_article_index)
