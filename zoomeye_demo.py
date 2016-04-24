#!/usr/bin/python
#coding:utf-8
import ZoomEyeSDK
import json

if __name__ == '__main__':
    g_strReqType = raw_input("请输入查询类型: ")
    g_strReqPage = raw_input("请输入查询页数: ")
    g_strReqData = raw_input("请输入查询内容: ")
    m_strUsername = "k0pwn_0110@sina.cn"
    m_strPasswd = "k0shl@0110_"
    m_strjsonToken = json.loads(ZoomEyeSDK.ZoomEye_Login(m_strUsername,m_strPasswd))
    m_strToken = m_strjsonToken["access_token"]
    print m_strToken
    m_strToken = "JWT "+m_strToken
    m_strjsonBaseInfo = json.loads(ZoomEyeSDK.ZoomEye_BaseInfo(m_strToken))
    print "主机信息: "+str(m_strjsonBaseInfo["resources"]["host-search"])
    print "WEB信息: "+str(m_strjsonBaseInfo["resources"]["web-search"])#打印基本信息
    if g_strReqType == "HOST":
        for i in range(1,int(g_strReqPage)+1):
            print ZoomEyeSDK.ZoomEye_HostData(g_strReqData,i,m_strToken)
    elif g_strReqType == "WEB":
        for i in range(1,int(g_strReqPage)+1):
            print ZoomEyeSDK.ZoomEye_WebData(g_strReqData,i,m_strToken)
    else:
        print "请重新输入查询类型,只能是HOST,WEB"