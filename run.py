import pytest
from common.project_path import report_path


if __name__ == '__main__':
    pytest.main(["-s", r"--alluredir=test_result\report"])
