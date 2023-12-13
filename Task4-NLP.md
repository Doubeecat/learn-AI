# 人工智能考核文档
## 前言
首先恭喜各位完成上一轮考核

本轮我们的任务是写一个自然语言处理（NLP）模型，基本上能够理解中文语义并生成中文
句子，AKA 弱化版 ChatGPT

## 具体要求
1. 基于 Attention 机制搭建一个 Transform 模型，模型可以参考 pytorch 的教程、参考开源
模型如 Bert、GPT 等
2. 训练时采用无监督学习，预测掩蔽字的方法训练，具体方法例如：
输入“[BEGIN]事实证明 8M 参[MASK]就能做一个差强人意的模型出来。[END]”
输出“[BEGIN]事实证明 8M 参数就能做一个差强人意的模型出来。[END]”
其中[BEGIN]、[MASK]、[END]都是特殊标识符，类似的还有[UNKNOWN]、[NONE]等。
3. 整个模型不能超过 50M（五千万）。事实证明 8M 参数就能做一差强人意的模型出来，
所以不建议一味叠参数，参数过多训练也慢
4. 不能用预训练模型超近路，所以权重必须从随机训练至收敛,但是可以改进其结构然后自己训练

## 参考建议
1. 如果自己电脑跑不了可以晚上十二点去阿里云租搭载 V100 的抢占式服务器，夜间小时
计费非常便宜划算,另外可以报销服务器购买费用,仅限抢占式GPU例程,每人报销上限为100元。
2. 我们提供的数据集来自 2022 年全年人民日报的所有文章，说实话数据量略少，允许可
以自己写爬虫爬取中文语料。
3. 建议将**每个中文单字作为句子拆分的单位**而不是词。如果想尝试拆词建议使用 jieba 分
词算法。
4. 迭代次数可能回明显多于前几轮，有时候 30 多个 epoch 才看得出损失在下降，最终训
练时间可能会花费十多个小时，使用一开始看前几轮没啥变化不要急着停。
5. 有问题及时交流


## 提交内容
-------
将提交文件打个zip发到群里，典型的提交文件如下
```
ProjetcFodder
├─test.py
├─model.py
├─weight.pth
├─requirements.txt
└─network.jpg
```

具体的文件内容建议如下

+ test.py 包含一个测试函数def test(input_str: str),输入含有[BEGIN]、[END]、[MASK]等字段的字符串，自动调用模型对[MASK]处的字进行预测。
+ model.py 仅包含模型的类定义，具体训练、数据处理的代码最好放在诸如train.py、tokenlizer.py当中。
+ weight.pth 模型的权重文件，该文件应当只包含模型权重而不包含文件结构。
+ requirements.txt 环境配置文件，可由pip一键生成，但是请剔除一些绝对用不上的包
+ network.jpg 使用tensorwatch画的网络结构图，本轮可以不用tensorwatch画，可以手画


> 提交文件中包括但不限于以上文件，但是**禁止提交venv、.idea等环境文件**，所提交的代码应是在在执行以下代码安装环境后就可直接运行的最精简文件
> ```
> pip install -r requirement.txt
> ```

## 评价指标
1. 本次考核侧重各位模型构建和查找资料的能力，最后应该会有一个关于模型的答辩，最
终模型的效果不是考核的大头。
2. 自建数据集、阅读论文等这些都可以为最后考核加分
3. Ddl：6 月 13 日 23.59 分，届时按照提交要求打包发群即可