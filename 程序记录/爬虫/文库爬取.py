#https://www.cnblogs.com/huangguifeng/p/11829323.html

import requests
import re
import json
from docx import Document
from docx.oxml.ns import qn
import easygui as eg
url = "https://wenku.baidu.com/view/949bc6a3b8f3f90f76c66137ee06eff9aff84940.html?fr=search"
url=eg.enterbox(msg="请输入要访问的网页",title="文字文档下载")
def get_document(url):

    sess = requests.Session()
    html = sess.get(url).content.decode("gbk")
    title = re.search('id="doc-tittle-0">(.*?)</span>', html).group(1)
    res = re.search("WkInfo.htmlUrls = '(.*)'", html).group(1)
    res = res.replace("\\x22","\"")
    data = json.loads(res)
    document=Document()
    document.styles['Normal'].font.name = u'宋体'
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    #默认设置宋体
    string=""
    for i in data["json"]: 
        url=i["pageLoadUrl"]
        url=url.replace("\\","")
        data=requests.get(url).content.decode("utf-8")
        res=re.search(r"wenku_\d*\((.*)\)",data,re.S).group(1)
        data=json.loads(res)
        for i in data['body']:
            if i["t"] == "word":
                string += str(i["c"])
                if i["ps"] and i["ps"].get("_enter") == 1:
                    string=string[:-1]
                    document.add_paragraph(string)  # 将一段内容写入到word
                    string = ""  # 重新复制 "" 表示新的一段文本
    # 保存word
    dir_=eg.diropenbox(msg="选择保存的文件夹",title="文字文档下载")+r"\\"
    document.save(dir_ + title + ".docx")
get_document(url)