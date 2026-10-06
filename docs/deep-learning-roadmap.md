# 深度学习学习路线

目标是解释模型为什么这样计算，并用代码验证数学直觉。PyTorch 是实现与对照工具，学习内容始终围绕算法、模型和训练原理。当前各阶段均为计划，按实际进度在 [算法索引](algorithm-index.md) 登记，不提前创建空源码文件。

## 阶段与完成标准

| 顺序 | 主题 | From scratch：原理与核心实现 | PyTorch API：对照 | Experiment：验证问题 |
| --- | --- | --- | --- | --- |
| 00 | PyTorch 基础 | 张量形状、广播、矩阵运算；手算简单函数的导数与一次参数更新 | Tensor、autograd、Module、优化器；最小训练循环 | 小型线性回归：解释清零梯度、反向传播、更新参数；对照解析梯度 |
| 01 | MLP | 线性层、激活、损失、链式法则；组合两层网络 | Linear、激活、损失与顺序组合 | XOR 或合成分类：比较有无非线性、隐藏宽度与学习率 |
| 02 | CNN | 手算小矩阵卷积，写卷积与池化；解释通道、步幅、填充 | Conv2d、池化层 | 小图像分类或合成图案：对照卷积输出，改变卷积核或步幅 |
| 03 | RNN / LSTM / GRU | 循环状态更新、时间展开、门控；用基本张量运算写 cell | RNN、LSTM、GRU | 合成序列预测：比较不同序列长度与记忆能力，观察梯度 |
| 04 | Attention | Q/K/V、缩放点积、softmax、mask、自注意力、多头拼接 | 对应注意力 API、多头注意力模块 | 合成检索或序列任务：观察权重，验证 mask，比较头数 |
| 05 | Transformer | 位置编码、残差、归一化、前馈层；先组合 encoder，再 decoder | 对应 encoder/decoder 与 Transformer 模块 | 微型序列复制任务：比较位置编码与因果 mask，区分训练和推理输入 |

每个阶段完成后，应能脱离框架接口解释公式、标出主要张量维度、复述一个失败案例。表中的任务可选一个最小实验，不要求每阶段都做大型数据集训练。

## 三层学习法

### 1. From scratch

先写输入输出、数学表达式和形状，再实现最小核心。可以使用 PyTorch Tensor、矩阵运算和 autograd，但不要直接调用正在研究的现成模型层来代替手写部分。例如手写 RNN cell 应展开状态更新公式。

手写前向与手写反向是两个不同目标：先用简单函数或线性层掌握链式法则，复杂模型可借助 autograd。笔记要明确实现边界，不把使用 autograd 描述成手写反向传播。

### 2. PyTorch API

对同一输入做框架对照，必要时复制相同权重。记录权重布局、batch 维度、偏置、padding、mask、dropout 等约定差异。数值对照应指定误差容限；含随机层时控制随机性并说明训练或评估模式。

API 学习回答“这个接口对应哪一步数学运算”，不扩展成完整 PyTorch 教程。

### 3. Experiment

先写问题和预期，再固定基线，单次改变一个因素。记录数据生成或划分、随机种子、超参数、依赖版本、设备、指标和运行命令。对于序列任务，明确训练与评估如何划分，避免把目标或未来信息泄漏到输入。

损失下降只能说明一个实验现象；核心计算仍需小案例与框架对照。不要用“训练准确率高”代替实现正确性检查。

## 文件放置：以 MLP 为例

以下是开始该阶段时的建议路径，尚未创建这些实现：

```text
algorithms/deep_learning/mlp.py                 # 最小核心，避免数据下载与训练副作用
examples/deep_learning/mlp_example.py           # 简短调用与 API 对照
notebooks/deep_learning/mlp_exploration.ipynb   # 形状、梯度、参数探索
projects/deep_learning/mlp_xor/run.py            # 数据、训练、评估的完整入口
projects/deep_learning/mlp_xor/README.md         # 实验问题、依赖和运行方式
projects/deep_learning/mlp_xor/report.md         # 参数、结果、解释与失败案例
tests/deep_learning/test_mlp.py                 # 核心数值与梯度检查
docs/notes/deep_learning/mlp.md                 # 公式、实现边界、实验链接与复盘
```

简单模块先平铺在 `algorithms/deep_learning/`。只有某个主题出现多个实际模块时，再按 `cnn/`、`rnn/`、`attention/`、`transformer/` 拆分；不使用以数字开头的 Python 包名。

Notebook 探索结束后，将稳定实现提取到 `algorithms/`，可重复运行的完整实验整理到 `projects/`。项目复用核心实现，不复制一套不一致的核心代码。

## 验证与记录

- 核心测试：小输入的预期值、输出形状、边界条件、框架输出对照；需要时做梯度对照或有限差分检查。
- 模型特性：例如因果注意力的 mask 不应泄漏未来信息，循环网络的状态传递应符合时间展开公式。
- 完整实验：记录训练与评估指标、基线、单因素对比和失败案例，不把随机训练结果设为脆弱的精确值断言。
- 复盘：关联源码、API 对照、实验报告和笔记；只有完成这些验证与解释后才标记 `reviewed`。

沿用 [概念实验笔记模板](templates/concept-experiment-note-template.md) 和 [项目验证模板](templates/project-validation-template.md)，不额外维护一套重复模板。
