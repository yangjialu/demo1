import os
import time
t = time.strftime("%Y-%m-%d_%H%M", time.localtime())


# 文件的路径
path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


# 测试用例的路径
case_path = os.path.join(path, "test_cases")


# 测试报告的路径
report_path = os.path.join(path, "test_result", "report")


# 配置文件的路径
conf_path = os.path.join(path, "conf", "case.conf")


# 日志路径
log_path = os.path.join(path, "test_result", "test_log")


# 错误截图
pic_path = os.path.join(path, "test_result", "picture", 'api_{0}.png'.format(t))

# 图片信息
screen_path = os.path.join(path, "common", "img")



