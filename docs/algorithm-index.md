# 算法索引

用这张表追踪每个算法的学习进度。新增算法时先登记，再按学习流程补齐源码、笔记、示例和测试。

下面的 `todo` 条目是计划，路径尚未创建。深度学习按 [专项路线](deep-learning-roadmap.md) 逐阶段登记，开始实现时再填具体文件位置。

| 算法 | 分类 | 类型 | 状态 | 源码 | 笔记 | 验证 |
| --- | --- | --- | --- | --- | --- | --- |
| binary_search | basic | 确定型 | todo | `algorithms/basic/binary_search.py` | `docs/notes/basic/binary_search.md` | `tests/basic/test_binary_search.py` |
| k_means | optimization | 概念实验型 | todo | `algorithms/optimization/k_means.py` | `docs/notes/optimization/k_means.md` | `projects/optimization/k_means/` |

## 深度学习计划

| 阶段 | 状态 | 本阶段重点 |
| --- | --- | --- |
| PyTorch 基础 | todo | 张量、解析梯度与 autograd、最小训练循环 |
| MLP | todo | 线性层、非线性、链式法则、合成分类 |
| CNN | todo | 卷积、池化、通道与空间形状 |
| RNN / LSTM / GRU | todo | 循环状态、门控、时间展开与梯度 |
| Attention | todo | Q/K/V、缩放、mask、自注意力、多头 |
| Transformer | todo | 位置编码、encoder/decoder、序列任务 |

## 状态说明

| 状态 | 含义 |
| --- | --- |
| `todo` | 已计划，尚未开始 |
| `reading` | 正在理解问题、场景和原理 |
| `coding` | 正在实现源码 |
| `testing` | 正在补测试和示例 |
| `reviewed` | 已完成复盘 |

## 类型说明

| 类型 | 含义 |
| --- | --- |
| 确定型 | 有明确输入输出和可判定答案，适合单元测试 |
| 概念实验型 | 更像建模思想或迭代方法，适合用小型项目、指标和可视化验证 |
