import time
import pytest
import allure
from common.voice_ball import VoiceBallPage
from common.Logger import MyLog
logger = MyLog()


@allure.feature("测试语音球")
class TestVoiceBall:
    """测试语音球"""

    @allure.story("测试群聊中收起语音球")
    def test_ball_group(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试群聊中收起语音球")
        value = VoiceBallPage(app).click_back()
        assert value == True

    @allure.story("测试在消息对话页面中发送文本消息并且正常显示")
    def test_sent_msg(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在消息对话页面中发送文本消息并且正常显示")
        value = VoiceBallPage(app).sent_msg_display()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试在消息对话页面中发送文本消息并且发送成功")
    def test_sent_success(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在消息对话页面中发送文本消息并且发送成功")
        value = VoiceBallPage(app).sent_msg_success()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试消息对话页面中正常显示已发送的图片缩略图")
    def test_send_image(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试消息对话页面中正常显示已发送的图片缩略图")
        value = VoiceBallPage(app).click_send_image()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试可以成功发送图片消息")
    def test_send_image_success(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试可以成功发送图片消息")
        value = VoiceBallPage(app).click_send_image_success()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试点击图片缩略图可以查看大图")
    def test_view_big_picture(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试点击图片缩略图可以查看大图")
        value = VoiceBallPage(app).click_sent_picture()
        assert value == True

    @allure.story("测试可以成功发送表情消息")
    def test_send_face_success(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试可以成功发送表情消息")
        value = VoiceBallPage(app).send_face_success()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试消息对话页面中正常显示已发送的表情消息")
    def test_send_face_display(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试消息对话页面中正常显示已发送的表情消息")
        value = VoiceBallPage(app).send_face_display()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试消息对话页面中正常显示收藏中发送的表情消息")
    def test_select_collect_face(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试消息对话页面中正常显示收藏中发送的表情消息")
        value = VoiceBallPage(app).select_collect_face()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试可以成功发送收藏中表情消息")
    def test_select_collect_face_success(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试可以成功发送收藏中表情消息")
        value = VoiceBallPage(app).select_collect_face_success()
        VoiceBallPage(app).click_clear_chat()
        assert value == True

    @allure.story("测试使消息对话页面在TT中打开")
    def test_msg_open(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试使消息对话页面在TT中打开")
        value = VoiceBallPage(app).click_open_in()
        assert value == True

    @allure.story("测试清除聊天记录")
    def test_clear_msg(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试清除聊天记录")
        value = VoiceBallPage(app).clear_msg()
        assert value == False

    @allure.story("测试普通娱乐房进入房间")
    def test_enter_my_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试普通娱乐房进入房间")
        value = VoiceBallPage(app).enter_my_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试普通娱乐房房主/房管上麦")
    def test_upper_wheat(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试普通娱乐房房主/房管上麦")
        value = VoiceBallPage(app).click_upper_wheat()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试普通娱乐房设置麦位闭麦状态")
    def test_close_wheat(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试设置麦位闭麦状态")
        value = VoiceBallPage(app).click_close_wheat()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试普通娱乐房邀请玩伴")
    def test_invite_playmates(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试普通娱乐房邀请玩伴")
        value = VoiceBallPage(app).click_confirm_btn()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试普通娱乐房静音")
    def test_open_silence(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试普通娱乐房静音")
        value = VoiceBallPage(app).click_silence_button()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试普通娱乐房中直接退出房间")
    def test_close_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试普通娱乐房中直接退出房间")
        value = VoiceBallPage(app).click_close_room()
        assert value == False

    @allure.story("测试普通娱乐房进入其他房间而退出房间")
    def test_click_btn_confirm(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试普通娱乐房进入其他房间而退出房间")
        value = VoiceBallPage(app).click_btn_confirm()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试高音质开黑房进入房间")
    def test_enter_hight_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房进入房间")
        value = VoiceBallPage(app).enter_my_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试高音质开黑房房主/房管上麦")
    def test_enter_black_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房房主/房管上麦")
        value = VoiceBallPage(app).click_upper_wheat_1()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试高音质开黑房设置麦位闭麦状态")
    def test_close_wheat_black(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房设置麦位闭麦状态")
        value = VoiceBallPage(app).click_close_wheat_1()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试高音质开黑房邀请玩伴")
    def test_invite_playmates_black(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房邀请玩伴")
        value = VoiceBallPage(app).click_confirm_btn_1()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试高音质开黑房静音")
    def test_open_silence_black(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房静音")
        value = VoiceBallPage(app).click_silence_button_1()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试高音质开黑房中直接退出房间")
    def test_close_room_black(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房直接退出房间")
        value = VoiceBallPage(app).click_close_room()
        assert value == False

    @allure.story("测试高音质开黑房进入其他房间而退出房间")
    def test_click_btn_confirm_black(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试高音质开黑房进入其他房间而退出房间")
        value = VoiceBallPage(app).click_btn_confirm_1()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试切换房间模式到普通娱乐房")
    def test_switch_entertain_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试切换房间模式到普通娱乐房")
        value = VoiceBallPage(app).switch_to_entertainment()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试切换房间模式到高音质开黑房")
    def test_switch_black_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试切换房间模式到高音质开黑房")
        value = VoiceBallPage(app).switch_to_black()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试切换房间模式到高音质开黑房")
    def test_switch_black_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试切换房间模式到高音质开黑房")
        value = VoiceBallPage(app).switch_to_black()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会公开娱乐房进入房间")
    def test_public_enter_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房进入房间")
        value = VoiceBallPage(app).click_public_test()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会公开娱乐房房主/房管上麦")
    def test_public_upper_wheat(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房房主/房管上麦")
        value = VoiceBallPage(app).click_public_upper_wheat()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会公开娱乐房设置麦位闭麦状态")
    def test_public_close_wheat(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房设置麦位闭麦状态")
        value = VoiceBallPage(app).click_public_close_wheat()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会公开娱乐房邀请玩伴")
    def test_public_invite_playmate(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房邀请玩伴")
        value = VoiceBallPage(app).click_public_confirm()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会公开娱乐房静音")
    def test_public_close_voice(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房静音")
        value = VoiceBallPage(app).click_close_voice()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会公开娱乐房间中直接退出房间")
    def test_public_close_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房间中直接退出房间")
        value = VoiceBallPage(app).click_public_close_room()
        assert value == False

    @allure.story("测试公会公开娱乐房进入其他房间而退出房间")
    def test_public_other_close(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会公开娱乐房进入其他房间而退出房间")
        value = VoiceBallPage(app).click_public_enter_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部房进入高音质开黑房间")
    def test_enter_black_guild_house(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部房进入高音质开黑房间")
        value = VoiceBallPage(app).enter_black_guild_house()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部高音质开黑房普通成员上麦")
    def test_upper_black_guild_house(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部高音质开黑房普通成员上麦")
        value = VoiceBallPage(app).click_guild_upper_wheat()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部高音质开黑房设置麦位闭麦状态")
    def test_close_black_guild_house(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部高音质开黑房设置麦位闭麦状态")
        value = VoiceBallPage(app).click_guild_close_wheat()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部高音质开黑房邀请玩伴")
    def test_invite_black_group(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部高音质开黑房邀请玩伴")
        value = VoiceBallPage(app).click_guild_invite_group()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部高音质开黑房静音")
    def test_guild_close_voice(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部高音质开黑房静音")
        value = VoiceBallPage(app).click_guild_close_voice()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部高音质开黑房直接退出房间")
    def test_exit_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部高音质开黑房直接退出房间")
        value = VoiceBallPage(app).exit_room_guild()
        assert value == False

    @allure.story("测试公会内部高音质开黑房进入其他房间而退出房间")
    def test_enter_other_exit_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部高音质开黑房进入其他房间而退出房间")
        value = VoiceBallPage(app).enter_other_exit_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部房进入娱乐房间")
    def test_entertain_guild_house(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部房进入娱乐房间")
        value = VoiceBallPage(app).enter_entertain_guild_house()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部娱乐房普通成员上麦")
    def test_upper_entertain_guild_house(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部娱乐房普通成员上麦")
        value = VoiceBallPage(app).click_guild_entertainment()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部娱乐房邀请玩伴")
    def test_invite_entertainment_group(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部娱乐房邀请玩伴")
        value = VoiceBallPage(app).entertain_invite_group()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部娱乐房静音")
    def test_entertain_close_voice(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部娱乐房静音")
        value = VoiceBallPage(app).entertain_close_voice()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试公会内部娱乐房间中直接退出房间")
    def test_entertain_exit_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部娱乐房间中直接退出房间")
        value = VoiceBallPage(app).entertain_exit_room()
        assert value == False

    @allure.story("测试公会内部娱乐房进入其他房间而退出房间")
    def test_other_exit_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试公会内部娱乐房进入其他房间而退出房间")
        value = VoiceBallPage(app).other_exit_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试在房间内发起召集")
    def test_call_together(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在房间内发起召集")
        value = VoiceBallPage(app).click_call_together()
        assert value == True

    @allure.story("测试在房间内取消召集")
    def test_cancel_together(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在房间内取消召集")
        value = VoiceBallPage(app).click_cancel_together()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试房间tab进入没有密码的房间")
    def test_click_black_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试房间tab进入没有密码的房间")
        value = VoiceBallPage(app).click_black_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试在房间tab进入我收藏的房间")
    def test_enter_collection_room(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试房间tab进入我收藏的房间")
        value = VoiceBallPage(app).enter_collection_room()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试在房间tab进入最近进入的房间")
    def test_recently_entered_rooms(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试房间tab进入最近进入的房间")
        value = VoiceBallPage(app).recently_entered_rooms()
        VoiceBallPage(app).close_room()
        assert value == True

    @allure.story("测试在房间tab搜索个人房间")
    def test_search_personal_rooms(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在房间tab搜索个人房间")
        value = VoiceBallPage(app).click_search_view()
        assert value == True

    @allure.story("测试在房间tab查看大厅房间")
    def test_view_lobby_rooms(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在房间tab查看大厅房间")
        value = VoiceBallPage(app).view_lobby_rooms()
        assert value == True

    @allure.story("测试在房间tab查看热门房间")
    def test_view_popular_rooms(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在房间tab查看热门房间")
        value = VoiceBallPage(app).view_popular_rooms()
        assert value == True

    @allure.story("测试在房间tab查看公会房间")
    def test_view_guild_rooms(self, init_app_noreset):
        app = init_app_noreset
        VoiceBallPage(app).press("home")
        logger.info("Start 测试在房间tab查看公会房间")
        value = VoiceBallPage(app).view_guild_rooms()
        assert value == True

















