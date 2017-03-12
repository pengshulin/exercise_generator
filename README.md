introduction in Chinese, no English version

Python练习题生成器
==================

个人业余制作，给自家的小学生出算术题训练用。

用Python定义规则，将生成结果复制粘帖到Excel/WPS模板中再排版，此处只提供工具，暂不提供模板文件。

规则说明：

* 定义必须包含generator函数，其返回值必须为字符串列表，作为单次出题结果。
* 用ASSERT函数筛除不符合规则的出题。
* random库的所有函数已导入，可直接使用。
* 支持unicode字符串。
* 当返回结果项为字符串“EOL”时，换行输出。

URL: <https://github.com/pengshulin/exercise_generator>

Peng Shullin <trees_peng@163.com> 2017


