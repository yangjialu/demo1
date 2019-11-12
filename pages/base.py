import traceback, sys, xlrd, xlwt, re, os, atx, time, functools
from xlutils.copy import copy
from common.Logger import MyLog
logger = MyLog()
from common.project_path import pic_path

__all__ = ['BasePage']
TIMEOUT = 10


class BasePage(object):
    def __init__(self, app, pkg="com.sabac.hy", act=None):
        self.app = app
        self.packageName = pkg
        self.activity = act

    def setpkg(self, pkg):
        self.packageName = pkg

    def setactivity(self, act):
        self.activity = act

    # 启动app
    def start_app(self, stop=True):
        '''
        Start application

        Args:
            - package_name (string): like com.example.app1
            - activity (string): optional, activity name
            - stop: force stop the target app before starting the activity

        Returns time used (unit second), if activity is not None
        '''
        activity = self.activity
        return self.app.start_app(self.packageName, activity, stop)

    # 关闭app
    def close_app(self, clear=False):
        '''
        Stop application

        Args:
            package_name: string like com.example.app1
            clear: bool, remove user data

        Returns:
            None
        '''
        self.app.stop_app(self.packageName, clear)

    # 图片查找元素
    def findpic(self, imgName, raw=True, minpoint=20, confidence=0.9, timeout=TIMEOUT):
        '''
        if raw is True, find raw img, fast, need same size, color, shape, confidence the bigger the more similar,
        the value is little than 1.
        
        if raw is False, use sift find image, could manage scale, but slow, around 0.5s, minpoint the bigger
        the more similar, the max value depands on the picture.
        
        take screenshot takes 0.3s
        '''
        pos = None
        st = time.time()
        while time.time() - st < timeout:
            if not raw:                
                pos = self.img_pos(imgName, "sift")
                if pos and pos[1][0] > minpoint:
                    return pos[0]
            else:
                pos = self.img_pos(imgName, "template")
                if pos and pos[1] > confidence:
                    return pos[0]
        return None

    def img_pos(self, imgName, algorithm):
        """Check if image position in screen

        Args:
            - imgName: Image file name or opencv image object

        Returns:
            None or FindPoint, For example:

            FindPoint(pos=(20, 30), method='tmpl', confidence=0.801, matched=True)

            Only when confidence > self.image_match_threshold, matched will be True

        Raises:
            TypeError: when image_match_method is invalid
        """
        return self.app.exists(imgName, method=algorithm)

    def click_img(self, imgName):
        self.app.click_exists(imgName)

    def click(self, x, y):
        self.app.click(x, y)
        
    def drag(self, sx, sy, ex, ey, duration=0.5):
        self.app.drag(sx, sy, ex, ey, duration=0.5)
        
    def double_click(self, x, y):
        self.app.double_click(x,y)
        
    def long_click(self, x, y, duration=None):
        self.app.long_click(x, y)
        
    def swipe(self, fx, fy, tx, ty, duration=0.5):
        self.app.swipe(fx, fy, tx, ty, duration=0.5)
        
    def screenShot(self):
        """
        Image format is JPEG

        Args:
            filename (str): saved filename
            format (string): used when filename is empty. one of "pillow" or "opencv"

        Raises:
            IOError, SyntaxError

        Examples:
            screenshot("saved.jpg")
            screenshot().save("saved.png")
            cv2.imwrite('saved.jpg', screenshot(format='opencv'))
        """
        time_str = time.strftime('_%m%d_%H%M', time.localtime(time.time()))
        self.app.screenshot(pic_path)
        return None
        
    def screen_on(self):
        self.app.screen_on()
        
    def screen_off(self):
        self.app.screen_off()
        
    def press(self, key):
        '''
        home,back;left;right;up;down;center;menu;search;enter;delete ( or del);recent (recent apps);volume_up
        volume_down;volume_mute;camera;power
        press('home')
        '''
        self.app.press(key)

    def _uiwarp(self, **kwargs):
        '''
        resourceId=None, text=None, className=None, description=None,
        textContains, textMatches, textStartsWith,descriptionContains,descriptionMatches,
        focused,selected,resourceIdMatches,index
        ''' 
        if 'timeout' in kwargs:
            timeout = kwargs['timeout']
            del(kwargs['timeout'])
        else:
            timeout = TIMEOUT
        st = time.time()
        while time.time() - st < timeout:
            try:
                el = self.app(**kwargs)
                if el.exists():
                    return el
                else:
                    time.sleep(0.1)
            except Exception as e:
                logger.error("元素定位出错，错误是：{}".format(e))
                raise e
                # exc_type, exc_value, exc_traceback = sys.exc_info()
                # traceback.print_exception(exc_type, exc_value, exc_traceback)
                # print(kwargs)
        return None

    def findIdText(self, idname, textname, timeout=TIMEOUT):
        return self._uiwarp(resourceId=idname, text=textname, timeout=timeout)

    def findId(self, idname, timeout=TIMEOUT):
        return self._uiwarp(resourceId=idname, timeout=timeout)

    def findClassText(self, classname, textname, timeout=TIMEOUT):
        return self._uiwarp(className=classname, text=textname, timeout=timeout)

    def clickId(self, idname, timeout=TIMEOUT):
        el = self.findId(idname, timeout)
        if el:
            time.sleep(1)
            el.click()
        else:
            raise Exception("click id error {}".format(idname))

    def writeToExcel(self, data, filename, sheetname):
        if os.path.exists(filename):
            self.writeOldExcel(data, filename, sheetname)
        else:
            self.writeNewExcel(data, filename, sheetname)

    def writeNewExcel(self, data, filename, sheetname):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)
        l = len(data)
        for i in range(l):
            worksheet.write(0, i, str(data[i]))
        workbook.save(filename)

    def writeOldExcel(self, data, filename, sheetname):
        oldWb = xlrd.open_workbook(filename)
        newWb = copy(oldWb)
        if sheetname in oldWb.sheet_names():
            rows = oldWb.sheet_by_name(sheetname).nrows
            newWs = newWb.get_sheet(sheetname)
        else:
            newWs = newWb.add_sheet(sheetname, cell_overwrite_ok=True)
            rows = 0
        l = len(data)
        for i in range(l):
            newWs.write(rows, i, str(data[i]))
        newWb.save(filename)

    def clickElTime(self, el=None, checkId=None, checkText=None, reg=None, pos=None, img=None):
        checkEl = None
        retry = 10
        time.sleep(1)
        if el or pos:
            if el:
                el.click()
            else:
                x, y = pos
                self.click(x, y)
            time.sleep(1)
            while retry > 0:
                if checkText:
                    checkEl = self.findIdText(checkId, checkText)
                elif checkId != None:
                    print("check id", checkId)
                    checkEl = self.findId(checkId)
                else:
                    checkEl = self.findpic(img)
                if checkEl:
                    if not reg:
                        return True
                    else:
                        m = re.search(reg, checkEl.get_text())
                        if m:
                            return True
                        else:
                            retry -= 1
                            continue
                else:
                    self.screenShot()
                    logger.error("出错了，错误是没有找到：{}或{}或{}".format(checkId, checkText, img))
                    return False
                retry -= 10
        else:
            self.screenShot()
            logger.error("出错了，错误是没有找到：el or pos")
        return False

