import pymysql, pyodbc

def main():
    sql = "'conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=test;DATABASE=test;UID=user;PWD=password')'"
    conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 10.0};SERVER=172.21.2.58,3433;DATABASE=BW_Contract;UID=sa;PWD=kj222')
    # conn = pymysql.connect(host='172.21.2.58', database='BW_Contract',user='sa', password='kj222')
    
    # cur = conn.cursor()
    # cur.execute("SELECT TOP 1000 [Type],[Name]FROM m_Type2 where Type=16")
    cursor = conn.cursor()
    #cursor.execute("select user_id, user_name from users")
    cursor.execute("SELECT TOP 1000 [Type],[Name]FROM m_Type2 where Type=16")
    row = cursor.fetchone()
    if row:
        print(row)

if __name__ == '__main__':
    main()