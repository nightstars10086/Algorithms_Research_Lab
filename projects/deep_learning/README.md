# 深度学习验证项目

这里按 [学习路线](../../docs/deep-learning-roadmap.md) 放置小型完整项目，例如 MLP 的 XOR 分类、循环网络的合成序列预测、Transformer 的序列复制。当前这些项目尚未实现，仅在开始实验时创建相应目录。

每个项目至少说明验证问题、数据、依赖与运行方式，并包含可重复运行的训练/评估入口和结果报告。复用 `algorithms/deep_learning/` 的核心实现，提供 PyTorch API 基线；先保证小数据、CPU 下可以检查基本流程，再按需要扩大实验。

记录随机种子、设备、框架版本、参数、数据划分和指标。一次对比尽量只改变一个因素，报告也保留失败案例。数据能生成就提供生成方式；大型数据与权重保存在仓库外，不预建空 `data/` 或 `outputs/`。

报告沿用 [项目验证模板](../../docs/templates/project-validation-template.md)。
