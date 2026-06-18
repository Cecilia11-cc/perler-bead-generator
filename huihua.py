import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# ================== 参数设置 ==================
pixN = 50                  # 像素画大小
maxC = 60                  # 最大使用颜色数
showCName = True           # 在色块上显示色号
fontSZ = 4.5               # 色号字体大小
palettePos = 'right'       # 图例位置：'bottom' 或 'right'

# ================== 文件路径 ==================
base_dir = r'D:\CODE\pyCODE\fuse beads'
input_image  = os.path.join(base_dir, 'input.png')
output_image = os.path.join(base_dir, 'output_pixel_50x50.png')

# ================== Mard 拼豆色卡（直接内嵌） ==================
raw_data = """
A1	#faf5cd
A2	#fcfed6
A3	#fcff92
A4	#f7ec5c
A5	#f0d83a
A6	#fda951
A7	#fa8c4f
A8	#fbda4d
A9	#f79d5f
A10	#f47e38
A11	#fedb99
A12	#fda276
A13	#fec667
A14	#f75842
A15	#fbf65e
A16	#feff97
A17	#fde173
A18	#fcbf80
A19	#fd7e77
A20	#f9d666
A21	#fae393
A22	#edf878
A23	#e4c8ba
A24	#f3f6a9
A25	#fdf785
A26	#ffc734
B1	#dff13b
B2	#64f343
B3	#a1f586
B4	#5fdf34
B5	#39e158
B6	#64e0a4
B7	#3eae7c
B8	#1d9b54
B9	#2a5037
B10	#9ad1ba
B11	#627032
B12	#1a6e3d
B13	#c8e87d
B14	#abe84f
B15	#305335
B16	#c0ed9c
B17	#9eb33e
B18	#e6ed4f
B19	#26b78e
B20	#cbeccf
B21	#18616a
B22	#0a4241
B23	#343b1a
B24	#e8faa6
B25	#4e846d
B26	#907c35
B27	#d0e0af
B28	#9ee5bb
B29	#c6df5f
B30	#e3fbb1
B31	#b4e691
B32	#92ad60
C1	#f0fee4
C2	#abf8fe
C3	#a2e0f7
C4	#44cdfb
C5	#06aadf
C6	#54a7e9
C7	#3977ca
C8	#0f52bd
C9	#3349c3
C10	#3cbce3
C11	#2aded3
C12	#1e334e
C13	#cde7fe
C14	#d5fcf7
C15	#21c5c4
C16	#1858a2
C17	#02d1f3
C18	#213244
C19	#18869d
C20	#1a70a9
C21	#bcddfc
C22	#6bb1bb
C23	#c8e2fd
C24	#7ec5f9
C25	#a9e8e0
C26	#42adcf
C27	#d0def9
C28	#bdcee8
C29	#364a89
D1	#acb7ef
D2	#868dd3
D3	#3554af
D4	#162d7b
D5	#b34ec6
D6	#b37bdc
D7	#8758a9
D8	#e3d2fe
D9	#d5b9f4
D10	#301a49
D11	#beb9e2
D12	#dc99ce
D13	#b5038d
D14	#862993
D15	#2f1f8c
D16	#e2e4f0
D17	#c7d3f9
D18	#9a64b8
D19	#d8c2d9
D20	#9a35ad
D21	#940595
D22	#38389a
D23	#eadbf8
D24	#768ae1
D25	#4950c2
D26	#d6c6eb
E1	#f6d4cb
E2	#fcc1dd
E3	#f6bde8
E4	#e8649e
E5	#f0569f
E6	#eb4172
E7	#c53674
E8	#fddbe9
E9	#e376c7
E10	#d13b95
E11	#f7dad4
E12	#f693bf
E13	#b5026a
E14	#fad4bf
E15	#f5c9ca
E16	#fbf4ec
E17	#f7e3ec
E18	#f9c8db
E19	#f6bbd1
E20	#d7c6ce
E21	#c09da4
E22	#b38c9f
E23	#937d8a
E24	#debee5
F1	#fe9381
F2	#f63d4b
F3	#ee4e3e
F4	#fb2a40
F5	#e10328
F6	#913635
F7	#911932
F8	#bb0126
F9	#e0677a
F10	#874628
F11	#592323
F12	#f3536b
F13	#f45c45
F14	#fcadb2
F15	#d50527
F16	#f8c0a9
F17	#e89b7d
F18	#d07f4a
F19	#be454a
F20	#c69495
F21	#f2b8c6
F22	#f7c3d0
F23	#ed806c
F24	#e09daf
F25	#e84854
G1	#ffe4d3
G2	#fcc6ac
G3	#f1c4a5
G4	#dcb387
G5	#e7b34e
G6	#e3a014
G7	#985c3a
G8	#713d2f
G9	#e4b685
G10	#da8c42
G11	#dac898
G12	#fec993
G13	#b2714b
G14	#8b684c
G15	#f6f8e3
G16	#f2d8c1
G17	#77544e
G18	#ffe3d5
G19	#dd7d41
G20	#a5452f
G21	#b38561
H1	#ffffff
H2	#fbfbfb
H3	#b4b4b4
H4	#878787
H5	#464648
H6	#2c2c2c
H7	#010101
H8	#e7d6dc
H9	#efedee
H10	#ebebeb
H11	#cdcdcd
H12	#fdf6ee
H13	#f4edf1
H14	#ced7d4
H15	#9aa6a6
H16	#1b1213
H17	#f0eeef
H18	#fcfff6
H19	#f2eee5
H20	#96a09f
H21	#f8fbe6
H22	#cacad2
H23	#9b9c94
M1	#bbc6b6
M2	#909994
M3	#697e81
M4	#e0d4bc
M5	#d1ccaf
M6	#b0aa86
M7	#b0a796
M8	#ae8082
M9	#a68862
M10	#c4b3bb
M11	#9d7693
M12	#644b51
M13	#c79266
M14	#c27563
M15	#747d7a
"""

