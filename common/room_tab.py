import uiautomator2 as u2
from pages.room_pages import RoomTabPages
import time
from common.do_uiautomator2 import UiAuto2
d = u2.connect()


class RoomPage(RoomTabPages):
    """房间tab"""

    def click_home_tab(self):
        """点击房间tab"""
        self.findId(**self.home_tab).click()

    def click_search(self):
        """点击全局搜索"""
        el = self.findId(**self.channel_tab_search)
        return self.clickElTime(el, **self.option_contact)

    def click_channel_tab_home(self):
        """点击开黑进房按钮"""
        self.findId(**self.channel_tab_home).click()

    def click_my_home(self):
        """点击进入我的房间"""
        self.click_channel_tab_home()
        el = self.findId(**self.enter_button)
        return self.clickElTime(el, **self.role_name)

    def view_list(self):
        """查看最近的访问列表"""
        el = self.findId(**self.channel_tab_home)
        return self.clickElTime(el, **self.group_name)

    def click_enter_room(self):
        """从最近访问的列表中进入房间"""
        self.click_channel_tab_home()
        el = self.findId(**self.enter_name)
        return self.clickElTime(el, **self.guild_id)

    def click_collection_button(self):
        """点击我的收藏按钮"""
        self.click_channel_tab_home()
        el = self.findClassText(**self.collect)
        return self.clickElTime(el, **self.channel_num)

    def click_enter(self):
        """点击进入按钮"""
        self.click_channel_tab_home()
        self.findId(**self.enter_button).click()

    def click_add(self):
        """点击房间内+号按钮"""
        self.click_enter()
        if self.findId("com.sabac.hy:id/current_mode_txt", timeout=5):
            self.findId(**self.enter_add).click()

    def click_order(self):
        """点击召集令"""
        self.click_add()
        self.findIdText(**self.order).click()

    def click_order_display(self):
        """点击召集令后弹出的确定按钮"""
        self.click_order()
        el = self.findId(**self.determine1)
        return self.clickElTime(el, **self.convene_display)

    def click_locked_room(self):
        """点击房间上锁"""
        self.click_add()
        self.findIdText(**self.locked_room).click()

    def click_submit(self):
        """输入房间密码点击提交"""
        self.click_locked_room()
        d.send_keys("1234", clear=True)
        self.findId(**self.submit_button).click()

    def click_locked(self):
        """选择任意的玩法后点击确定"""
        self.click_submit()
        self.findId(**self.channel_left_publish).click()
        self.findIdText(**self.entertainment_tag).click()
        self.findClassText(**self.define).click()

    def click_unlock_publish(self):
        """点击解锁并发布"""
        self.click_locked()
        el = self.findId(**self.unlock_publish)
        return self.clickElTime(el, **self.cancel_btn)

    def click_collection(self):
        """点击我的收藏按钮"""
        self.click_channel_tab_home()
        self.findClassText(**self.collect).click()

    def click_channel_name(self):
        """点击收藏的房间名"""
        self.click_collection()
        el = self.findId(**self.collect_channel_name)
        return self.clickElTime(el, **self.room_mode_txt)

    def click_long_room(self):
        """长按房间"""
        self.click_collection()
        x, y = self.findpic(**self.img_88)
        self.long_click(x, y)

    def click_remove_collect(self):
        """点击长按房间后弹出的确定按钮"""
        self.click_long_room()
        self.findIdText(**self.determine).click()
        return UiAuto2().get_toast()

    def close_room(self):
        """点击退出房间"""
        self.findId(**self.title_more).click()
        self.findId(**self.close_room_menu).click()
        time.sleep(2)

    def click_room_add(self):
        """点击房间tab右上角的+号按钮"""
        UiAuto2().xpath(self.room_add)

    def select_game_tag(self):
        """选择游戏标签"""
        self.click_room_add()
        self.findIdText(**self.game_tag).click()

    def click_game_tag(self):
        """选择游戏标签后点击确定"""
        self.select_game_tag()
        el = self.findClassText(**self.define)
        return self.clickElTime(el, **self.game_mode_txt)

    def select_entertainment_tag(self):
        """选择娱乐标签"""
        self.click_room_add()
        self.findIdText(**self.entertainment_tag).click()

    def click_entertainment_tag(self):
        """选择娱乐标签后点击确定"""
        self.select_entertainment_tag()
        el = self.findClassText(**self.define)
        return self.clickElTime(el, **self.entertainment_mode_txt)

    def click_entertain_room(self):
        """选择娱乐标签后点击确定"""
        self.select_entertainment_tag()
        el = self.findClassText(**self.define)
        return self.clickElTime(el, **self.cancel_btn)

    def click_back(self):
        """返回到房间tab"""
        self.click_enter()
        time.sleep(4)
        for i in range(2):
            self.press("back")

    def external_select_tag(self):
        """在房间外部重新发布其他的房间"""
        self.click_back()
        self.select_entertainment_tag()

    def click_external(self):
        """外部房间选择后点击确定"""
        self.external_select_tag()
        el = self.findClassText(**self.define)
        return self.clickElTime(el, **self.cancel_btn)

    def click_find_someone(self):
        """点击找人玩按钮"""
        self.click_enter()
        self.findId(**self.channel_left_publish).click()

    def select_room_rule(self):
        """选择房间玩法"""
        self.click_find_someone()
        self.findIdText(**self.entertainment_tag).click()

    def click_define(self):
        """房间玩法选择后点击确定"""
        self.select_room_rule()
        el = self.findClassText(**self.define)
        return self.clickElTime(el, **self.cancel_btn)

    def click_view_group(self):
        """点击速配队友"""
        self.findId(**self.view_group).click()

    def click_arrange(self):
        """点击安排一下"""
        self.click_view_group()
        el = self.findId(**self.arrange_it)
        return self.clickElTime(el, **self.title_more_button)

    def list_display(self):
        """列表展示"""
        el = self.findId(**self.home_tab)
        return self.clickElTime(el, **self.head_desc)

    def filter_tag(self):
        """点击筛选标签再点击游戏标签"""
        self.findId(**self.filter_button).click()
        self.findClassText(**self.select_tag).click()

    def click_peace_tag(self):
        """选中游戏标签后点击确定按钮"""
        self.filter_tag()
        el = self.findId(**self.filter_confirm)
        return self.clickElTime(el, **self.peace_tag)

    def click_del_filter(self):
        """点击标签右边X按钮"""
        self.filter_tag()
        self.findId(**self.filter_confirm).click()
        el = self.findId(**self.del_filter)
        return self.clickElTime(el, **self.recommend_tip)

    def click_head_desc(self):
        """点击任意的有空麦的房间"""
        self.findId(**self.head_desc_2).click()
        time.sleep(6)

    def click_immediately_wheat(self):
        """点击立即上麦"""
        self.click_head_desc()
        el = self.findId(**self.immediately_wheat)
        return self.clickElTime(el, **self.img_99)

    def click_enter_my_room(self):
        """点击进入我的房间"""
        self.click_channel_tab_home()
        self.findId(**self.enter_button).click()

    def click_switch_high(self):
        """点击切换高音质房间"""
        self.click_enter_my_room()
        self.findIdText(**self.current_txt).click()
        el = self.findClassText(**self.high_quality)
        return self.clickElTime(el, **self.gang_up)

    def click_desc(self):
        """点击房间tab里面的任意一个推荐房"""
        self.findId(**self.head_desc_2).click()
        self.findId(**self.room_collect).click()
        return UiAuto2().get_toast()

    def click_desc_room(self):
        """点击房间tab里面的任意一个推荐房，在点击房间的个人名称"""
        self.findId(**self.head_desc_2).click()
        time.sleep(1)
        self.findId(**self.tag_name).click()
        time.sleep(2)

    def click_view_information(self):
        """点击查看资料"""
        self.click_desc_room()
        elp = self.findpic(**self.img_1)
        return self.clickElTime(el=None, **self.follow_button, pos=elp)

    def click_say_hello(self):
        """点击打招呼"""
        self.click_desc_room()
        elp = self.findpic(**self.img_2)
        return self.clickElTime(el=None, **self.voice_btn, pos=elp)

    def click_alone_say_hello(self):
        """点击打招呼后再点击关注"""
        self.click_desc_room()
        x, y = self.findpic(**self.img_2)
        self.click(x, y)
        el = self.findId(**self.add_friend)
        return self.clickElTime(el, **self.tv_content)

    def click_message(self):
        """点击房间内信息按钮"""
        self.click_enter_my_room()
        self.findId(**self.message_btn).click()

    def send_message(self):
        """输入框中输入内容"""
        self.click_message()
        self.findId(**self.message_input).send_keys("一帆风顺")

    def click_send_btn(self):
        """点击发送按钮"""
        self.send_message()
        el = self.findId(**self.send_btn)
        return self.clickElTime(el, **self.send_context)

    def click_face(self):
        """点击表情图标选择表情"""
        self.click_message()
        self.findId(**self.face_btn).click()
        self.findId(**self.select_face).click()

    def send_face(self):
        """发送表情"""
        self.click_face()
        el = self.findId(**self.send_btn)
        return self.clickElTime(el, **self.face_context)

    def click_image(self):
        """点击图片按钮并点击从相册中选取"""
        self.click_message()
        self.findId(**self.image_btn).click()
        self.findClassText(**self.picture_btn).click()

    def select_pic(self):
        """选择图片"""
        self.click_image()
        UiAuto2().xpath(self.picture_select)

    def screen_send_picture(self):
        """点击发送"""
        self.select_pic()
        el = self.findId(**self.pager_send_view)
        return self.clickElTime(el, **self.img_3)

    def click_mute(self):
        """点击房间内静音按钮"""
        self.click_enter_my_room()
        self.findId(**self.mute_btn).click()
        return UiAuto2().get_toast()

    def click_img_4(self):
        """点击麦克风图标"""
        self.click_enter_my_room()
        x, y = self.findpic(**self.img_4)
        self.click(x, y)

    def click_close_wheat(self):
        """点击设为闭麦位按钮"""
        self.click_img_4()
        el = self.findIdText(**self.close_wheat)
        return self.clickElTime(el, **self.status_img)

    def click_locked_wheat(self):
        """点击锁麦按钮"""
        self.click_img_4()
        el = self.findIdText(**self.suo_mai)
        return self.clickElTime(el, **self.img_5)

    def click_msg_entrance(self):
        """点击快捷回复消息图标"""
        self.click_enter_my_room()
        self.findId(**self.msg_entrance).click()

    def send_msg_entrance(self):
        """发消息给玩伴"""
        self.click_msg_entrance()
        self.findId(**self.et_input).send_keys("一帆风顺")
        el = self.findId(**self.chatting_sent_btn)
        value = self.clickElTime(el, **self.message_read_status)
        return value

    def click_message_playmate(self):
        """点击快捷回复界面玩伴按钮"""
        self.click_msg_entrance()
        el = self.findClassText(**self.company_man)
        value = self.clickElTime(el, **self.company_name)
        return value

    def click_room_management(self):
        """点击房间管理"""
        self.click_add()
        el = self.findIdText(**self.room_management)
        return self.clickElTime(el, **self.change_bg)

    def click_turn_on_mode(self):
        """点击K歌模式"""
        self.click_add()
        self.findIdText(**self.turn_on_mode).click()
        return UiAuto2().get_toast()

    def click_open_ear_function(self):
        """点击耳返功能"""
        self.click_add()
        self.findIdText(**self.open_ear_function).click()
        return UiAuto2().get_toast()

    def click_feed_back(self):
        """点击意见反馈按钮和输入意见反馈内容"""
        self.click_add()
        self.findIdText(**self.feed_back).click()
        self.findId(**self.input_box).send_keys("欢游好好玩，继续保持！！")

    def click_send_opinion(self):
        """点击意见反馈界面发送按钮"""
        self.click_feed_back()
        UiAuto2().xpath(self.send_opinion)
        return UiAuto2().get_toast()

    def click_lock_wheat(self):
        """点击自动锁麦"""
        self.click_add()
        self.findIdText(**self.lock_wheat).click()
        return UiAuto2().get_toast()

    def click_close_screen(self):
        """点击关闭公屏按钮再点击是按钮"""
        self.click_add()
        self.findIdText(**self.public_screen).click()
        el = self.findId(**self.yes_confirm)
        return self.clickElTime(el, **self.close_public_screen)

    def click_room_locked(self):
        """点击房间上锁按钮"""
        self.click_add()
        self.findIdText(**self.room_locked).click()

    def click_submission(self):
        """输入密码点击提交按钮"""
        self.click_room_locked()
        d.send_keys("1111", clear=True)
        self.findId(**self.submission_btn).click()
        return UiAuto2().get_toast()

    def click_right_button(self):
        """点击房间右上角更多按钮"""
        self.click_enter()
        self.findId(**self.title_more).click()

    def click_pack_up_room(self):
        """点击收起点击按钮"""
        self.click_right_button()
        el = self.findId(**self.pack_up_room)
        return self.clickElTime(el, **self.suspension_ball)

    def click_close_room(self):
        """点击退出房间按钮"""
        self.click_right_button()
        el = self.findId(**self.close_room_menu)
        return self.clickElTime(el, **self.get_into)

    def click_btn_ball(self):
        """点击悬浮球"""
        self.click_right_button()
        self.findId(**self.pack_up_room).click()
        el = self.findId(**self.btn_ball)
        return self.clickElTime(el, **self.title_more_button)

    def drag_btn_ball(self):
        """拖动悬浮球"""
        self.click_right_button()
        self.findId(**self.pack_up_room).click()
        d(**self.btn_ball).drag_to(0.394, 0.895)
        return UiAuto2().get_toast()


































