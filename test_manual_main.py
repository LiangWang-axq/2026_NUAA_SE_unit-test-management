# ===================== 1. 待测模块的2个关键方法（来自more.py）=====================
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import more_itertools.more as tested_more
from more_itertools.more import chunked, ilen

# ===================== 2. 针对2个关键方法的测试用例 ======================
def test_chunked_method():
    """测试第1个关键方法：chunked（覆盖注入的缺陷）"""
    print("=" * 60)
    print("【关键方法1测试】chunked 分块功能")
    # 测试数据
    test_data = [1, 2, 3, 4, 5, 6]
    chunk_size = 3
    # 预期正确结果
    expected = [[1, 2, 3], [4, 5, 6]]
    # 实际运行结果
    actual = list(chunked(test_data, chunk_size))
    
    print(f"输入数据: {test_data}")
    print(f"分块大小: {chunk_size}")
    print(f"预期结果: {expected}")
    print(f"实际结果: {actual}")
    
    if actual == expected:
        print("测试通过")
        return True
    else:
        print("测试不通过，成功检测到注入的缺陷")
        return False

def test_ilen_method():
    """测试第2个关键方法：ilen 可迭代对象长度计算"""
    print("\n" + "=" * 60)
    print("【关键方法2测试】ilen 可迭代对象长度计算")
    # 测试数据1：普通列表
    test_data1 = [1, 2, 3, 4, 5]
    expected1 = 5
    actual1 = ilen(test_data1)
    
    # 测试数据2：生成器（无法直接用len()）
    test_data2 = (x for x in range(10))
    expected2 = 10
    actual2 = ilen(test_data2)
    
    print(f"普通列表输入，预期长度：{expected1}，实际结果：{actual1}")
    print(f"生成器输入，预期长度：{expected2}，实际结果：{actual2}")
    
    if actual1 == expected1 and actual2 == expected2:
        print("测试通过")
        return True
    else:
        print("测试不通过")
        return False

# ===================== 3. main方法驱动2个关键方法的测试 ======================
if __name__ == "__main__":
    print("开始执行单元测试（main方法驱动待测模块的2个关键方法）")
    print("=" * 60)
    print(f"当前导入的 more.py 路径: {Path(tested_more.__file__).resolve()}")
    
    # 驱动2个关键方法的测试
    result_chunked = test_chunked_method()
    result_ilen = test_ilen_method()
    
    # 汇总模块质量检查结果
    print("\n" + "=" * 60)
    print("【模块单元质量检查汇总】")
    total_methods = 2
    passed_methods = sum([result_chunked, result_ilen])
    
    print(f"待测关键方法总数：{total_methods}")
    print(f"通过测试的方法数：{passed_methods}")
    print(f"存在缺陷的方法数：{total_methods - passed_methods}")
    
    if not result_chunked:
        print("\n检测结果：chunked方法存在逻辑缺陷，模块质量不通过")
    else:
        print("\n检测结果：所有关键方法测试通过，模块质量正常")