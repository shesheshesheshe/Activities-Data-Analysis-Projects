def getColumnNames(indexs, db_name):
    '''
    get a string of all indexed column name
    '''
    column_names = pd.read_sql_query("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '"+db_name+"'", conn1)

    if len(indexs)==1:
        return column_names['column_name'][indexs]
    elif index=='all':
        return column_names['column_name']
    else:    
        output = ''
        for index in indexs:
            output = output+column_names['column_name'][index]+','
        return output[:-1]


def iqr_fence(x):
    Q1 = x.quantile(0.25)
    Q3 = x.quantile(0.75)
    IQR = Q3 - Q1
    Lower_Fence = Q1 - (1.5 * IQR)
    Upper_Fence = Q3 + (1.5 * IQR)
    u = max(x[x<Upper_Fence])
    l = min(x[x>Lower_Fence])
    return [u,l]




