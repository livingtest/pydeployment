import os

import faker



os.environ.setdefault('DJANGO_SETTINGS_MODULE','bestproject.settings')

import django
django.setup()

import random
from firstapp.models import accessrecord,Webpages,Topic,Users
from faker import Faker
fakegen=Faker()



topics=["Family","marriage","sex","relationship","Children","weddings"]
def addtopic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        top=addtopic()


        # create a fake data  for net
        

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        fake_fname=fakegen.first_name()
        fake_lname=fakegen.last_name()
        fake_email=fakegen.email()
 
        # create entry for company


        webpg=Webpages.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        user=Users.objects.get_or_create(firstname=fake_fname,lastname=fake_lname,email=fake_email)[0]



        # create fake access record for that


        acc_rec= accessrecord.objects.get_or_create(name=webpg,date=fake_date)[0]


        
if __name__=='__main__':
    print('populate script')

    populate(25)
    print("COMPLETE")




         










