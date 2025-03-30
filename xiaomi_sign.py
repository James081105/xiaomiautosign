import requests
import re
from urllib.parse import quote
#github：James081105原创 bilibili：James-520 公众号：James吖
def extract_miui_vip_ph(cookie):
    """从cookie中提取miui_vip_ph参数"""
    pattern = r'miui_vip_ph=([^;]+)'
    match = re.search(pattern, cookie)
    if match:
        return match.group(1)
    return None

def checkin(cookie):
    """执行签到操作"""
    # 从cookie中提取miui_vip_ph
    miui_vip_ph = extract_miui_vip_ph(cookie)
    if not miui_vip_ph:
        print("未找到miui_vip_ph参数")
        return False

    # 设置请求URL和参数
    url = 'https://api.vip.miui.com/mtop/planet/vip/user/checkinV2'
    params = {
        'ref': 'vipAccountShortcut',
        'pathname': '/mio/checkIn',
        'version': 'dev.250321',
        'miui_version': 'V14.0.27.0.TMRCNXM',
        'android_version': '13',
        'oaid': '05e13b9fa7c836c5',
        'device': 'marble',
        'restrict_imei': '',
        'miui_big_version': 'V130',
        'model': quote('Redmi Note 12 Turbo'),
        'androidVersion': '13',
        'miuiBigVersion': 'V130',
        'miui_vip_ph': miui_vip_ph
    }

    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 23049RAD8C Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36XiaoMi/HybridView/ app/vipaccount/dev.250321',
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Origin': 'https://web.vip.miui.com',
        'X-Requested-With': 'com.xiaomi.vipaccount',
        'Referer': 'https://web.vip.miui.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie
    }

    # 设置表单数据
    data = {
        'token': 'Oafd30L2H0XB7oVcSGPfpLP9ZN53SbuYCTdgJOxKE+G83nhY3gDtNH/fp92xqxZhOOwueQUAURhmIPPBPyPP+3aDMt40at5aTi4LgimrHD+KPJfu4HcaeBzH4oxLfw25t/0hFIRHfVFs7Y6RcH7WJJ7MWA7R1Po/fUD0X+DqTApEVchbLtaunmdXj/FE4+DK8Om4wSvelMTzxyIF5gJYc1fG3RdYIw5TzokPkDooTsDMQhMTcwQVE/S+3Rj416h0xJjEEDk5GPia0tj9FM92bAbF8WBcOsXWGLKaC0RT6waYxm6vP4DfsmBIX/sAHbFP',
        'miui_vip_ph': miui_vip_ph
    }

    try:
        response = requests.post(url, params=params, headers=headers, data=data)
        result = response.json()
        print(f"签到结果: {result}")
        return result.get('status') == 200
    except Exception as e:
        print(f"签到失败: {str(e)}")
        return False

if __name__ == "__main__":
    print("github：James081105原创 bilibili：James-520 公众号：James吖")
    # 这里填入你的cookie
    cookie = "cUserId=vvHGMrmirMgHc1yPr6T5uEOYzwQ; userId=bb4e5fc54a143770b8061d31cbe813fe; miui_vip_ph=yMH5ojWsG1ONUVGHFsBr9g==; miui_vip_slh=Qw8r8WbP3d2PwNjLVr29WBNduyw=; miui_vip_serviceToken=eFjqQoE9kM35o+Ds9nKkOxq1sw0fGtHMVUCNjlayxhnyRlFE/01x2TwBsJkJI7bg0MtQMYTdwuoGyWQ6JrYOiL+u3lNzegV9QhZBiA6eQnhAeAa8i8cnyyTWZCFEHkXOLg7dtT1q69XP8qW46v5BGwlVKcJvezdKzXQ9oXmIxblghN7eLSuT1YWyDB+GC+mPhIZ/IThLmJ5FDemSzwAyh9hoN/f0yCfKerfITveaYkCHhh9Jbjg3UGVKJQw7VAJb3H6sMFLpK4G+du+7Vo8j7g=="
    
    success = checkin(cookie)
    if success:
        print("签到成功！")
        print("github：James081105原创 bilibili：James-520 公众号：James吖")
    else:
        print("签到失败！") 
        print("github：James081105原创 bilibili：James-520 公众号：James吖")