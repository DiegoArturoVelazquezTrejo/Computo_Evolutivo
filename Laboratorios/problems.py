import numpy as np
import torch

def spheres_f(x):
    return sum(x**2)


def spheres_j(x):
    return 2*x


def schwefel_f(x):
    alpha = 418.982887
    return sum(-x*np.sin(np.sqrt(np.abs(x))))+alpha*len(x)


def schwefel_j(x):
    x_t = torch.from_numpy(x)
    x_t.requires_grad_()
    alpha = 418.982887
    fx_t = sum(-x_t*torch.sin(torch.sqrt(torch.abs(x_t))))+alpha*len(x)
    jx_t = fx_t.backward()
    return x_t.grad.numpy()

