import pandas as pd
from io import StringIO
from datetime import datetime

def process_html_content(html_content):
    
    html_file_like = StringIO(html_content)

    df = pd.read_html(html_file_like)[0]

    # df.columns = ['_'.join(col).strip() for col in df.columns.values]

    # Reset the index of the DataFrame
    df1 = df.reset_index()

    # Drop the first column of the DataFrame
    df_dropped = df1.drop(df1.columns[0], axis=1)

    df_dropped = df_dropped.applymap(lambda x: x.replace('Value', '') if isinstance(x, str) else x)

    df_dropped['Bank'] = 'NDB'
    df_dropped['Date'] = datetime.now().strftime('%Y-%m-%d') # today's date 
    df_dropped['Time'] = datetime.now().strftime('%H:%M:%S') # today's time
    df_dropped['ST BANK CODE'] = '7214'

    return df_dropped
