import wordcloud
import jieba

f=open("政府工作报告.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",\
                      width=1000,height=700,background_color="white",\
               max_words=25,stopwords="和 的 等 在 为 要 坚持")
w.generate(txt)
w.to_file("Report.png")