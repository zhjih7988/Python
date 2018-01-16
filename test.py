# -*- coding:utf-8 -*-  
#https://github.com/rg3/youtube-dl/blob/master/README.md#readme


def main():
    date = '2018-01-22'
    try:
        date = date.split('-')
        date = '%04d-%02d-%02d' % (int(date[0]), int(date[1]), int(date[2]))
        print(date)
    except:
        print("请输入有效的时间格式，例如：2018-1-9 或 2018-01-09")
        return













if __name__ == '__main__':
    main()