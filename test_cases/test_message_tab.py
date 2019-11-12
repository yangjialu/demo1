import allure
import pytest
import uiautomator2 as u2
from common.message_tab import MessagePage
from common.do_uiautomator2 import UiAuto2
from common.project_path import screen_path
from common.Logger import MyLog
logger = MyLog()
d = u2.connect()


@allure.feature("测试消息tab")
class TestMessage:

    @allure.story("测试发送文本/字母/数字并且正常显示已发送的文本/字母/数字消息")
    def test_send_message(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发送文本/字母/数字并且正常显示已发送的文本/字母/数字消息")
        value = MessagePage(app).send_message()
        MessagePage(app).clear_chat()
        assert value == True

    @allure.story("测试发送消息后消息左上角提示送达")
    def test_send_message_success(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发送消息后消息左上角提示送达")
        value = MessagePage(app).send_message_success()
        MessagePage(app).clear_chat()
        assert value == True

    @allure.story("测试发送图片和点击图片缩略图可以查看大图")
    def test_send_picture(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发送图片和点击图片缩略图可以查看大图")
        value1, value2 = MessagePage(app).send_picture()
        assert value1 == True and value2 == True

    @allure.story("测试可以成功发送表情消息，消息对话页面中正常显示已发送的表情消息")
    def test_send_face_success(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试可以成功发送表情消息，消息对话页面中正常显示已发送的表情消息")
        value = MessagePage(app).send_face_success()
        MessagePage(app).clear_chat()
        assert value == True

    @allure.story("测试发送表情后消息左上角提示送达")
    def test_send_face(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发送表情后消息左上角提示送达")
        value = MessagePage(app).send_face_random()
        MessagePage(app).clear_chat()
        assert value == True

    @allure.story("测试发送我的房间传送门")
    def test_portal(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发送我的房间传送门")
        value , value2 = MessagePage(app).click_send_confirm()
        assert value == True and value2 == True

    @allure.story("测试IM页默认表情展示")
    def test_default_display(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试IM页默认表情展示")
        value = MessagePage(app).click_default_display()
        assert value == True

    @allure.story("测试IM页自定义表情不为空展示")
    def test_custom_display(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试IM页自定义表情不为空展示")
        value = MessagePage(app).custom_display()
        assert value == True

    @allure.story("测试IM页热门表情展示")
    def test_hot_display(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试IM页热门表情展示")
        value = MessagePage(app).hot_display()
        assert value == True

    @allure.story("测试添加自定义表情")
    def test_add_custom(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试添加自定义表情")
        value = MessagePage(app).add_custom()
        assert value == True

    @allure.story("测试删除自定义表情")
    def test_del_custom(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试删除自定义表情")
        value = MessagePage(app).del_custom()
        assert value == False

    @allure.story("测试IM消息页表情/图片添加到表情")
    def test_add_expression(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试IM消息页表情/图片添加到表情")
        MessagePage(app).click_select_text()
        value = UiAuto2().get_toast()
        assert value == "已添加"

    @allure.story("测试图片添加到表情重复")
    def test_repeat_expression(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试图片添加到表情重复")
        MessagePage(app).click_text()
        value = UiAuto2().get_toast()
        assert value == "你已经添加过这个表情了哦(-5101)"

    @allure.story("测试查看打招呼的消息")
    def test_greet(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试查看打招呼的消息")
        value = MessagePage(app).click_add_friend()
        assert value == True

    @allure.story("测试个人状态显示")
    def test_personal_status(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试个人状态显示")
        value = MessagePage(app).click_member_face()
        assert value == True

    @allure.story("测试忽略消息列表未读消息")
    def test_ignore_message(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试忽略消息列表未读消息")
        value = MessagePage(app).click_ignore_send()
        assert value == False

    @allure.story("测试会长在公会总群@全体超过3次")
    def test_guild_group(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试会长在公会总群@全体超过3次")
        value = MessagePage(app).click_four_people()
        assert value == True

    @allure.story("测试取消关注")
    def test_remove_concerns(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试取消关注")
        value = MessagePage(app).remove_concerns()
        assert value == True

    @allure.story("测试不取消关注")
    def test_noremove_concerns(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试不取消关注")
        value = MessagePage(app).noremove_concerns()
        assert value == False

    @allure.story("测试查看粉丝列表")
    def test_view_fan(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试查看粉丝列表")
        value = MessagePage(app).click_fans2()
        assert value == True

    @allure.story("测试查看群组列表")
    def test_view_group(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试查看群组列表")
        value = MessagePage(app).view_group()
        assert value == True

    @allure.story("测试创建游戏群")
    def test_group_chat(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试创建游戏群")
        value = MessagePage(app).click_later_on()
        assert value == True






