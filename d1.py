import pandas as pd
data={'country':['belgium' ,'india' ,'brazil'],
'capital':['brussesls','new delhi','brasilia'],
'population':[11,123,23]}
df=pd.DataFrame(data,columns=['country','capital','population'])
print(df)