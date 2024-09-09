import itertools

# Đọc dữ liệu đầu vào
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Loại bỏ các phần tử trùng lặp và sắp xếp mảng
A = sorted(set(A))

# Sinh tất cả các tổ hợp chập K của A
combinations = itertools.combinations(A, K)

# In kết quả
for combination in combinations:
    print(*combination)
