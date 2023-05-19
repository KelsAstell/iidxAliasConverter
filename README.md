## 别名库转换器

> 针对maimaiDX [#issue 66](https://github.com/Yuri-YuzuChaN/maimaiDX/issues/66) 制作的一个json转换小工具

最近刚换用[Yuri-YuzuChaN/maimaiDX](https://github.com/Yuri-YuzuChaN/maimaiDX)的maimai机器人模块，因为xray Bot的别名库更为丰富但苦于json结构不同，自己写了个小工具做一下转换。

## 开始使用
1. 克隆本项目到本地
2. 下载[xray bot别名库](https://download.fanyu.site/maimai/alias.json)到项目的`/data`文件夹内
3. 使用任何正常的方式运行`run.py`
4. target.json即为转好格式的json文件

## FAQ
Q: 为什么要生成`target.json`而不是直接覆盖`all_alias.json`
A: 作为增量升级的手段, 留点后悔药.

Q: 别名库的内容有没有审核过
A: 挠头, 使用本工具视同已知晓本人不对不适宜的别名承担任何直接或间接责任

Q: 会不会有重复的别名
A: 没有, 也不会有空的除非原来就是空的, thanks xray

Q: 会不会有xxx功能
A: 不会有, 我一个学翻译的造了什么孽要写代码

Q: 我覆盖了all_alias.json后为什么没起作用
A: 该文件通过接口自动更新, 作者更新前我是直接把更新代码patch掉了, 其实这个工具现在应该也不会用到了, 因为作者已经在[#issue 66](https://github.com/Yuri-YuzuChaN/maimaiDX/issues/66)中表示更新了别名库
