import time
import pytest
import allure
from common.room_tab import RoomPage
from common.project_path import screen_path
from common.Logger import MyLog
logger = MyLog()


@allure.feature("测试房间tab")
class TestRoom:

    @allure.story("测试点击搜索")
    def test_click_search(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试点击搜索")
        value = RoomPage(app).click_search()
        assert value == True

    @allure.story("测试进入我的房间")
    def test_my_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试进入我的房间")
        value = RoomPage(app).click_my_home()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试查看最近访问列表")
    def test_view_list(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试查看最近访问列表")
        value = RoomPage(app).view_list()
        assert value == True

    @allure.story("测试从最近访问记录进入房间")
    def test_enter_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试从最近访问记录进入房间")
        value = RoomPage(app).click_enter_room()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试查看收藏列表")
    def test_view_collect(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试查看收藏列表")
        value = RoomPage(app).click_collection_button()
        assert value == True

    @allure.story("测试取消收藏房间")
    def test_remove_collect(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试取消收藏房间")
        value = RoomPage(app).click_remove_collect()
        assert value == "已取消收藏"

    @allure.story("测试收到召集令显示")
    def test_order_display(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试收到召集令显示")
        value = RoomPage(app).click_order_display()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试成功进入已收藏的房间")
    def test_collection_success(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试成功进入已收藏的房间")
        value = RoomPage(app).click_channel_name()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试发布游戏房间")
    def test_game_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发布游戏房间")
        value = RoomPage(app).click_game_tag()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试发布娱乐房间")
    def test_entertainment_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试发布娱乐房间")
        value = RoomPage(app).click_entertainment_tag()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试不在房间时发布房间")
    def test_entertain_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试不在房间时发布房间")
        value = RoomPage(app).click_entertain_room()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试房间中外部发布房间")
    def test_external_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试房间中外部发布房间")
        value = RoomPage(app).click_external()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试房间中房间内发布房间")
    def test_inside_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试房间中房间内发布房间")
        value = RoomPage(app).click_define()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试房间上锁发布房间")
    def test_locked_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试房间上锁发布房间")
        value = RoomPage(app).click_unlock_publish()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试速配队友进房")
    def test_match_teammates(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试速配队友进房")
        value = RoomPage(app).click_arrange()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试列表展示")
    def test_list_display(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试列表展示")
        value = RoomPage(app).list_display()
        assert value == True

    @allure.story("测试筛选标签")
    def test_filter_tag(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试筛选标签")
        value = RoomPage(app).click_peace_tag()
        assert value == True

    @allure.story("测试删除筛选标签")
    def test_filter_tag(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试删除筛选标签")
        value = RoomPage(app).click_del_filter()
        assert value == True

    @allure.story("测试被邀请上麦弹窗")
    def test_wheat_window(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试被邀请上麦弹窗")
        value = RoomPage(app).click_immediately_wheat()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试切换高音质开黑房")
    def test_switch_high(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试切换高音质开黑房")
        value = RoomPage(app).click_switch_high()
        RoomPage(app).close_room()
        assert value == True

    @allure.story("测试进入高音质开黑房收藏房间")
    def test_switch_collect(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试进入高音质开黑房收藏房间")
        value = RoomPage(app).click_desc()
        RoomPage(app).close_room()
        assert value == "已收藏"

    @allure.story("测试个人卡片查看资料")
    def test_view_information(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试个人卡片查看资料")
        value = RoomPage(app).click_view_information()
        assert value == True

    @allure.story("测试个人卡片打招呼")
    def test_view_information(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试个人卡片打招呼")
        value = RoomPage(app).click_say_hello()
        assert value == True

    @allure.story("测试锁麦")
    def test_locked_wheat(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试锁麦")
        value = RoomPage(app).click_locked_wheat()
        assert value == True

    @allure.story("测试个人卡片关注玩伴")
    def test_add_friends(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试个人卡片关注玩伴")
        value = RoomPage(app).click_alone_say_hello()
        assert value == True

    @allure.story("测试公屏发送图片且公屏上正常显示")
    def test_screen_send_picture(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试公屏发送图片且公屏上正常显示")
        value = RoomPage(app).screen_send_picture()
        assert value == True

    @allure.story("测试公屏发送文字且公屏上正常显示")
    def test_speaking_text(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试公屏发言文字且公屏上正常显示")
        value = RoomPage(app).click_send_btn()
        assert value == True

    @allure.story("测试公屏发送表情且公屏上正常显示")
    def test_screen_send_expression(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试公屏发送表情且公屏上正常显示")
        value = RoomPage(app).send_face()
        assert value == True

    @allure.story("测试静音")
    def test_mute(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试静音")
        value = RoomPage(app).click_mute()
        assert value == "静音中"

    @allure.story("测试闭麦")
    def test_close_wheat(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试闭麦")
        value = RoomPage(app).close_wheat()
        assert value == True

    @allure.story("测试快捷消息回复")
    def test_send_msg_entrance(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试快捷消息回复")
        value = RoomPage(app).send_msg_entrance()
        assert value == True

    @allure.story("测试快捷消息玩伴")
    def test_message_playmate(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试快捷消息玩伴")
        value = RoomPage(app).click_message_playmate()
        assert value == True

    @allure.story("测试跳转到房间管理")
    def test_room_management(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试跳转到房间管理")
        value = RoomPage(app).click_room_management()
        assert value == True

    @allure.story("测试打开K歌模式")
    def test_turn_on_mode(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试打开K歌模式")
        value = RoomPage(app).click_turn_on_mode()
        assert "K歌模式已开启" in value

    @allure.story("测试打开耳返功能")
    def test_open_ear_function(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试打开耳返功能")
        value = RoomPage(app).click_open_ear_function()
        assert value == "耳返模式已开启"

    @allure.story("测试进行意见反馈")
    def test_feedback(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试进行意见反馈")
        value = RoomPage(app).click_send_opinion()
        assert "谢谢您的反馈" in value

    @allure.story("测试打开自动锁麦")
    def test_lock_wheat(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试打开自动锁麦")
        value = RoomPage(app).click_lock_wheat()
        assert "自动锁麦已开启" in value

    @allure.story("测试关闭公屏")
    def test_close_screen(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试关闭公屏")
        value = RoomPage(app).click_close_screen()
        assert value == True

    @allure.story("测试房间上锁")
    def test_room_lock(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试房间上锁")
        value = RoomPage(app).click_submission()
        assert value == "房间已上锁"

    @allure.story("测试收起房间")
    def test_retract_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试收起房间")
        value = RoomPage(app).click_pack_up_room()
        assert value == True

    @allure.story("测试退出房间")
    def test_close_room(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试退出房间")
        value = RoomPage(app).click_close_room()
        assert value == True

    @allure.story("测试点击悬浮球回到房间")
    def test_btn_ball(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试点击悬浮球回到房间")
        value = RoomPage(app).click_btn_ball()
        assert value == True

    @allure.story("测试拖动悬浮球退出房间")
    def test_drag_btn_ball(self, init_app_noreset):
        app = init_app_noreset
        logger.info("Start 测试拖动悬浮球退出房间")
        value = RoomPage(app).drag_btn_ball()
        assert "已退出房间" in value








































