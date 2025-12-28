import hashlib
import os
import random
import numpy as np

def hamming_distance(bytes1, bytes2):
    assert len(bytes1) == len(bytes2)
    dist = 0
    for b1, b2 in zip(bytes1, bytes2):
        xor_result = b1 ^ b2
        dist += bin(xor_result).count('1')
    return dist
def sm3_hash(data):
    try:
        from Crypto.Hash import SM3
        h = SM3.new()
        h.update(data)
        return h.digest()
    except ImportError:
        try:
            from gmssl import sm3
            result = sm3.sm3_hash(list(data))
            return bytes.fromhex(result)
        except ImportError:
            return hashlib.new('sm3', data).digest()
def sha3_256_hash(data):
    """SHA3-256哈希函数"""
    return hashlib.sha3_256(data).digest()
def test_avalanche_effect(hash_func, hash_name, data_length=256, num_trials=1000):
    print(f"\n=== 正在测试 {hash_name} 的雪崩效应 ===")
    print(f"消息长度: {data_length} 比特")
    print(f"试验次数: {num_trials}")
    change_rates = []
    for i in range(num_trials):
        # 1. 生成随机原始消息
        original_msg = os.urandom(data_length // 8)  # 生成随机字节
        # 2. 计算原始哈希值
        original_hash = hash_func(original_msg)
        # 3. 随机选择一个比特位置进行翻转
        flip_byte_index = random.randint(0, len(original_msg) - 1)
        flip_bit_index = random.randint(0, 7)
        # 创建翻转后的消息
        flipped_msg = bytearray(original_msg)
        flipped_msg[flip_byte_index] ^= (1 << flip_bit_index)
        # 4. 计算翻转后的哈希值
        flipped_hash = hash_func(bytes(flipped_msg))
        # 5. 计算汉明距离和变化率
        hash_bit_length = len(original_hash) * 8
        dist = hamming_distance(original_hash, flipped_hash)
        change_rate = (dist / hash_bit_length) * 100.0
        change_rates.append(change_rate)
    # 6. 统计分析
    avg_rate = float(np.mean(change_rates))
    std_dev = float(np.std(change_rates))
    print(f"结果分析 ({hash_name}):")
    print(f"  平均比特变化率: {avg_rate:.4f}%")
    print(f"  标准差: {std_dev:.4f}%")
    print(f"  理论理想值: 50.0000%")
    return avg_rate, std_dev
if __name__ == "__main__":
    NUM_TRIALS = 1000
    # 测试 SHA3-256
    sha3_avg, sha3_std = test_avalanche_effect(sha3_256_hash, "SHA3-256", num_trials=NUM_TRIALS)
    # 测试 SM3
    sm3_avg, sm3_std = test_avalanche_effect(sm3_hash, "SM3", num_trials=NUM_TRIALS)
    # 简单对比
    print(f"\n=== 简要对比 ===")
    print(f"SHA3-256 接近 50% 的程度: {abs(50.0 - sha3_avg):.4f}%")
    print(f"SM3      接近 50% 的程度: {abs(50.0 - sm3_avg):.4f}%")