import requests as r
import re
import json
import time
total = 0
for i in range(0,99):
    try:
        kv = {"Host":"club.jd.com","Referer":"https://item.jd.com/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",'Cookie':'__jda=122270672.686255361.1663426070.1664099539.1664101609.7; unpl=JF8EAK1nNSttWBhcAxxWGUJHTQlXWwpaSB4BPzQDAFpaQlEFHgFMERB7XlVdXhRKHx9sYxRUXFNIUg4fCysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrBRIVE09ZVlldOHsQM19XDVBeWk9XNRoyGiJSHwFSX10LTR9OaG4CV1lcSVMFKwMrEQ; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1b976e3af7e24fc283ab7e6384142f21|1664072879059; __jdu=686255361; areaId=1; ipLoc-djd=1-2802-54745-0; shshshfpb=jLl9spXiK3nW8GxNgeKug8g; shshshfp=e2b17eda11c3b9b68fcfe24214ee3d40; shshshfpa=6011cd29-5bcc-42c4-b8cb-5da51a419123-1645335498; PCSYCityID=CN_510000_510100_0; ip_cityCode=1930; __jdc=122270672; JSESSIONID=D10304AF2FC6990A77CE872625BA0C49.s1; jwotest_product=99; jsavif=1; token=64a6e5f7e0bfa8f4f8ab911002bebef5,2,924500; __tk=66a4654c55e4d969d87395d720a34e84,2,924500; shshshsID=a5d63f5161a51d4f0f4b18a8c13f5c0c_1_1664101608712; __jdb=122270672.1.686255361|7.1664101609; 3AB9D23F7A4B3C9B=IGAP4IYIPGB6VQTORC653ILT5NMGEKGL5NJ6LROCEKPNIJWGWNZHOBU54EUU523MI2DTXYMDOGI3XHIG66EQLFZD2Q'}
        t = r.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(i),headers=kv)
        t.raise_for_status
        t.encoding = t.apparent_encoding
        txt = re.findall(u'\(.*\)',t.text)
        txt = txt[0]
        txt = txt[1:-1]
        
        info = json.loads(txt)
        ans = ''
        for k in range(10):
            ans += '{}:\n'.format(total)
            total = total + 1
            ans += '{}'.format(info['comments'][k]['id'])
            ans += '\n'
            ans += info['comments'][k]['nickname']
            ans += '\n'
            ans += info['comments'][k]['creationTime']
            ans += '\n'
            ans += info['comments'][k]['content']
            ans += '\n\n\n'
        with open('comments.txt','a+',encoding='utf-8') as f:
            f.write(ans)
        t.close
        time.sleep(10)
        print('\r{}'.format(i),end='')
    except:
        pass
    