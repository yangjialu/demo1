import random
from pages.base import BasePage
from common.project_path import screen_path


class MsgTabPages(BasePage):
    input_box = {"idname": "com.sabac.hy:id/chatting_edit_rel"}  # 消息输入框
    send_button = {"idname": "com.sabac.hy:id/chatting_sent_btn"}  # 消息发送按钮
    num = random.randint(1, 100)
    str2 = "趣丸a{}".format(num)  # 输入的文本/字母/数字
    send_str = {"checkId": "com.sabac.hy:id/tv_chatcontent", "checkText": "{}".format(str2)}  # 已发送的文本信息定位
    read_status = {"checkId": "com.sabac.hy:id/tv_message_read_status"}  # 送达元素定位
    picture_send_button = {"idname": "com.sabac.hy:id/picture_pager_send_view"}  # 图片发送按钮
    click_picture_2= {"idname": "com.sabac.hy:id/image_content_panel"}  # 点击图片
    img = {"img": screen_path + "/123.png"}  # 点击图片后与原图对比的截图
    send_face_2 = {"checkId": "com.sabac.hy:id/tv_chatcontent", "checkText": "[t000/微笑]"}  # 默认的表情图标
    send_confirm = {"idname": "com.sabac.hy:id/dialog_confirm"}  # 发送并进房按钮
    gift_icon = {"checkId": "com.sabac.hy:id/channel_entertainment_gift_icon"}  # 房间礼物按钮
    portal = {"checkId": "com.sabac.hy:id/content_text_view", "checkText": "传送门已为你开启，快来找我一起浪！"}  # 传送门
    close_room = {"idname": "com.sabac.hy:id/tv_channel_top_menu_close"}  # 退出房间按钮
    add_face = {"idname": "com.sabac.hy:id/tv_dialog_select_text", "textname": "添加到表情"}  # 添加到表情按钮
    add_friend = {"idname": "com.sabac.hy:id/add_friend"}  # 关注按钮
    add_success = {"checkId": "com.sabac.hy:id/tv_chatcontent", "checkText": "我关注了你，互相关注并已成为玩伴，可以愉快地玩耍啦"}  # 关注成功后的提示语
    member_face = {"idname": "com.sabac.hy:id/tempgroup_member_face"}  # 成员图标
    user_id = {"checkId": "com.sabac.hy:id/tv_user_detail_header_id"}  # 玩伴id
    red_point = {"checkId": "com.sabac.hy:id/red_point"}  # 未读消息
    all_person = {"idname": "com.sabac.hy:id/at_group_at_all"}  # 全体成员
    system_msg = {"checkId": "com.sabac.hy:id/chatting_system_tv"}  # 第四次@全体成员后系统提示的信息
    follow_button = {"checkId": "com.sabac.hy:id/tv_user_detail_to_follow"}  # 点击取消关注后出现关注按钮
    button = {"idname": "com.sabac.hy:id/tv_user_detail_to_follow"}  # 点击关注
    dialog_cancel = {"idname": "com.sabac.hy:id/dialog_cancel"}  # 不再关注按钮
    later_on = {"idname": "com.sabac.hy:id/dialog_cancel"}  # 稍后再说按钮
    system_tv = {"checkId": "com.sabac.hy:id/chatting_system_tv"}  # 创建群成功后提示语
    section_name = {"checkId": "com.sabac.hy:id/section_name"}  # 公会群主
    group_button = {"classname": "android.widget.TextView", "textname": "群组"}  # 群组按钮
    fans_enter = {"idname": "com.sabac.hy:id/fans_enter_icon"}  # 粉丝按钮
    user_name = {"checkId": "com.sabac.hy:id/user_name", "checkText": "妙妙"}  # 粉丝用户名
    default_img = {"img": screen_path + '/default.png'}  # 默认表情
    face_button = {"idname": "com.sabac.hy:id/chatting_face_btn"}  # 表情按钮
    shou_cang = {"imgName": screen_path + "/shoucang.png"}  # 收藏按钮
    bian_ji = {"img": screen_path + "/bianji.png"}  # 自定义表情列表
    remen = {"imgName": screen_path + "/remen.png"}  # 热门按钮
    re_men = {"img": screen_path + "/re_men.png"}  # 热门表情列表
    send_view = {"idname": "com.sabac.hy:id/picture_pager_send_view"}  # 选择图片后的添加按钮
    img_44 = {"img": screen_path + "/44.png"}  # 添加图片后查询是否添加成功
    home_message = {"idname": "com.sabac.hy:id/home_message_red_point"}  # 消息tab按钮
    message_title = {"idname": "com.sabac.hy:id/message_title_tv", "textname": "妙妙"}  # 进入消息对话界面
    add_button = {"idname": "com.sabac.hy:id/chatting_more_menu_btn_ll"}  # 加号按钮
    picture_button = {"idname": "com.sabac.hy:id/chatting_menu_name_view_tv", "textname": "照片"}  # 图片按钮
    together_button = {"idname": "com.sabac.hy:id/chatting_menu_name_view_tv", "textname": "一起玩"}  # 一起玩按钮
    more_button = {"idname": "com.sabac.hy:id/channel_chatting_title_more"}  # 房间右上角更多按钮
    select_picture_2 = '//*[@resource-id="com.sabac.hy:id/picture_grid_view"]/android.widget.FrameLayout[10]'  # 选择要发的图片
    num = random.randint(1, 20)
    select_face_2= '//*[@resource-id="com.sabac.hy:id/emoticons_grid"]/android.widget.LinearLayout[{}]/android.widget.ImageView[1]'.format(
        num)  # 选择随机的表情
    face_default = {"idname": "com.sabac.hy:id/emoticon_view"}  # 选择的默认表情
    select_right = '//androidx.appcompat.widget.LinearLayoutCompat'  # 消息界面右上角图标
    clear_chat_2 = {"classname": "android.widget.TextView", "textname": "清空聊天记录"}  # 清空聊天记录按钮
    click_confirm = {"idname": "com.sabac.hy:id/dialog_confirm"}  # 点击确定按钮
    collect_picture = '//*[@resource-id="com.sabac.hy:id/v_tt_data_list"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]'  # 收藏图标
    edit_add = {"idname": "com.sabac.hy:id/sticker_item_add_layout"}  # 编辑增加按钮
    greet_person = {"idname": "com.sabac.hy:id/message_title_tv"}  # 打招呼的人的id
    img_greet = {"imgName": screen_path + "/11.png"}  # 打招呼的图标
    ignore_message = {"imgName": screen_path + "/22.png"}  # 忽略消息的图标
    guild_group = {"idname": "com.sabac.hy:id/message_title_tv", "textname": "东方风格风光总群"}  # 公会总群
    switch = {"imgName": screen_path + "/33.png"}  # 切换到玩伴的图标
    friend_pic = {"imgName": screen_path + "/44.png"}  # 玩伴图标
    more_friend = {"idname": "com.sabac.hy:id/img_user_detail_more"}  # 玩伴右上角的更多按钮
    cancel_connect = {"idname": "com.sabac.hy:id/menu_item_text", "textname": "取消关注"}  # 取消关注按钮
    signature = {"idname": "com.sabac.hy:id/signature"}  # 进入玩伴个人资料
    establish_button = '//androidx.appcompat.widget.LinearLayoutCompat'  # 创建按钮
    interest_group_name = {"idname": "com.sabac.hy:id/interest_group_name_et"}  # 创建群输入框名称
    str_group = '你好{}'.format(num)  # 群名称
    edit = {"idname": "com.sabac.hy:id/sticker_item_add_layout"}  # 编辑按钮
    add = {"idname": "com.sabac.hy:id/sticker_add_item_tv"}  # 添加按钮
    picture_pager = '//*[@resource-id="com.sabac.hy:id/picture_grid_view"]/android.widget.FrameLayout[19]'
    img_55 = {"imgName": screen_path + "/55.png"}  # 我的表情界面的编辑按钮
    all_select = {"idname": "com.sabac.hy:id/manage_sticker_selected_all_cb"}  # 全选按钮
    delete_btn = {"idname": "com.sabac.hy:id/manage_sticker_delete_btn"}  # 删除已选表情按钮
    img_77 = {"imgName": screen_path + "/77.png"}  # 要发送的热门表情
    img_66 = {"imgName": screen_path + "/66.png"}  # 要添加的热门表情
    select_text = {"idname": "com.sabac.hy:id/tv_dialog_select_text", "textname": "添加到表情"}  # 添加到表情按钮
    fans_enter_icon = {"idname": "com.sabac.hy:id/fans_enter_icon"}  # 粉丝按钮
