# 初识Tensor
import torch

# ------------------------------------------------------------------------------
# 构造一个5x3矩阵，不初始化。
x = torch.empty(5, 3)
print(x)
# tensor([[0., 0., 0.],
#         [0., 0., 0.],
#         [0., 0., 0.],
#         [0., 0., 0.],
#         [0., 0., 0.]])
# ------------------------------------------------------------------------------
# 构造一个随机初始化的矩阵
x = torch.rand(5, 3)
print(x)
# tensor([[0.3866, 0.9270, 0.6233],
#         [0.1388, 0.1148, 0.9689],
#         [0.0647, 0.4684, 0.8883],
#         [0.2774, 0.8448, 0.1349],
#         [0.6488, 0.2879, 0.8991]])
# ------------------------------------------------------------------------------
# 构造一个矩阵全为 0，而且数据类型是 long.
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
# tensor([[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]])
# ------------------------------------------------------------------------------
# 构造一个张量，直接使用数据
x = torch.Tensor([5.5, 3])
print(x)
# tensor([5.5000, 3.0000])
# ------------------------------------------------------------------------------
# 创建一个 tensor 基于已经存在的 tensor
x = x.new_ones((5, 3), dtype=torch.double)
print(x)
# tensor([[1., 1., 1.],
#         [1., 1., 1.],
#         [1., 1., 1.],
#         [1., 1., 1.],
#         [1., 1., 1.]], dtype=torch.float64)
x = torch.randn_like(x, dtype=torch.float)
print(x)
# tensor([[ 0.1660,  0.9741, -0.3072],
#         [ 1.2797,  0.1477,  0.0961],
#         [-1.1257, -0.0305,  1.0636],
#         [-1.5539, -0.8391,  0.8644],
#         [-0.9935,  0.1761, -1.1106]])
print(x.size())  # 获取它的维度信息 -> torch.Size([5, 3])
# 注意  torch.Size 是一个元组，所以它支持左右的元组操作。
# ------------------------------------------------------------------------------
# 加法
# 方式1
y = torch.rand(5, 3)
print(x + y)
# 方式2
print(torch.add(x, y))
# 方式3  提供一个输出
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
# 方式4  加法之后更新参数
y.add_(x)
print(y)
# tensor([[ 1.7917,  0.8497, -1.1727],
#         [-0.2183, -0.4071,  0.4765],
#         [ 2.7828,  0.8397,  0.4204],
#         [ 0.2390,  0.6799,  0.6519],
#         [ 0.5359,  0.6640, -0.0592]])
# 注意  任何使张量会发生变化的操作都有一个‘前缀’。例如：x.copy(y), x.t_(), 将会改变 x.
# ------------------------------------------------------------------------------
# 使用标准的 NumPy 类似的索引操作
print(x[:, 1])
# tensor([-0.0199,  1.5832,  1.1359,  1.9394,  1.1089])
# ------------------------------------------------------------------------------
# 改变大小  如果你想改变一个 tensor 的大小或者形状  你可以使用 torch.view
x = torch.rand(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())
# torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])
# ------------------------------------------------------------------------------
# 使用 .item() 来获得这个value  此处只适合获取一个标量
print(x[0, 0].item())  # print(x[0][0].item())
# ------------------------------------------------------------------------------
