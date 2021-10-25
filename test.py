import pandas as pd

df = pd.read_csv('dc-wikia-data.csv')
#pageId,name,urlslug,id,align,eye,hair,sex,gsm,alive,appearances,firstAppearance,year



#df["year"] = df["year"].fillna(0)
#df["pageId"] = df["pageId"].fillna(0)
#df["appearances"] = df["appearances"].fillna(0)
for column in df.columns:
    df[column] = df[column].fillna(0)

df = df.astype({"pageId":int,"name":str,"urlslug":str,"id":str,"align":str,"eye":str,"hair":str,"sex":str,"gsm":str,"alive":str,"appearances":int,"firstAppearance":str,"year":int})

print(df)

