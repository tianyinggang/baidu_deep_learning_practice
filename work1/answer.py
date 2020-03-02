# encoding=utf-8
import math
import sys
import re
import jieba
import jieba.analyse
import paddlehub

sys.path.append('../')


def read_md(nameMD):
    with open(nameMD) as f:
        lines = f.readlines()
    lines = [i.strip() for i in lines]
    delete = u'[’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'  # 用户也可以在此进行自定义过滤字符
    lines = re.sub(delete, '', str(lines))
    lines = lines.replace("\n", '')
    lines = lines.replace(" ", '')
    return lines


def Keyword_part_LAC(arr):
    model = paddlehub.Module(name="lac")
    result=model.lexical_analysis(data={'text':arr})
    return result


def Keyword_part_jieba(arr):
    seg_list = jieba.cut_for_search(str(arr))  # 搜索引擎模式
    a = ", ".join(seg_list)
    a = a.split(',')
    print(a)
    return a


def informationentropy(strs):  # Calculating information entropy

    strs_number = {}
    for i in range(int(len(strs))):
        if i in strs_number:
            strs_number[i] += 1
        else:
            strs_number[i] = 1

    strs_count = len(strs)
    info = 0
    for Key, value in strs_number.items():
        p = value / strs_count
        info = info - p * math.log(p, 2)
    return info


if __name__ == "__main__":
    strs1 = read_md('data/1946-05-15_艾森豪威尔_过京沪即将赴日.md')
    a = input('请选择分词方法：' + '\n' + '1.jieba分词' + '\n' + '2.paddle_LAC分词' + '\n' + '请输入【1/2】')
    a=int(a)
    print('\n')
    if a == 1:
        arr = Keyword_part_jieba(strs1)
    elif a == 2:
        arr = Keyword_part_LAC(strs1)
    else:
        print('please input agin')
    entr = informationentropy(arr)
    print('\n'+"information entropy:{}".format(entr))