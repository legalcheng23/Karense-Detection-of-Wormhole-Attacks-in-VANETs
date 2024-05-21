import math
import random

# 定義節點類
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def distance_to(self, other_node):
        return math.sqrt((self.x - other_node.x) ** 2 + (self.y - other_node.y) ** 2)

    def __repr__(self):
        return f"Node({self.id}, x={self.x:.2f}, y={self.y:.2f})"

# 生成隨機節點
def generate_random_nodes(num_nodes, area_size):
    nodes = []
    for i in range(num_nodes):
        x = random.uniform(0, area_size)
        y = random.uniform(0, area_size)
        nodes.append(Node(i, x, y))
    return nodes

# 模擬 Wormhole 攻擊
def simulate_wormhole_attack(node1, node2):
    # 節點1和節點2之間建立Wormhole連接
    return (node1, node2)

# 偵測 Wormhole 攻擊
def detect_wormhole(nodes, wormhole_link, communication_range):
    node1, node2 = wormhole_link
    distance = node1.distance_to(node2)
    if distance > communication_range:
        print(f"Wormhole attack detected between Node {node1.id} and Node {node2.id} with distance {distance:.2f}!")
    else:
        print(f"Direct communication between Node {node1.id} and Node {node2.id} is normal.")

# 主程式
def main():
    # 設定參數
    NUM_NODES = 10
    AREA_SIZE = 500
    COMMUNICATION_RANGE = 100.0

    # 生成節點
    nodes = generate_random_nodes(NUM_NODES, AREA_SIZE)
    print("Generated Nodes:")
    for node in nodes:
        print(node)

    # 選擇兩個節點來模擬 Wormhole 攻擊
    node1, node2 = random.sample(nodes, 2)
    print(f"\nSelected Nodes for Wormhole Attack: Node {node1.id} and Node {node2.id}")

    # 模擬 Wormhole 攻擊
    wormhole_link = simulate_wormhole_attack(node1, node2)

    # 檢測 Wormhole 攻擊
    detect_wormhole(nodes, wormhole_link, COMMUNICATION_RANGE)

# 執行主程式
if __name__ == "__main__":
    main()
