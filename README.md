# Font-Messer-For-LiteLoaderQQNT-CCND

为 [@MapleRecall](https://github.com/MapleRecall) 的插件 [LiteLoaderQQNT-CCND](https://github.com/MapleRecall/LiteLoaderQQNT-CCND) 生成新的混淆字体

需要 `Python 3.9`，不保证在其它版本的环境下能正常运行，使用前请安装以下库：

```python
pip install fontTools
pip install brotli
```

安装完成后使用 Python 运行 main.py，即可在 `output` 目录下得到新的混淆字体文件。

main.py 暂时只能生成除 Chaos（乱序映射）样式以外的其他字体文件。Chaos 样式的混淆生成代码在单独的文件夹 CHAOS 内。

> [!WARNING]
> CHAOS 的混淆生成代码需要运行很久很久很久并进行大量的手动操作（后续我会进行优化，但可能要鸽很久）

因该脚本运行过程中引用了 fontTools 库中的一个命令行操作函数，正在研究如何将其打包为 `.exe` 文件（可能也要鸽很久）~~Mac和Linux小白用户就自求多福吧（暴论）（狗头保命）~~

## English_version

Create messed fonts. Used to create new fonts for the [LiteLoaderQQNT-CCND](https://github.com/MapleRecall/LiteLoaderQQNT-CCND)(Author [@MapleRecall](https://github.com/MapleRecall)).

`Python 3.9` REQUIRED, no guarantee for proper working in any other versions. Before use, please install the following LIBS:

```python
pip install fontTools
pip install brotli
```
When installed successfully, use your python to run the file _main.py_, and then you can see the messed fonts in folder _/output_.

Can only generate the styles EXCEPT _chaos_, cause I haven't finished it yet, so I seperated it in the folder _CHAOS_

> [!WARNING]
> THE SCRIPT FOR GENERATING _CHAOS_ MAY TAKE A VERY VERY VERY LONG TIME, AND NEED A MASSIVE MANUAL OPERATION.