# 解析颜色数据
bead_colors = []
for line in raw_data.strip().split('\n'):
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) != 2:
        continue
    name = parts[0]
    hex_str = parts[1].lstrip('#')
    if len(hex_str) != 6:
        continue
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    bead_colors.append((name, r, g, b))

# 转换为 numpy 数组并归一化
CName_full = [c[0] for c in bead_colors]
RGB_full = np.array([[c[1]/255.0, c[2]/255.0, c[3]/255.0] for c in bead_colors], dtype=np.float64)

print(f'已加载 Mard 拼豆色卡：{len(CName_full)} 种颜色')

# ================== 读取并预处理图片 ==================
try:
    img_pil = Image.open(input_image).convert('RGBA')
except FileNotFoundError:
    print(f'错误：输入图片未找到 -> {input_image}')
    exit(1)

img_rgba = np.array(img_pil).astype(np.float64) / 255.0
M, N, _ = img_rgba.shape

has_alpha = (img_rgba.shape[2] == 4)
if has_alpha:
    alp = img_rgba[:, :, 3]
    img = img_rgba[:, :, :3]
else:
    alp = None
    img = img_rgba[:, :, :3]

# 居中裁剪为正方形
szN = min(M, N) - (min(M, N) % pixN)
start_r = (M - szN) // 2
start_c = (N - szN) // 2
img = img[start_r:start_r+szN, start_c:start_c+szN, :]
if has_alpha:
    alp = alp[start_r:start_r+szN, start_c:start_c+szN]

# ================== 纯 NumPy 分块下采样至 50×50 ==================
szB = szN // pixN
img_small = img.reshape(pixN, szB, pixN, szB, 3).mean(axis=(1, 3))
if has_alpha:
    alp_small = alp.reshape(pixN, szB, pixN, szB).mean(axis=(1, 3))
    img_small[alp_small < 0.5] = [1.0, 1.0, 1.0]

pixels = img_small.reshape(-1, 3)

# ================== 颜色匹配（两次匹配） ==================
CN_full = RGB_full.shape[0]
diff = (pixels[:, None, :] - RGB_full[None, :, :]) ** 2
dist = np.sum(diff, axis=2)
indC_full = np.argmin(dist, axis=1)
countC_full = np.bincount(indC_full, minlength=CN_full)

