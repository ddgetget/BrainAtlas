import re

my_url = '''<img alt="冥王星小瑞塔的直播" data-original="https://rpic.douyucdn.cn/live-cover/roomCover/2018/07/05/f156a1f2e0bfd49cd18052e53594cd69_small.jpg" src="https://rpic.douyucdn.cn/live-cover/roomCover/2018/07/05/f156a1f2e0bfd49cd18052e53594cd69_small.jpg" width="283" height="163" class="JS_listthumb" style="display: block;">'''

# 默认是贪婪模式： 根据正则表达式尽量多匹配数据
# 非贪婪： 在范围正则表达式代码后面加上?, 比如: *?, +?, ??
# 非贪婪的含义： ?后面的数据不要前面的正则表达式进行匹配，自己进行匹配
match_obj = re.search("https?://.*?\.jpg", my_url)
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")


match_obj = re.match(r"#.*?#", "#sdfa#sd#")

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")