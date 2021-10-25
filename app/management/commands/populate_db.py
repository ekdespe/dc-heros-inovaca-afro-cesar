import pandas as pd
from django.core.management.base import BaseCommand
from app.models import DcHero



class Command(BaseCommand):
    help = "Load DCHeros to database from csv file"


    def handle(self,*args,**kwargs):
        if DcHero.objects.exists():
            print("The table has alredy been imported")
        else:
             df = pd.read_csv('dc-wikia-data.csv')
             for column in df.columns:
                df[column] = df[column].fillna(0)

             df = df.astype({"pageId":int,"name":str,"urlslug":str,"identity":str,"align":str,"eye":str,"hair":str,"sex":str,"gsm":str,"alive":str,"appearances":int,"firstAppearance":str,"year":int})
             data =   df.to_dict('records')
             #print(data)
             objs =   DcHero.objects.bulk_create([DcHero(**item) for item in data])

             print(f"{len(objs)} DC heros inserteds") 