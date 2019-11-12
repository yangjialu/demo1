import uiautomator2 as u2
from pages.message_pages import MsgTabPages
import time
from common.do_uiautomator2 import UiAuto2
d = u2.connect()


class MessagePage(MsgTabPages):
        """消息tab"""

        def click_home_message(self):
            """点击消息tab按钮"""
            self.findId(**self.home_message).click()

        def click_fans2(self):
            """点击粉丝按钮"""
            self.click_home_message()
            el = self.findId(**self.fans_enter_icon)
            return self.clickElTime(el, **self.user_name)

        def click_message_title(self):
            """点击进入消息对话界面"""
            self.click_home_message()
            self.findIdText(**self.message_title).click()

        def click_default_display(self):
            """点击表情按钮"""
            self.click_message_title()
            el = self.findId(**self.face_button)
            return self.clickElTime(el, **self.default_img)

        def send_message(self):
            """输入框中输入内容后发送"""
            self.click_message_title()
            self.findId(**self.input_box).click()
            d.send_keys(self.str2, clear=True)
            el = self.findId(**self.send_button)
            return self.clickElTime(el, **self.send_str)

        def send_message_success(self):
            """发送消息后消息左上角提示送达"""
            self.click_message_title()
            self.findId(**self.input_box).click()
            d.send_keys(self.str2, clear=True)
            el = self.findId(**self.send_button)
            return self.clickElTime(el, **self.read_status)

        def click_add_button(self):
            """点击加号按钮"""
            self.click_message_title()
            self.findId(**self.add_button).click()

        def click_picture_button(self):
            """点击图片按钮"""
            self.click_add_button()
            self.findIdText(**self.picture_button).click()

        def select_picture(self):
            """点击选择的图片"""
            self.click_picture_button()
            UiAuto2().xpath(self.select_picture_2)

        def send_picture(self):
            """发送图片和点击图片缩略图查看大图"""
            self.select_picture()
            el = self.findId(**self.picture_send_button)
            value = self.clickElTime(el, **self.read_status)
            el2 = self.findId(**self.click_picture_2)
            value2 = self.clickElTime(el2, **self.img)
            return value, value2

        def click_face(self):
            """点击表情按钮"""
            self.click_message_title()
            self.findId(**self.face_button).click()

        def custom_display(self):
            """点击收藏自定义表情不为空"""
            self.click_face()
            elp = self.findpic(**self.shou_cang)
            return self.clickElTime(el=None, **self.bian_ji, pos=elp)

        def hot_display(self):
            """点击热门表情按钮展示正常"""
            self.click_face()
            elp = self.findpic(**self.remen)
            return self.clickElTime(el=None, **self.re_men, pos=elp)

        def click_sc(self):
            """点击收藏按钮"""
            self.click_face()
            x, y = self.findpic(**self.shou_cang)
            self.click(x, y)

        def click_editing(self):
            """点击编辑按钮"""
            self.click_sc()
            self.findId(**self.edit).click()

        def click_edit(self):
            """点击我的表情界面的编辑按钮"""
            self.click_editing()
            x, y = self.findpic(**self.img_55)
            self.click(x, y)

        def click_all_election(self):
            """点击全选按钮"""
            self.click_edit()
            self.findId(**self.all_select).click()

        def click_del_face(self):
            """点击删除已选表情按钮"""
            self.click_all_election()
            self.findId(**self.delete_btn).click()

        def del_custom(self):
            """点击删除自定义表情"""
            self.click_del_face()
            el = self.findId(**self.send_confirm)
            return self.clickElTime(el, **self.re_men)

        def click_add(self):
            """点击添加按钮"""
            self.click_editing()
            self.findId(**self.add).click()

        def click_picture(self):
            """点击要添加的图片"""
            self.click_add()
            UiAuto2().xpath(self.picture_pager)

        def add_custom(self):
            """点击添加自定义表情"""
            self.click_picture()
            el = self.findId(**self.send_view)
            return self.clickElTime(el, **self.img_44)

        def send_face(self):
            """点击发送热门表情"""
            self.click_face()
            x, y = self.findpic(**self.remen)
            self.click(x, y)
            x, y = self.findpic(**self.img_77)
            self.click(x, y)

        def long_select(self):
            """长按消息页面中表情"""
            self.send_face()
            x, y = self.findpic(**self.img_66)
            self.long_click(x, y, duration=0.5)

        def click_select_text(self):
            """点击添加到表情按钮"""
            self.long_select()
            self.findIdText(**self.select_text).click()

        def long_ck(self):
            """直接长按消息页面中表情"""
            self.click_message_title()
            x, y = self.findpic(**self.img_66)
            self.long_click(x, y, duration=0.5)

        def click_text(self):
            """点击添加到表情按钮"""
            self.long_ck()
            self.findIdText(**self.select_text).click()

        def select_face(self):
            """选择随机表情"""
            self.click_face()
            UiAuto2().xpath(self.select_face_2)

        def send_face_random(self):
            """选择随机表情后点击发送"""
            self.select_face()
            el = self.findId(**self.send_button)
            return self.clickElTime(el, **self.read_status)

        def select_face_default(self):
            """选择默认的表情"""
            self.click_face()
            self.findId(**self.face_default).click()

        def send_face_success(self):
            """选择默认表情后点击发送"""
            self.select_face_default()
            el = self.findId(**self.send_button)
            return self.clickElTime(el, **self.send_face_2)

        def clear_chat(self):
            """清空聊天记录"""
            UiAuto2().xpath(self.select_right)
            self.findClassText(**self.clear_chat_2).click()
            self.findId(**self.click_confirm).click()

        def send_my_room(self):
            """发送我的房间传送门"""
            self.click_add_button()
            self.findIdText(**self.together_button).click()

        def click_send_confirm(self):
            """房间传送门选择好点击确定按钮"""
            self.send_my_room()
            el = self.findId(**self.send_confirm)
            value = self.clickElTime(el, **self.gift_icon)
            self.click_more()
            el2 = self.findId(**self.close_room)
            value2 = self.clickElTime(el2, **self.portal)
            return value, value2

        def click_more(self):
            """点击更多按钮"""
            self.findId(**self.more_button).click()

        def click_greet_person(self):
            """点击和你打招呼的人"""
            self.click_home_message()
            x, y = self.findpic(**self.img_greet)
            self.click(x, y)
            self.findId(**self.greet_person).click()

        def click_add_friend(self):
            """点击关注按钮"""
            self.click_greet_person()
            el = self.findId(**self.add_friend)
            return self.clickElTime(el, **self.add_success)

        def click_friend(self):
            """查看玩伴信息"""
            self.click_message_title()
            UiAuto2().xpath(self.select_right)

        def click_member_face(self):
            """点击成员图标"""
            self.click_friend()
            el = self.findId(**self.member_face)
            return self.clickElTime(el, **self.user_id)

        def click_ignore_message(self):
            """点击忽略消息按钮"""
            self.click_home_message()
            x, y = self.findpic(**self.ignore_message)
            self.click(x, y)

        def click_ignore_send(self):
            """点击忽略信息后点击确定按钮"""
            self.click_ignore_message()
            el = self.findId(**self.send_confirm)
            return self.clickElTime(el, **self.red_point)

        def click_guild_group(self):
            """点击进入选择的公会总群"""
            self.click_home_message()
            self.findIdText(**self.guild_group).click()

        def click_all_person(self):
            """输入@全体成员3次"""
            self.click_guild_group()
            for i in range(3):
                self.findId(**self.input_box).click()
                d.send_keys("@")
                self.findId(**self.all_person).click()
                self.findId(**self.send_button).click()

        def click_four_people(self):
            """第四@全体成员"""
            self.click_all_person()
            self.findId(**self.input_box).click()
            d.send_keys("@", clear=True)
            self.findId(**self.all_person).click()
            el = self.findId(**self.send_button)
            return self.clickElTime(el, **self.system_msg)

        def switch_friend(self):
            """点击切换到玩伴页面"""
            self.click_home_message()
            x, y = self.findpic(**self.switch)
            self.click(x, y)

        def click_more_button(self):
            """点击玩伴右上角的更多按钮"""
            self.switch_friend()
            self.findId(**self.signature).click()
            self.findId(**self.more_friend).click()

        def click_cancel(self):
            """点击取消关注按钮"""
            self.click_more_button()
            self.findIdText(**self.cancel_connect).click()

        def remove_concerns(self):
            """点击不在关注"""
            self.click_cancel()
            el = self.findId(**self.dialog_cancel)
            value = self.clickElTime(el, **self.follow_button)
            self.findId(**self.button).click()
            return value

        def noremove_concerns(self):
            """点击我手滑了"""
            self.click_cancel()
            el = self.findId(**self.send_confirm)
            value = self.clickElTime(el, **self.follow_button)
            return value

        def click_group(self):
            """点击群组按钮"""
            self.switch_friend()
            self.findClassText(**self.group_button).click()

        def view_group(self):
            """点击群组按钮查看"""
            self.click_group()
            el = self.findClassText(**self.group_button)
            return self.clickElTime(el, **self.section_name)

        def establish_group(self):
            """点击创建群和输入群名称"""
            self.click_group()
            UiAuto2().xpath(self.establish_button)
            self.findId(**self.interest_group_name).click()
            d.send_keys(self.str_group)
            UiAuto2().xpath(self.establish_button)

        def click_later_on(self):
            """创建房间后点击稍后再说按钮"""
            self.establish_group()
            el = self.findId(**self.later_on)
            return self.clickElTime(el, **self.system_tv)


if __name__ == '__main__':
    pass





















