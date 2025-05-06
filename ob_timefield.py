
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_ob_timefield():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # กำหนดแกน
    x = np.array([1, 0, 0])
    y = np.array([0, 1, 0])
    z = np.array([0, 0, 1])
    origin = np.array([[0, 0, 0]]).T

    # แสดงเวกเตอร์
    ax.quiver(*origin, *x, color='blue', label='X: Linear Time')
    ax.quiver(*origin, *y, color='green', label='Y: Structural Outcome')
    ax.quiver(*origin, *z, color='red', label='Z: Potential Time')

    ax.set_xlim([-0.2, 1.2])
    ax.set_ylim([-0.2, 1.2])
    ax.set_zlim([-0.2, 1.2])
    ax.set_xlabel('X: Time Flow')
    ax.set_ylabel('Y: Activity / Output')
    ax.set_zlabel('Z: Unobserved Potential')
    ax.set_title('Ob()TimeField: 3D Quantum Time Logic')

    ax.legend()
    plt.tight_layout()
    plt.show()

# เรียกใช้ฟังก์ชันได้โดยตรง
if __name__ == "__main__":
    plot_ob_timefield()
