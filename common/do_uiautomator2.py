import uiautomator2 as u2
from common.Logger import MyLog
TIMEOUT = 10.0


class UiAuto2:
    def __init__(self):
        self.d = u2.connect()

    def get_size(self):
        """获取手机屏幕大小"""
        size = self.d.window_size()
        return size

    def xpath(self, path, timeout=TIMEOUT):
        """xpath定位"""
        try:
            element = self.d.xpath(path).wait(timeout=timeout)
            return element.click()
        except:
            MyLog().error("xpath定位失败")
            return None

    def get_toast(self):
        """获取toast值"""
        try:
            toast = self.d.toast.get_message()
            print(toast)
        except Exception as e:
            MyLog().error("获取toast失败，错误是：{}".format(e))
            raise e
        return toast


if __name__ == '__main__':
    UiAuto2().xpath('//*[@text="电话"]')