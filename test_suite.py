# ==============================
# pytest 测试集（等价于 JUnit Suite）
# 作用：将多个单元测试打包，实现批量运行
# ==============================
import pytest

# 定义测试集：把要批量运行的测试函数全部放进来
test_suite = [
    "test_pytest.py::test_import_source_is_workspace_copy",  # 导入来源校验
    "test_pytest.py::test_chunked_defect",    # 带缺陷的方法测试
    "test_pytest.py::test_ilen_list",          # 方法2测试
    "test_pytest.py::test_ilen_gen",           # 边界场景
    "test_pytest.py::test_chunked_empty",      # 边界值
]

# 批量运行测试集
if __name__ == "__main__":
    print("===== 开始执行 测试集 批量运行（等价于 JUnit Suite）=====")
    pytest.main([*test_suite, "-v"])  # 一键执行所有测试