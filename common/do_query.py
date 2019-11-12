import time


class DoQuery:

    now = time.time()
    t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now-60*60))
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now+60*60))

    def do_query_click(self, uid, pageid, eventid, info='*,toDateTime(client_timestamp)'):
        '''查询语句：点击事件查询语句,uid查询'''
        query = "select {0} from  ods_app_exposure_event_click_all where uid={1} " \
                "and client_timestamp >= '{2}' " \
                "and client_timestamp<'{3}' " \
                "and eventId='{4}' " \
                "and pageId='{5}' " \
                "order by client_timestamp desc".format(info,uid, self.t1, self.t2,eventid,pageid)
        return query

    def do_query_click_device(self, deviceId, pageid, eventid, info='*,toDateTime(client_timestamp)'):
        '''查询语句：点击事件查询语句,设备查询'''
        query = "select {0} from  ods_app_exposure_event_click_all where deviceId='{1}' " \
                "and client_timestamp >= '{2}' " \
                "and client_timestamp<'{3}' " \
                "and eventId='{4}' " \
                "and pageId='{5}' " \
                "order by client_timestamp desc".format(info, deviceId, self.t1, self.t2, eventid, pageid)
        return query

    def do_query_exposure(self, uid, pageid, info='*,toDateTime(client_timestamp)'):
        '''查询语句：曝光事件查询语句，uid查询'''
        query = "select {0} from  ods_app_exposure_event_all " \
                "where uid={1} " \
                "and client_timestamp >= '{2}' " \
                "and client_timestamp<'{3}' " \
                "and pageId='{4}' " \
                "order by client_timestamp desc".format(info, uid, self.t1, self.t2, pageid)
        return query

    def do_query_exposure_matchkey(self, uid, pageid, info='*,toDateTime(client_timestamp)', pageExt='pageExt'):
        '''查询语句：曝光事件查询语句，uid查询,matchkey值不为空'''
        query = "select {0} from  ods_app_exposure_event_all " \
                "where uid={1} " \
                "and client_timestamp >= '{2}' " \
                "and client_timestamp<'{3}' " \
                "and pageId='{4}' " \
                "and length(matchkey)!=0 " \
                "and pageExt='{5}'" \
                "order by client_timestamp desc".format(info,uid, self.t1, self.t2,pageid,pageExt)
        return query

    def do_query_exposure_matchkey_none(self, uid, pageid, info='*,toDateTime(client_timestamp)', pageExt='pageExt'):
        '''查询语句：曝光事件查询语句，uid查询,matchkey值为空'''
        query = "select {0} from  ods_app_exposure_event_all " \
                "where uid={1} " \
                "and client_timestamp >= '{2}' " \
                "and client_timestamp<'{3}' " \
                "and pageId='{4}' " \
                "and length(matchkey)=0 " \
                "and pageExt='{5}'" \
                "order by client_timestamp desc".format(info,uid, self.t1, self.t2, pageid, pageExt)
        return query

    def do_query_ods_topic(self, postId):
        """查询语句：根据帖子id查询用户id"""
        query="select uid from  ods_topic_log_all where postId='{0}'".format(postId)
        return query

    def do_query_exposureweb(self, uid, pageid, pageExt, info='*,toDateTime(client_timestamp)'):
        '''查询web曝光事件，根据pageid和pageExt查询'''
        query = "select {0} from  ods_app_exposure_event_all " \
                "where uid={1} " \
                "and client_timestamp >= '{2}' " \
                "and client_timestamp<'{3}' " \
                "and pageId='{4}' " \
                "and pageExt='{5}'"\
                "order by client_timestamp desc".format(info, uid, self.t1, self.t2, pageid, pageExt)
        return query

    def do_query_uid(self,uid,point):
        '''查询语句：根据uid查询'''
        query= "select *,toDateTime(client_timestamp) from  ods_app_exposure_event_click_all where uid={0} " \
                 "and client_timestamp >= '{1}' and client_timestamp<'{2}' " \
                 "and eventId='{3}' order by client_timestamp desc limit 50".format(uid, self.t1, self.t2, point)

        return query

    def do_query_device(self,device,point):
        '''查询语句：根据设备id查询'''
        query= "select *,toDateTime(client_timestamp) from  ods_app_exposure_event_click_all where deviceId='{0}' " \
                 "and client_timestamp >= '{1}' and client_timestamp<'{2}' " \
                 "and eventId='{3}' order by client_timestamp desc limit 50".format(device, self.t1, self.t2, point)

        return query

    def do_uid(self, ttid):
        '''查询语句：根据ttid查询ttuid'''
        query="select uid from  dwd_user_tt_all where ttId='{0}'".format(ttid)
        return query

    def do_query_uid_uid(self, uid, point):
        '''查询语句：根据uid查询配对的人的uid,有些表pageExt为TTid'''
        query= "select pageExt from  ods_app_exposure_event_click_all where uid={0} " \
                 "and client_timestamp >= '{1}' and client_timestamp<'{2}' " \
                 "and eventId='{3}' order by client_timestamp desc limit 50".format(uid, self.t1, self.t2, point)
        return query

    def do_query_uid_channelID(self, uid, eventid, pageid):
        '''查询语句：根据uid查询广场进入对应的房间类型和对应的房间id'''
        query = "select pageExt,channelID from  ods_app_exposure_event_click_all where uid={0} " \
                "and client_timestamp >= '{1}' " \
                "and client_timestamp<'{2}' " \
                "and eventId='{3}' " \
                "and pageId='{4}' " \
                "order by client_timestamp desc".format(uid, self.t1, self.t2, eventid, pageid)
        return query

    '''使用eventID+eventExt查询'''

    def do_query_EventEXT(self, uid, point, eventExt):
        query = "select *,toDateTime(client_timestamp) from  ods_app_exposure_event_click_all where uid={0} " \
                "and client_timestamp >= '{1}' and client_timestamp<'{2}' " \
                "and eventId='{3}' and eventExt='{4}'order by client_timestamp desc limit 50".format(uid, self.t1,
                                                                                                     self.t2, point,
                                                                                                     eventExt)
        return query

    '''进入圈子的查询语句，根据pageID和eventID查询'''

    def do_query_PageID(self, uid, point, pageId):
        query = "select *,toDateTime(client_timestamp) from  ods_app_exposure_event_click_all where uid={0} " \
                "and client_timestamp >= '{1}' and client_timestamp<'{2}' " \
                "and eventId='{3}' and pageId='{4}'order by client_timestamp desc limit 50".format(uid, self.t1,
                                                                                                   self.t2, point,
                                                                                                   pageId)
        return query

    '''在圈子内关注用户的查询语句，需要查看pageExt是否对应圈子的ID'''

    def do_query_PageEXT(self, uid, point, pageExt):
        query = "select *,toDateTime(client_timestamp) from  ods_app_exposure_event_click_all where uid={0} " \
                "and client_timestamp >= '{1}' and client_timestamp<'{2}' " \
                "and eventId='{3}' and pageExt='{4}'order by client_timestamp desc limit 50".format(uid, self.t1,
                                                                                                    self.t2, point,
                                                                                                    pageExt)
        return query


if __name__ == '__main__':
    # query2 = DoQuery().do_query_exposureweb(861932,'chat_page','ttyuyinzhushou')
    query1 = DoQuery().do_query_exposure(861932, 'guild_channel_page', 'event,matchkey')
    print(query1)