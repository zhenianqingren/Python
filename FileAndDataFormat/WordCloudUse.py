import wordcloud
import jieba

# w=wordcloud.WordCloud(width=600,height=600)
# w.generate(txt) case:w.generate("Python and WordCloud")
# w.to_file(filename) case:w.to_file(outfile.png") transform wordcloud to picture
#
# other parameter:
# min_font_size regulate the minimum font size , default is 4
# max_font_size regulate the max font size ,it will adjust to environment accordingly
# font_path regulate the path of font file ,default is None
# max_words regulate the max number of words in wordcloud
# stop_words regulate words which can'be displayed
# mask regulate the shape of wordcloud ,default is rectangle
# background_color

txt="程序设计语言是计算机能够理解和" \
    "识别用户操作意图的一种交互体系，它按照" \
    "特定规则组织计算机指令，使计算机能够自" \
    "动进行各种运算处理"
w=wordcloud.WordCloud(width=1000,\
                      font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pycloud.png")
