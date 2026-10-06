# Algorithms_Research_Lab · 算法研究实验室

这个仓库用于长期记录和理解各种算法、模型及相关框架，通过代码把数学原理变成可执行、可验证的理解。目标不是只收集代码，而是让每一个主题都留下完整学习轨迹：问题从哪里来、核心思想是什么、如何手写实现、怎样验证、最后掌握到了什么。

## 仓库边界

- 收录算法、模型、数学原理的最小实现、推导、对照实验与复盘。
- 框架学习围绕具体算法展开，例如用 PyTorch 的张量、自动求导和网络层理解 MLP、CNN、RNN、Attention 与 Transformer；不做通用 API 手册。
- Python、Git、Docker、ROS2、MuJoCo API 等通用工具教程不放在这里。实验必要的依赖、运行命令和环境版本写在对应项目中。
- Zotero 负责文献管理，Obsidian 负责个人知识整理，不属于本代码仓库职责。这里保留与实现直接相关的笔记、文献引用和实验结论，不同步文献库或整个笔记库。

仓库标准名称为 `Algorithms_Research_Lab`。GitHub 远程名称尚待改正时，使用现有地址克隆，并显式指定正确的本地目录名：

```bash
git clone https://github.com/nightstars10086/Algorithms_Reaserch_Lab.git Algorithms_Research_Lab
cd Algorithms_Research_Lab
```

远程完成重命名后，克隆地址改用 `https://github.com/nightstars10086/Algorithms_Research_Lab.git`，已有副本可更新：

```bash
git remote set-url origin https://github.com/nightstars10086/Algorithms_Research_Lab.git
```

## 仓库结构

```text
.
├── algorithms/              # 最小、可解释、可测试的核心实现
│   ├── basic/               # 基础算法：排序、查找、递归、分治等
│   ├── data_structures/     # 数据结构：链表、栈、队列、树、图等
│   ├── dynamic_programming/ # 动态规划与状态建模
│   ├── graph/               # 图论算法
│   ├── optimization/        # 启发式、智能优化、搜索优化
│   └── deep_learning/       # 张量、梯度、网络层与模型核心
├── docs/                    # 原理、学习路线、记录模板、专题笔记
├── examples/                # 简短调用示例，保留已有入口
├── projects/                # 小型完整验证项目与可复现实验
│   └── deep_learning/       # 手写实现与 PyTorch 模型的对照验证
├── notebooks/               # 探索实验、推导草稿、可视化
│   └── deep_learning/       # 张量、梯度和模型行为的探索
└── tests/                   # 核心实现正确性、边界、数值与梯度检查
```

已有分类和模板保持兼容。只在开始具体实现或实验时创建主题子目录，不预建整套空模型目录。

## 深度学习路线

按 **PyTorch 基础 → MLP → CNN → RNN / LSTM / GRU → Attention → Transformer** 推进，详细任务与完成标准见 [深度学习学习路线](docs/deep-learning-roadmap.md)。

每个模型都走三层：

1. **From scratch**：先推导公式和张量形状，再用 Python 或张量基本运算实现核心；明确哪些梯度手推，哪些由 autograd 计算。
2. **PyTorch API**：用对应框架模块实现同一计算，统一输入、参数和约定，对照输出及梯度，而不只会调用接口。
3. **Experiment**：用小数据完成训练或行为验证，改变一个因素，记录预期、结果和失败原因。

核心运算放在 `algorithms/deep_learning/`；短小 API 对照放在 `examples/`；自由探索放在 `notebooks/deep_learning/`；完整训练与评估放在 `projects/deep_learning/`。阶段编号只用于路线顺序，不强制进入 Python 包名。

## 推荐学习闭环

每学习一个算法，按下面流程走一遍：

1. 选择算法  
   在 `docs/algorithm-index.md` 里登记算法名称、所属主题、学习状态和相关文件。

2. 判断学习类型  
   如果算法有明确输入输出和标准答案，例如二分查找、最短路、排序，使用“确定型算法”流程；如果算法更像一种建模思想或迭代过程，例如 K-means、PCA、遗传算法、反向传播，使用“概念实验型算法”流程。

3. 推导核心思想  
   确定型算法重点写输入输出、关键不变量、状态定义、递推关系或搜索策略。概念实验型算法重点写问题假设、核心概念、优化目标、迭代过程、结果如何解释。不要急着写代码，先保证自己能用自然语言讲清楚。

