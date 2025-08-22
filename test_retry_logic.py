# 测试重试逻辑的简单验证

def test_retry_logic():
    """测试重试逻辑"""
    
    # 测试各种配置下的重试次数
    test_cases = [
        {"judge_max_retries": 0, "expected_attempts": 1},  # 不重试
        {"judge_max_retries": 1, "expected_attempts": 2},  # 重试1次
        {"judge_max_retries": 3, "expected_attempts": 4},  # 重试3次（默认）
        {"judge_max_retries": 5, "expected_attempts": 6},  # 重试5次
    ]
    
    for case in test_cases:
        judge_max_retries = case["judge_max_retries"]
        expected_attempts = case["expected_attempts"]
        
        # 模拟代码逻辑
        max_retries = judge_max_retries + 1
        if judge_max_retries == 0:
            max_retries = 1
            
        attempts = []
        for attempt in range(max_retries):
            attempts.append(attempt + 1)
            
        print(f"配置重试{judge_max_retries}次 -> 实际尝试{len(attempts)}次 -> 预期{expected_attempts}次 -> {'✅' if len(attempts) == expected_attempts else '❌'}")

if __name__ == "__main__":
    test_retry_logic()
