# 深度学习探索实验

按照 [学习路线](../../docs/deep-learning-roadmap.md) 探索张量形状、梯度、模型行为和参数影响。当前只提供入口说明，具体 notebook 随学习进度创建。

- 每个 notebook 聚焦一个问题，先写预期，再记录观察与解释。
- 记录依赖、设备、随机种子和数据来源；提交前重启内核并从头运行，避免依赖隐藏状态。
- 将稳定核心实现提取到 `algorithms/deep_learning/`，将可重复的训练与评估整理到 `projects/deep_learning/`，结论写回 `docs/notes/deep_learning/`。
- 不提交大型数据集、模型权重或冗长训练输出；保留必要的小图表与结果摘要。
