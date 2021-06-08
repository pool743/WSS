from pmaw import PushshiftAPI
import datetime
import mysql.connector
from configparser import ConfigParser



""" Retreive SQL credentials from ini """
config = ConfigParser()
file='sql_credentials.ini'
config.read(file)
sql_credentials = config['VALUES']



""" MAKING REQUEST """
api = PushshiftAPI()
startTime = int(datetime.datetime(2021, 5, 18, 0, 0).timestamp())
endTime = int(datetime.datetime(2021, 5, 19, 0, 0).timestamp())
subreddit='wallstreetbets'

""" CONNECTING TO DATABASES """
mydb = mysql.connector.connect(
  host=sql_credentials['host'],
  user=sql_credentials['user'],
  password=sql_credentials['password'],
  database=sql_credentials['database']
)
mycursor = mydb.cursor()


""" mycursor.execute('SELECT symbol FROM NASDAQ ORDER by RAND() LIMIT 3')

tickers= mycursor.fetchall()
tickerslist=list(tickers) """
tickerslistclean=['mara']
totalchecked=[]
sql = 'INSERT INTO MENTIONS (stockticker, mentions, date) VALUES (%s, %s, %s)'
for x in tickerslistclean:
    comments=api.search_comments(q=x, subredit=subreddit, before=endTime, after=startTime, fields='body')
    length = int(len(comments))
    """ data = PushshiftAPIBase
    print(data) """
    """length = int(data['metadata']['total_results'])
    val = ('%s'%x , '%s'%length, '%s'%startTime)
    mycursor.execute(sql, val)"""
    totalchecked.append(1)
    """mydb.commit()"""
    print( x, length)
    if len(totalchecked) == len(tickerslistclean):
        break 





