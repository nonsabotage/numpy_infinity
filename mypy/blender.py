# ---------------------------------------------------
# 値が 0~1 に正規化されている二つのRGB画像をブレンド
# ----------------------------------------------------

import numpy as np

def hardlight(img1, img2):
    lay1 = 2 * img1 * img2
    lay2 = 1 - 2 * (1 - img1) * (1 - img2)
    mask = img2 < .5
    out  = mask * lay1 + (1-mask) * lay2
    out  = np.clip(out, 0, 1)
    return out


def softlight (img1, img2):
    lay1 = 2 * img1 * img2 + img1 * img1 * (1 - 2 * img2)
    lay2 = 2 * img1 * (1 - img2) + np.sqrt(img1) * (2 * img2 - 1)
    mask = img2 < .5
    out  = mask * lay1 + (1 - mask) * lay2
    out  = np.clip(out, 0, 1)
    return out

def linearlight(img1, img2):
    layer1 = img1 + 2 * img2 - 1
    layer2 = img1 + 2 * (img2 - .5)
    mask = img2 < .5
    out  = mask * layer1 + (1-mask) * layer2
    out  = np.clip(out, 0, 1)
    return out


def vividlight(img1, img2):
    epsilon = 1e-8
    layer1  = 1 - (1 - img1) / (2 * img2 + epsilon)
    layer2  = img1 / (1 - 2 * (img2 - .5) + epsilon)
    mask = img2 < .5
    out  = mask * layer1 + (1-mask) * layer2
    out  = np.clip(out, 0, 1)
    return out


def overlay(img1, img2):
    layer1 = 2 * img1 * img2
    layer2 = 1 - 2 * (1 - img1) * (1 - img2)
    mask = img1 < .5
    out  = mask * layer1 + (1-mask) * layer2
    out  = np.clip(out, 0, 1)
    return out

