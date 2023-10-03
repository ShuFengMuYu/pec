# utils
[https://github.com/scutcyr/CPED]()
修复了一些bug，并且按照需要进行了改动

## 架构说明
### 基础文件
base_util.py: 读取数据集的一些共用函数
dataset_statistics.py: 用于数据集的统计等

### 数据集处理文件
每一个数据集（假设名字为：xxx）都有两个.py文件，格式如下：    
* xxx_util.py: 封装读取数据集的函数以及一些常量
* xxx_dataset.py: 构建torch.utils.data.Dataset的子类、build_xxx_dataloaders函数

### CPED数据集的处理文件：
* cped_util.py: 封装读取CPED数据集的函数以及一些常量
* cped_dataset.py: 构建torch.utils.data.Dataset的子类、build_xxx_dataloaders函数
