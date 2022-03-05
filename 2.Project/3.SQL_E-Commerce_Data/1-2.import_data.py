##
import pandas as pd
import numpy as np
import seaborn as sns

from sqlalchemy import create_engine
import pymysql
import pandas as pd

pymysql.install_as_MySQLdb()


df_customer = pd.read_csv("/Users/parksungwon/Documents/1-3.project_3/US_ecommerce_customer_stats.csv")
df_records = pd.read_csv("/Users/parksungwon/Documents/1-3.project_3/US_ecommerce_records.csv")


# engine = create_engine('mysql+mysqldb://root:enqnenqn@localhost:3306/e_commerce',encoding='utf-8')
# #engine = create_engine('mysql+mysqldb://root:workbench mysql 비밀번호입력 @localhost:3306/데이터베이스이름',encoding='utf-8')
# conn = engine.connect()
# df.to_sql(name='customer_stats', con=conn, if_exists='append', index=False)
# #데이터프레임.to_sql(name='sql 내 테이블 명', con=conn, if_exists = 'append', index=False)
# conn.close()
