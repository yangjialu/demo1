import uiautomator2 as u2
from pages.voice_ball_pages import VoicePages
import time
from common.do_uiautomator2 import UiAuto2
d = u2.connect()


class VoiceBallPage(VoicePages):

    def click_voice_sign(self):
        """点击语音球图标"""
        x, y = self.findpic(**self.img_7)
        self.click(x, y)

    def click_group_mark(self):
        """点击语音球里面群标志"""
        self.click_voice_sign()
        self.findId(**self.group_mark).click()

    def click_back(self):
        """点击返回"""
        self.click_group_mark()
        self.press("back")
        if self.findpic(**self.img_6):
            return True
        else:
            return False

    def click_clear_chat(self):
        """语音球中点击清除聊天记录"""
        self.findId(**self.more_menu).click()
        self.findClassText(**self.clear_chat).click()

    def sent_msg_display(self):
        """发送文本信息正常显示"""
        self.click_voice_sign()
        self.findId(**self.input_txt).send_keys(self.str_msg)
        el = self.findId(**self.sent_btn)
        return self.clickElTime(el, **self.msg_context)

    def sent_msg_success(self):
        """发送文本信息成功"""
        self.click_voice_sign()
        self.findId(**self.input_txt).send_keys(self.str_msg)
        el = self.findId(**self.sent_btn)
        return self.clickElTime(el, **self.read_status)

    def sent_pic_display(self):
        """点击图片按钮"""
        self.click_voice_sign()
        self.findId(**self.photo_btn).click()

    def select_picture(self):
        """选择图片"""
        self.sent_pic_display()
        self.findId(**self.select_photo).click()

    def click_send_image(self):
        """选择图片后点击发送"""
        self.select_picture()
        el = self.findId(**self.send_image)
        return self.clickElTime(el, **self.content_container)

    def click_send_image_success(self):
        """选择图片后点击发送"""
        self.select_picture()
        el = self.findId(**self.send_image)
        return self.clickElTime(el, **self.read_status)

    def click_sent_picture(self):
        """点击已发送的图片查看大图"""
        self.select_picture()
        self.findId(**self.send_image).click()
        el = self.findId(**self.sent_pic)
        return self.clickElTime(el, **self.big_pic)

    def click_face_btn(self):
        """点击表情图标"""
        self.click_voice_sign()
        self.findId(**self.face_btn).click()

    def select_face_1(self):
        """选择表情"""
        self.click_face_btn()
        self.findId(**self.select_face).click()

    def send_face_success(self):
        """点击发送按钮"""
        self.select_face_1()
        el = self.findId(**self.sent_btn)
        return self.clickElTime(el, **self.read_status)

    def send_face_display(self):
        """发送的表情正常显示"""
        self.select_face_1()
        el = self.findId(**self.sent_btn)
        return self.clickElTime(el, **self.msg_content)

    def click_collect_btn(self):
        """点击收藏按钮"""
        self.click_face_btn()
        x, y = self.findpic(**self.img_10)
        self.click(x, y)

    def select_collect_face(self):
        """发送收藏的表情并正常显示"""
        self.click_collect_btn()
        el = self.findId(**self.sticker_image)
        return self.clickElTime(el, **self.content_container)

    def select_collect_face_success(self):
        """发送收藏的表情并提示成功"""
        self.click_collect_btn()
        el = self.findId(**self.sticker_image)
        return self.clickElTime(el, **self.read_status)

    def click_more_menu(self):
        """点击消息界面右上角..."""
        self.click_voice_sign()
        self.findId(**self.more_menu).click()

    def click_open_in(self):
        """点击在欢游中打开"""
        self.click_more_menu()
        el = self.findClassText(**self.open_in_hy)
        return self.clickElTime(el, **self.voice_btn)

    def clear_msg(self):
        """清空聊天记录"""
        self.click_voice_sign()
        self.findId(**self.input_txt).send_keys(self.str_msg)
        self.findId(**self.sent_btn).click()
        self.click_clear_chat()
        if self.findIdText(**self.msg_context2, timeout=3):
            return True
        else:
            return False

    def click_room_btn(self):
        """点击房间按钮"""
        self.click_voice_sign()
        self.findClassText(**self.room_btn).click()

    def close_room(self):
        """退出房间"""
        self.findId(**self.quit_button).click()
        self.findId(**self.confirm_button).click()

    def enter_my_room(self):
        """点击进入我的房间"""
        self.click_room_btn()
        el = self.findId(**self.room_title)
        return self.clickElTime(el, **self.music_icon)

    def judgement_black_room(self):
        """判断是否是开黑房"""
        self.click_room_btn()
        self.findId(**self.room_title).click()
        if self.findIdText(**self.entertainment_btn, timeout=2):
            self.findIdText(**self.entertainment_btn).click()
            self.findClassText(**self.black_room).click()

    def judgement_entertainment_room(self):
        """判断是否是娱乐房"""
        self.click_room_btn()
        self.findId(**self.room_title).click()
        if self.findIdText(**self.black_btn, timeout=2):
            self.findIdText(**self.black_btn).click()
            self.findClassText(**self.entertain_room).click()

    def click_enter_my_room(self):
        """进入到娱乐房间点击空麦位"""
        self.judgement_entertainment_room()
        self.findId(**self.empty).click()

    def click_enter_my_room_1(self):
        """进入到开黑房间点击空麦位"""
        self.judgement_black_room()
        self.findId(**self.empty).click()

    def click_upper_wheat(self):
        """娱乐房点击上麦按钮"""
        self.click_enter_my_room()
        el = self.findIdText(**self.upper_wheat)
        return self.clickElTime(el, **self.success)

    def click_upper_wheat_1(self):
        """开黑房点击上麦按钮"""
        self.click_enter_my_room_1()
        el = self.findIdText(**self.upper_wheat)
        return self.clickElTime(el, **self.success)

    def click_close_wheat(self):
        """娱乐房点击闭麦位按钮"""
        self.judgement_entertainment_room()
        x, y = self.findpic(**self.img_04)
        self.click(x, y)
        el = self.findIdText(**self.close_wheat)
        return self.clickElTime(el, **self.success_wheat)

    def click_close_wheat_1(self):
        """开黑房点击闭麦位按钮"""
        self.judgement_black_room()
        x, y = self.findpic(**self.img_04)
        self.click(x, y)
        el = self.findIdText(**self.close_wheat)
        return self.clickElTime(el, **self.success_wheat)

    def click_more_button(self):
        """娱乐房点击右下角更多按钮"""
        self.judgement_entertainment_room()
        self.findId(**self.more_btn).click()

    def click_more_button_1(self):
        """开黑房点击右下角更多按钮"""
        self.judgement_black_room()
        self.findId(**self.more_btn).click()

    def click_invite_friend(self):
        """娱乐房点击邀请玩伴按钮"""
        self.click_more_button()
        self.findIdText(**self.invite_friend).click()

    def click_invite_friend_1(self):
        """开黑房点击邀请玩伴按钮"""
        self.click_more_button_1()
        self.findIdText(**self.invite_friend).click()

    def click_float_name(self):
        """娱乐房选择联系人"""
        self.click_invite_friend()
        self.findId(**self.float_name).click()

    def click_float_name_1(self):
        """开黑房选择联系人"""
        self.click_invite_friend_1()
        self.findId(**self.float_name).click()

    def click_confirm_btn(self):
        """娱乐房点击发送按钮"""
        self.click_float_name()
        el = self.findId(**self.confirm_btn)
        return self.clickElTime(el, **self.img_02)

    def click_confirm_btn_1(self):
        """开黑房点击发送按钮"""
        self.click_float_name_1()
        el = self.findId(**self.confirm_btn)
        return self.clickElTime(el, **self.img_02)

    def click_silence_button(self):
        """娱乐房点击静音按钮"""
        self.click_more_button()
        el = self.findIdText(**self.silence_btn)
        return self.clickElTime(el, **self.silence_in)

    def click_silence_button_1(self):
        """开黑房点击静音按钮"""
        self.click_more_button_1()
        el = self.findIdText(**self.silence_btn)
        return self.clickElTime(el, **self.silence_in)

    def click_close_room(self):
        """点击退出房间按钮"""
        self.enter_my_room()
        self.close_room()
        time.sleep(0.5)
        if self.findpic(**self.img_03, timeout=2):
            return True
        else:
            return False

    def click_room(self):
        """进入娱乐房后点击房间按钮"""
        self.judgement_entertainment_room()
        self.findClassText(**self.room_btn).click()

    def click_room_1(self):
        """进入开黑房后点击房间按钮"""
        self.judgement_black_room()
        self.findClassText(**self.room_btn).click()

    def click_hot(self):
        """娱乐房点击热门按钮再选择任意的热门房间"""
        self.click_room()
        self.findClassText(**self.hot_btn).click()
        self.findId(**self.hot_title).click()

    def click_hot_1(self):
        """开黑房点击热门按钮再选择任意的热门房间"""
        self.click_room_1()
        self.findClassText(**self.hot_btn).click()
        self.findId(**self.hot_title).click()

    def click_btn_confirm(self):
        """娱乐房选择好热门房间后点击弹出的确定按钮"""
        self.click_hot()
        el = self.findId(**self.btn_confirm)
        return self.clickElTime(el, **self.collect_button)

    def click_btn_confirm_1(self):
        """开黑房选择好热门房间后点击弹出的确定按钮"""
        self.click_hot_1()
        el = self.findId(**self.btn_confirm)
        return self.clickElTime(el, **self.collect_button)

    def enter_in_my_room(self):
        """进入我的房间"""
        self.click_room_btn()
        self.findId(**self.room_title).click()

    def switch_to_entertainment(self):
        """切换至娱乐房间"""
        self.enter_in_my_room()
        self.findIdText(**self.black_btn).click()
        el = self.findClassText(**self.entertain_room)
        return self.clickElTime(el, **self.entertainment_btn_1)

    def switch_to_black(self):
        """切换至开黑房间"""
        self.enter_in_my_room()
        self.findIdText(**self.entertainment_btn).click()
        el = self.findClassText(**self.black_room)
        return self.clickElTime(el, **self.black_btn_1)

    def click_public_room(self):
        """点击公会房间按钮"""
        self.click_room_btn()
        self.findClassText(**self.public_btn).click()

    def click_public_test(self):
        """点击公会测试房"""
        self.click_public_room()
        el = self.findIdText(**self.public_test)
        return self.clickElTime(el, **self.public_test_display)

    def enter_public_room(self):
        """进入公会测试房点击空麦位"""
        self.click_public_room()
        self.findIdText(**self.public_test).click()
        self.findId(**self.empty).click()

    def enter_public_room_1(self):
        """进入公会测试房点击空麦位"""
        self.click_public_room()
        self.findIdText(**self.public_test).click()
        x, y = self.findpic(**self.img_04)
        self.click(x,y)

    def click_public_upper_wheat(self):
        """点击公会测试上麦按钮"""
        self.enter_public_room()
        el = self.findIdText(**self.upper_wheat)
        return self.clickElTime(el, **self.success)

    def click_public_close_wheat(self):
        """点击公会测试闭麦按钮"""
        self.enter_public_room_1()
        el = self.findIdText(**self.close_wheat)
        return self.clickElTime(el, **self.success_wheat)

    def click_public_more_btn(self):
        """点击公会公开房右下角三个点按钮"""
        self.click_public_room()
        self.findIdText(**self.public_test).click()
        self.findId(**self.more_btn).click()

    def click_public_invite(self):
        """点击邀请玩伴按钮"""
        self.click_public_more_btn()
        self.findIdText(**self.invite_friend).click()

    def select_contacts(self):
        """选择联系人"""
        self.click_public_invite()
        self.findId(**self.float_name).click()

    def click_public_confirm(self):
        """点击发送按钮"""
        self.select_contacts()
        el = self.findId(**self.confirm_btn)
        return self.clickElTime(el, **self.img_02)

    def click_close_voice(self):
        """点击公会娱乐房静音按钮"""
        self.click_public_more_btn()
        el = self.findIdText(**self.silence_btn)
        return self.clickElTime(el, **self.silence_in)

    def click_public_close_room(self):
        """从公会房间退出房间"""
        self.click_public_room()
        self.findIdText(**self.public_test).click()
        self.close_room()
        time.sleep(0.5)
        if self.findpic(**self.img_03, timeout=2):
            return True
        else:
            return False

    def enter_to_other_room(self):
        """进入到其他的房间后再退出"""
        self.findClassText(**self.room_btn).click()  # 点击房间按钮
        # 点击热门按钮
        self.findClassText(**self.hot_btn).click()
        # 点击任意的热门房间
        self.findId(**self.hot_title).click()
        # 点击确定
        el = self.findId(**self.btn_confirm)
        return self.clickElTime(el, **self.collect_button)

    def click_public_enter_room(self):
        """进入公会房间后再进入其他的任意房间在退出"""
        self.click_public_room()
        self.findIdText(**self.public_test).click()
        return self.enter_to_other_room()

    def click_common_upper_wheat(self):
        """点击空麦位再点击上麦"""
        self.findId(**self.empty).click()
        el = self.findIdText(**self.upper_wheat)
        return self.clickElTime(el, **self.success)

    def click_common_close_wheat(self):
        """点击空麦位再点击设为闭麦位"""
        x, y = self.findpic(**self.img_04)
        self.click(x, y)
        el = self.findIdText(**self.close_wheat)
        return self.clickElTime(el, **self.success_wheat)

    def click_common_more_btn(self):
        """点击语音房间三个点按钮后再点击静音按钮"""
        self.findId(**self.more_btn).click()
        el = self.findIdText(**self.silence_btn)
        return self.clickElTime(el, **self.silence_in)

    def click_common_invite_btn(self):
        """点击语音房间三个点按钮后再点击邀请玩伴"""
        self.findId(**self.more_btn).click()
        self.findIdText(**self.invite_friend).click()
        self.findId(**self.float_name).click()
        el = self.findId(**self.confirm_btn)
        return self.clickElTime(el, **self.img_02)

    def enter_guild_house(self):
        """进入公会内部房"""
        self.click_public_room()
        self.findIdText(**self.guild_house).click()

    def enter_entertain_guild_house(self):
        """进入公会内部娱乐房"""
        self.click_public_room()
        el = self.findIdText(**self.guild_house)
        return self.clickElTime(el, **self.music_icon)

    def enter_black_guild_house(self):
        """进入公会内部开黑房"""
        self.click_public_room()
        el = self.findIdText(**self.guild_house)
        return self.clickElTime(el, **self.music_icon)

    def judge_room_type_black(self):
        """判断房间是否是开黑房"""
        if self.findIdText(**self.entertainment_btn, timeout=2):
            self.findIdText(**self.entertainment_btn).click()
            self.findClassText(**self.black_room).click()

    def click_guild_upper_wheat(self):
        """开黑房点击上麦"""
        self.enter_guild_house()
        self.judge_room_type_black()
        return self.click_common_upper_wheat()

    def click_guild_close_wheat(self):
        """开黑房点击设为闭麦位"""
        self.enter_guild_house()
        self.judge_room_type_black()
        return self.click_common_close_wheat()

    def click_guild_invite_group(self):
        """开黑房点击邀请玩伴"""
        self.enter_guild_house()
        self.judge_room_type_black()
        return self.click_common_invite_btn()

    def click_guild_close_voice(self):
        """开黑房点击静音"""
        self.enter_guild_house()
        self.judge_room_type_black()
        return self.click_common_more_btn()

    def exit_room_guild(self):
        """开黑房直接退出房间"""
        self.enter_guild_house()
        self.judge_room_type_black()
        self.close_room()
        time.sleep(0.5)
        if self.findpic(**self.img_03, timeout=2):
            return True
        else:
            return False

    def enter_other_exit_room(self):
        """进入到其他房间再退出"""
        self.enter_guild_house()
        self.judge_room_type_black()
        return self.enter_to_other_room()

    def judge_room_type_entertain(self):
        """判断房间是否是娱乐房"""
        if self.findIdText(**self.black_btn, timeout=2):
            self.findIdText(**self.black_btn).click()
            self.findClassText(**self.entertain_room).click()

    def click_guild_entertainment(self):
        """娱乐房点击上麦"""
        self.enter_guild_house()
        self.judge_room_type_entertain()
        return self.click_common_upper_wheat()

    def entertain_invite_group(self):
        """娱乐房点击邀请玩伴"""
        self.enter_guild_house()
        self.judge_room_type_entertain()
        return self.click_common_invite_btn()

    def entertain_close_voice(self):
        """娱乐房点击静音"""
        self.enter_guild_house()
        self.judge_room_type_entertain()
        return self.click_common_more_btn()

    def entertain_exit_room(self):
        """娱乐房直接退出房间"""
        self.enter_guild_house()
        self.judge_room_type_entertain()
        self.close_room()
        time.sleep(0.5)
        if self.findpic(**self.img_03, timeout=2):
            return True
        else:
            return False

    def other_exit_room(self):
        """进入到其他房间再退出"""
        self.enter_guild_house()
        self.judge_room_type_entertain()
        return self.enter_to_other_room()

    def click_call_together(self):
        """点击一键召集再点击确定"""
        self.click_room_btn()
        self.findId(**self.room_title).click()
        self.findId(**self.more_btn).click()
        self.findIdText(**self.invite_more).click()
        el = self.findId(**self.dialog_confirm)
        return self.clickElTime(el, **self.invite_num)

    def enter_together(self):
        """进入已经召集的房间点击已召集"""
        self.click_room_btn()
        self.findId(**self.room_title).click()
        self.findId(**self.invite).click()

    def click_cancel_together(self):
        """点击取消召集"""
        self.enter_together()
        self.findId(**self.cancel_invite).click()
        self.findId(**self.dialog_confirm).click()
        if self.findId(**self.invite, timeout=2):
            return False
        else:
            return True

    def click_black_room(self):
        """点击任意的开黑房间"""
        self.click_room_btn()
        self.findId(**self.friend_name).click()
        el = self.findId(**self.btn_confirm)
        return self.clickElTime(el, **self.music_icon)

    def enter_collection_room(self):
        """进入收藏的房间"""
        self.click_room_btn()
        el = self.findIdText(**self.room_number)
        return self.clickElTime(el, **self.music_icon)

    def recently_entered_rooms(self):
        """进入最近进入的房间"""
        self.click_room_btn()
        size = UiAuto2().get_size()
        x = size[0]
        y = size[1]
        time.sleep(1)
        self.swipe(x*0.1, y*0.9, x*0.1, y*0.1)
        el = self.findIdText(**self.room_number)
        return self.clickElTime(el, **self.music_icon)

    def click_search_view(self):
        """点击搜索框并且输入房间id"""
        self.click_room_btn()
        self.findId(**self.search_view).click()
        d.send_keys("50002", clear=True)
        el = self.findId(**self.v_search)
        return self.clickElTime(el, **self.channel_count)

    def view_lobby_rooms(self):
        """点击大厅"""
        self.click_room_btn()
        el = self.findClassText(**self.hall_btn)
        return self.clickElTime(el, **self.guild_room_title)

    def view_popular_rooms(self):
        """点击热门房间"""
        self.click_room_btn()
        el = self.findClassText(**self.hot_btn)
        return self.clickElTime(el, **self.hot_channel_title)

    def view_guild_rooms(self):
        """点击热门房间"""
        self.click_room_btn()
        el = self.findClassText(**self.public_btn)
        return self.clickElTime(el, **self.guild_room_title)




























