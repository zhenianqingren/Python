# jieba支持四种分词模式：
# - 精确模式：试图将句子最精确地切开，只输出最大概率组合；
# - 搜索引擎模式：在精确模式基础上，对长词再次切分，提高召回率，适用于搜索引擎分词；
# - 全模式：把句子中所有的可以成词的词语都扫描出来；
# - paddle模式，利用PaddlePaddle深度学习框架，训练序列标注（双向GRU）网络模型实现分词。同时支持词性标注。
import jieba

seglist=jieba.lcut('我来到了安徽省合肥市合肥工业大学就读于计算机科学与技术')
print('精确模式:   '+'\\'.join(seglist))
seglist=jieba.cut_for_search('我来到了安徽省合肥市合肥工业大学就读于计算机科学与技术')
print('搜索引擎模式:   '+'\\'.join(seglist))
seglist=jieba.lcut('我来到了安徽省合肥市合肥工业大学就读于计算机科学与技术',cut_all=True)
print('全模式:   '+'\\'.join(seglist))
seglist=jieba.lcut('我来到了安徽省合肥市合肥工业大学就读于计算机科学与技术',use_paddle=True)
print('paddle模式:   '+'\\'.join(seglist))