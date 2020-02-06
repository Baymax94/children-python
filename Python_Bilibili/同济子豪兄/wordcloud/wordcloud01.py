import wordcloud
w=wordcloud.WordCloud()
w.generate('and that government of the people, by the people, for the people, shall not perish from the earth')
w.to_file('wordcloud\output1.png')