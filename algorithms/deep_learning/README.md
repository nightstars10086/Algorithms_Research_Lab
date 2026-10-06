# deep_learning

这里放最小、可解释的深度学习核心实现：张量操作、损失函数、优化器、网络层，以及 MLP、CNN、RNN/LSTM/GRU、Attention、Transformer 的关键计算。

学习顺序与完成标准见 [深度学习路线](../../docs/deep-learning-roadmap.md)。先推导并用基本运算手写核心，再与 PyTorch API 对照，最后用小型实验验证行为。使用 autograd 时明确说明，不把它等同于手写反向传播。

- 简单模块先用 `linear.py`、`mlp.py` 等文件；内容增长后再拆主题子目录，不预建空模型包。
- 核心模块可导入、可测试，导入时不下载数据或启动训练。
- 张量形状、参数含义、数学约定写在 docstring 或相应笔记中。
- 简短 API 对照放在 `examples/`，探索放在 `notebooks/deep_learning/`，完整训练与评估放在 `projects/deep_learning/`。
- 核心测试放在 `tests/deep_learning/`，原理与复盘放在 `docs/notes/deep_learning/`；这些子目录随实际内容创建。
