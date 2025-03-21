# 导入自动化模块
from DrissionPage import ChromiumPage
#导入csv模块
import csv
#创建文件对象
f = open("jingdong.csv",mode = "w",encoding = "utf-8-sig",newline="")
csv_writer = csv.DictWriter(f,fieldnames=[
    "评论",
    "时间",
    "产品",
    "评分",
])
csv_writer.writeheader()
#实例话浏览器对象
dp = ChromiumPage()
#监听数据包
dp.listen.start('api.m.jd.com')
#访问网站
dp.get("https://detail.tmall.com/item.htm?abbucket=13&id=655618258908&ns=1&pisk=g_5t3txlBy3Ozrq8b1yHoazKTy4HMJbajG7SinxihMIdlHc07C22MiKd0hvM1hcvMZIVmiQ47EtfciKcIJVl7NR2GujYZ7bwLcp0PGKXcXaXkEMb-diO5Cu6GuquMv0BQlAfjJEe6DMBzHT6lKM_JBTvPmOXCFNQJETmfxG1cyQBYFM65ATjRvterAM6ldgBdUYs5nGfcwapoUAXci96rKZJ0bxoMTFLaYx-lghjG6L9dJb6Az1NOFLw2Nt3e8B2WdK55HZySkYBHGpOt5nyW9_RYFI4afR6HO6W1sE86B_PKGTdcuHvATCNMLfT2Y-1_nSJ19EI6IOwyZplKrMJxt_F9pCTEq8FsZ1wEQNrfnXhysLAgoPd2NsOFL1sXgzlZ_p6s0xJoAaLJxk2CeupXDhHjwq9HeKu-IDq3pFvJ34pVxk2C38pqyPS3xJLB&priceTId=undefined&skuId=5317743273465&spm=a21n57.1.hoverItem.2&utparam=%7B%22aplus_abtest%22%3A%223de019b0b77801b3153647caf0852d5c%22%7D&xxc=taobaoSearch")
# for page in range(100):
#     print(f"正在采集第{page+1}页的数据内容")
for page in range(100):
    print(f"正在采集第{page+1}页")
    dp.scroll.to_bottom()
# 点击下一页
    dp.ele("css:.ui-pager-next").click()

    #等待数据包加载
    resp = dp.listen.wait()
    #获取响应数据
    json_data = resp.response.body
    #解析数据
    comments = json_data["comments"]
    # #for循环命令
    for index in comments:
    #提取具体信息
        dit = {
        "评论":index["content"],
        "时间":index["creationTime"],
        "产品":index["productColor"],
        "评分":index["score"],
        }
        #写入数据
        csv_writer.writerow(dit)
        print(dit)