4. 手写 Python 实现  
   在 `algorithms/<topic>/<algorithm_name>.py` 中实现，优先写可读、可解释的版本，再考虑优化。

5. 编写示例  
   在 `examples/<topic>/<algorithm_name>_example.py` 中写一个贴近真实问题的小例子。

6. 选择验证方式  
   确定型算法优先写单元测试，放在 `tests/<topic>/test_<algorithm_name>.py`。概念实验型算法既要测试可判定的核心运算，也要在 `projects/<topic>/<algorithm_name>/` 用小数据集、可视化、指标或案例解释验证整体行为。

7. 运行验证  
   单元测试使用 `python -m pytest`。小型项目验证运行项目里的 `run.py` 或 notebook，并把结论写回验证报告。

8. 复盘总结  
   回到算法笔记，补充复杂度分析、容易犯错的点、和其他算法的对比，以及“我现在能否不用看代码讲清楚它”。

## 单个算法的文件约定

以二分查找为例：

```text
algorithms/basic/binary_search.py
examples/basic/binary_search_example.py
tests/basic/test_binary_search.py
docs/notes/basic/binary_search.md
```

命名建议：

- 文件名使用小写英文和下划线，例如 `merge_sort.py`。
- 函数名表达算法动作，例如 `binary_search`、`merge_sort`、`dijkstra_shortest_path`。
- 笔记文件与源码文件同名，方便互相查找。

## 两类算法记录方式

| 类型 | 适合算法 | 推荐模板 | 主要验证方式 |
| --- | --- | --- | --- |
| 确定型算法 | 排序、查找、图论、动态规划、数据结构操作 | `docs/templates/deterministic-algorithm-note-template.md` | 单元测试、边界测试、对拍 |
| 概念实验型算法 | K-means、PCA、梯度下降、遗传算法、神经网络基础模块 | `docs/templates/concept-experiment-note-template.md` | 小型项目、指标观察、可视化、消融实验 |

## 算法笔记应该回答的问题

每份算法笔记至少回答这些问题：

- 它解决的原始问题是什么？
- 真实应用场景有哪些？
- 它是确定型问题，还是概念实验型问题？
- 如果有明确输入输出，它们分别是什么？
- 如果没有简单输入输出，它的对象、假设、目标函数或评价指标是什么？
- 朴素思路是什么，瓶颈在哪里？
- 核心优化思想是什么？
- 正确性、收敛性或有效性依赖哪些不变量、数学性质或实验假设？
- 时间复杂度和空间复杂度是多少？
- 代码或实验里最容易写错的地方是什么？
- 有没有相似算法，区别在哪里？
- 学完之后能不能用自己的话讲出来？

## 当前分类规划

| 分类 | 适合记录的内容 |
| --- | --- |
| `basic` | 排序、查找、递归、分治、双指针、滑动窗口 |
| `data_structures` | 数组、链表、栈、队列、哈希表、堆、树、图 |
| `dynamic_programming` | 背包、区间 DP、树形 DP、状态压缩 |
| `graph` | BFS、DFS、最短路、最小生成树、拓扑排序、网络流 |
| `optimization` | 贪心、回溯、局部搜索、遗传算法、模拟退火、聚类优化 |
| `deep_learning` | 张量、反向传播、优化器、损失函数、MLP、CNN、RNN/LSTM/GRU、Attention、Transformer |

## 当前进度与运行

目前仓库包含目录说明、学习流程和模板，尚未实现具体算法或模型。索引中的 `todo` 路径是计划，不代表文件已经存在；深度学习路线也不代表已有可运行模型。

基础检查使用 Python 3.10 或更新版本和 pytest：

```bash
python -m pip install "pytest>=8.0"
python -m pytest
```

PyTorch、Notebook 和数据集依赖按实际实验需要添加，并在实验文档中记录版本、设备与运行方式；基础目录检查不依赖 PyTorch。

## 建议节奏

每个算法尽量分三遍完成：

1. 第一遍：理解问题和暴力解法，写出最朴素实现。
2. 第二遍：加入核心优化，补齐测试和复杂度分析。
3. 第三遍：不用资料重新实现一次，并写复盘。

学习算法最重要的不是一次写对，而是把“为什么这样想”记录下来。这个仓库就是你的算法推理日志。