sorted_idx = np.argsort(-countC_full)
valid_mask = countC_full[sorted_idx] > 0
top_indices = sorted_idx[valid_mask][:maxC]
indNC = np.sort(top_indices)

RGB = RGB_full[indNC]
CN = len(indNC)
diff = (pixels[:, None, :] - RGB[None, :, :]) ** 2
dist = np.sum(diff, axis=2)
indC_sel = np.argmin(dist, axis=1)
countC_sel = np.bincount(indC_sel, minlength=CN)
CName = [CName_full[i] for i in indNC]

label_map = indC_sel.reshape(pixN, pixN)

# ================== 绘制并保存 PNG ==================
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.set_xlim(-1, pixN)
ax.set_ylim(-1, pixN)
ax.axis('off')

# 1. 像素块
for i, (color_rgb, name) in enumerate(zip(RGB, CName)):
    if np.allclose(color_rgb, [1, 1, 1]):
        continue
    rows, cols = np.where(label_map == i)
    for r, c in zip(rows, cols):
        y = pixN - 1 - r
        x = c
        rect = plt.Rectangle((x, y), 1, 1, facecolor=color_rgb, edgecolor='none')
        ax.add_patch(rect)
        if showCName:
            text_color = 'white' if np.mean(color_rgb) < 0.5 else 'black'
            ax.text(x + 0.5, y + 0.5, name,
                    fontsize=fontSZ, color=text_color,
                    ha='center', va='center', fontname='Times New Roman')

# 2. 坐标灰边及数字
ax.add_patch(plt.Rectangle((-1, -1), pixN+1, 1, facecolor=[17/255, 112/255, 189/255]))
ax.add_patch(plt.Rectangle((-1, -1), 1, pixN+1, facecolor=[17/255, 112/255, 189/255]))
for i in range(pixN):
    ax.text(i + 0.5, -0.5, str(i+1), fontsize=7, color='white',
            ha='center', va='center', fontname='Times New Roman')
    ax.text(-0.5, pixN - i - 0.5, str(i+1), fontsize=7, color='white',
            ha='center', va='center', fontname='Times New Roman')

# 3. 网格线（仅像素区域内部）
for k in range(pixN + 1):
    ax.plot([0, pixN], [k, k], color='black', linewidth=0.5, solid_capstyle='butt')
    ax.plot([k, k], [0, pixN], color='black', linewidth=0.5, solid_capstyle='butt')
for k in range(0, pixN + 1, 5):
    ax.plot([0, pixN], [k, k], color='black', linewidth=1.0, solid_capstyle='butt')
    ax.plot([k, k], [0, pixN], color='black', linewidth=1.0, solid_capstyle='butt')

# 4. 色卡图例（右侧，自适应扩展）
rowN = max(1, int((pixN + 1.5) // 1.5))
cols = (CN + rowN - 1) // rowN
fig_width = cols * 3.5 + 0.5
ax.set_xlim(-1, pixN + fig_width)

for i, (color_rgb, name, cnt) in enumerate(zip(RGB, CName, countC_sel)):
    col_i, row_i = divmod(i, rowN)
    x0 = pixN + 0.5 + col_i * 3.5
    y0 = pixN - row_i * 1.5 - 1
    rect = plt.Rectangle((x0, y0), 3, 1, facecolor=color_rgb, edgecolor='gray', linewidth=0.3)
    ax.add_patch(rect)
    tcol = 'white' if np.mean(color_rgb) < 0.5 else 'black'
    ax.text(x0 + 1.5, y0 + 0.5, f'{name} ({cnt})', fontsize=5,
            color=tcol, ha='center', va='center', fontname='Times New Roman')

plt.tight_layout(pad=0.1)
plt.savefig(output_image, dpi=200, bbox_inches=None, pad_inches=0.1,
            facecolor='white', edgecolor='none')
plt.close(fig)

print(f'Mard 拼豆像素画已保存至: {output_image}')