from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
import csv

def insert_data(self):
    with open('D:\\Django\\venv\\Scripts\\projectcsv\\app\\bank.csv','r') as FO:
        IDO=csv.reader(FO)
        for row in IDO:
            bn=row[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse("data is inserted successfully")


def insert_branch_data(self):
    with open('D:\\Django\\venv\\Scripts\\projectcsv\\app\\branch1.csv','r') as FO:
        IDO=csv.reader(FO)
        next(IDO)
        for row in IDO:
            bn=row[0]

            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifsc=row[1]
                branch=row[2]
                address=row[3]
                contact=row[4]
                city = row[5]
                district =row[6] 
                state = row[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifsc,branch=branch,address=address,contact=contact,city=city,district=district,state=state)
                BRO.save()
    return HttpResponse("data insereted successfully") 

def delete_branch_data(self):
    Branch.objects.all().delete()
    return HttpResponse("Branch data deleted successfully")

