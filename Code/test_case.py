import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu mẫu (ma trận dữ liệu)
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Tạo biểu đồ heatmap
plt.imshow(data, cmap='viridis', interpolation='nearest')

# Đặt tiêu đề và tên trục
plt.title('Heatmap Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Hiển thị biểu đồ
plt.colorbar()  # Thêm thanh màu để hiển thị giá trị tương ứng với màu
plt.show()
