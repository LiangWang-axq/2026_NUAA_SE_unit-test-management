from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import more_itertools.more as tested_more
from more_itertools.more import chunked, ilen


def test_import_source_is_workspace_copy():
    """确保导入的是工作区根目录的 more_itertools，而不是 venv 里的包。"""
    assert Path(tested_more.__file__).resolve() == PROJECT_ROOT / "more_itertools" / "more.py"


def test_chunked_defect():
    """测试关键方法1：chunked（带缺陷，预期失败）"""
    data = [1, 2, 3, 4, 5, 6]
    assert list(chunked(data, 3)) == [[1, 2, 3], [4, 5, 6]]

def test_ilen_list():
    """测试关键方法2：ilen"""
    assert ilen([1, 2, 3, 4, 5]) == 5

def test_ilen_gen():
    """测试生成器长度计算"""
    assert ilen(x for x in range(10)) == 10

def test_chunked_empty():
    """边界值：空列表测试"""
    assert list(chunked([], 3)) == []