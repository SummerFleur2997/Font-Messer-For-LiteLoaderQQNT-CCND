# Mix-Codes-For-LiteLoade

为 [@MapleRecall](https://github.com/MapleRecall) 的插件 [LiteLoaderQQNT-CCND](https://github.com/MapleRecall/LiteLoaderQQNT-CCND) 生成新的混淆字体

需要 `Python 3.9`，不保证在更高版本的环境下能正常运行，使用前请安装以下库：

```python
pip install fontTools
pip install brotli
```

安装完成后使用 Python 运行 main.py，即可在 `output` 目录下得到新的混淆字体文件。

main.py 暂时只能生成除 Chaos（乱序映射）样式以外的其他字体文件。Chaos 样式的混淆生成代码在单独的文件夹 CHAOS 内，需要运行很久很久很久并进行大量的手动操作（后续我会进行优化，但可能要鸽很久）

因该脚本运行过程中引用了 fontTools 库中的一个命令行操作函数，正在研究如何将其打包为 `.exe` 文件（可能也要鸽很久）~~Mac和Linux小白用户就自求多福吧（暴论）（狗头保命）~~
