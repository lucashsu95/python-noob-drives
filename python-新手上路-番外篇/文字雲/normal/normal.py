from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# Read the whole text.
txtfile = "text.txt"  # 剛才下載存的文字檔
text = open(os.path.join(d, 'text.txt'), encoding="utf-8").read()
font_path = os.path.join(d, 'microsoft.ttf')  # 正確的文件名稱和路徑

# Generate a word cloud image
wordcloud = WordCloud(font_path=font_path, max_font_size=32).generate(text)

# 繪圖
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
