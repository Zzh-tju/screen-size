# 银幕尺寸绘制

数据采自[全球IMAX及其他系统影厅分布](https://docs.qq.com/sheet/DQ3FEUUZJdklNSWJP?tab=BB08J2)

### 数据准备
登录QQ PC端，快捷键Ctrl+Alt+O，识别文本，保存于name.txt，银幕尺寸信息保存于size.txt，这里只采集了IMAX影厅。

### 环境配置

安装Anaconda3

```
conda create -n drawsize python=3.8

conda activate drawsize

pip install numpy

pip install matplotlib

pip install opencv-python

pip install Pillow
```

### 绘制步骤

运行`convert.py`，将size.txt转成size1.txt。

说明：name.txt与size1.txt即为我们想要的，每一行对应一个影厅与银幕尺寸，不同的城市由短连接号隔开。

运行`draw.py`，得到银幕尺寸图，水平分辨率默认为4000。
