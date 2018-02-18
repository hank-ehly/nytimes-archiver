import urllib.request
import pandas as pd
import pandas.io.json.normalize
import json
from sqlalchemy import create_engine
from settings import NYTIMES_ARCHIVE_API_KEY, DB_NAME, DB_TABLE, DB_PORT, DB_USER, DB_PASS, DB_HOST

OUT_PATH = '2018_1.csv'


def fetch_archive_data():
    dl_url = 'https://api.nytimes.com/svc/archive/v1/2018/1.json?api-key=%s' % NYTIMES_ARCHIVE_API_KEY

    raw_response = urllib.request.urlopen(dl_url)
    dict_response = json.loads(raw_response.read().decode('UTF8'))

    doc_list = dict_response['response']['docs']
    keep_columns = ['_id', 'byline.person', 'document_type', 'headline.main', 'pub_date', 'web_url', 'word_count']

    return pd.io.json.json_normalize(doc_list)[keep_columns]


if __name__ == '__main__':
    connection = create_engine('mysql+mysqldb://%s:%s@%s:%i/%s' % (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME))

    df = fetch_archive_data()
    df.to_sql(name=DB_TABLE, con=connection)
