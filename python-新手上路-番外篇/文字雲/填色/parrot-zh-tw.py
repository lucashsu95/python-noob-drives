import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud
import jieba

# 獲取工作目錄
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# 讀取中文文字內容
text = open(os.path.join(d, 'wiki_rainbow.txt'), encoding="utf-8").read()

# 使用jieba分詞處理中文文本
seg_list = jieba.cut(text, cut_all=False)
segmented_text = " ".join(seg_list)

# 讀取彩色圖像
parrot_color = np.array(Image.open(os.path.join(d, "../img/cloud.png")))
parrot_color = parrot_color[::3, ::3]

# 創建遮罩圖
parrot_mask = parrot_color.copy()
parrot_mask[parrot_mask.sum(axis=2) == 0] = 255
edges = np.mean([gaussian_gradient_magnitude(
    parrot_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
parrot_mask[edges > .08] = 255


# 創建文字雲對象
font_path = os.path.join(d, 'microsoft.ttf')  # 正確的文件名稱和路徑
wc = WordCloud(
    font_path=font_path,  # 使用正確的字體文件路徑
    max_words=2000, mask=parrot_mask, max_font_size=20,
    random_state=32, relative_scaling=0
)


# 生成文字雲
wc.generate(segmented_text)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
