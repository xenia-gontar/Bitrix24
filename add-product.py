from bitrix24 import Bitrix24

import csv
from datetime import datetime, timedelta
import pandas as pd

bx24 = Bitrix24('urlWebHook')


df = pd.read_excel('text.xlsx', dtype=str)

df.to_csv(f"text.csv", index=False, sep=',')

data = pd.read_csv('text.csv')

print(data.columns)

data_not_null_price = data[data['Price'] != '0']

print(data_not_null_price)

list_of_deals = data_not_null_price["ID"].unique()

for deal in list_of_deals:
    data_prices = data_not_null_price[data_not_null_price["ID"] == deal]
    print(data_prices)
    data_prices = data_prices.reset_index()
    for index, row in data_prices.iterrows():
        bx24.callMethod("crm.deal.update",
            id = deal,
            fields={"UF_CRM_1716210704017": row['Product']})

        bx24.callMethod('bizproc.workflow.start',
            TEMPLATE_ID = 29,
            DOCUMENT_ID = ['crm', 'CCrmDocumentDeal', deal],)
                


                


bx24.callMethod(
    "crm.product.add",
        fields=
        {
            "NAME": "Test",
            "CURRENCY_ID": "RUB", 
            "PRICE": 4900, 
        })

"""             
bx24.callMethod('tasks.task.add',
                fields={'TITLE':'task for test', 'RESPONSIBLE_ID':1})




bx24.callMethod(
    "crm.deal.productrows.set",
        id = 1,
        rows= [{"PRODUCT_ID": 3, "PRICE": 100.00, "QUANTITY": 4}])

print(bx24.callMethod(
    "crm.deal.productrows.get",
    id = 1))
    """

"""
bx24.callMethod(
    "crm.deal.add",
        fields=
        {
            "TITLE": "Плановая продажа",
            "TYPE_ID": "GOODS", 
            "STAGE_ID": "NEW",
            "COMPANY_ID": 3,
            "CONTACT_ID": 3,
            "OPENED": "Y", 
            "ASSIGNED_BY_ID": 1, 
            "PROBABILITY": 30,
            "CURRENCY_ID": "USD", 
            "OPPORTUNITY": 5000,
            "CATEGORY_ID": 5,                  
        }
)        
"""


"""
bx24.callMethod(
    'bizproc.workflow.start',
    TEMPLATE_ID = 29,
    DOCUMENT_ID = ['crm', 'CCrmDocumentDeal', 1],
    PARAMETERS = [{'Price': "300"}]
 )


"""
#print(bx24.callMethod("crm.deal.fields"))

bx24.callMethod(
    "crm.deal.update",
    id = 1,
    fields={"UF_CRM_1716204402693": "500"})


bx24.callMethod(
    'bizproc.workflow.start',
    TEMPLATE_ID = 29,
    DOCUMENT_ID = ['crm', 'CCrmDocumentDeal', 1],
 )

bx24.callMethod(
    "crm.deal.update",
    id = 1,
    fields={"UF_CRM_1716204402693": "300"})


bx24.callMethod(
    'bizproc.workflow.start',
    TEMPLATE_ID = 29,
    DOCUMENT_ID = ['crm', 'CCrmDocumentDeal', 1],
 )
"""
print(bx24.callMethod(
        'bizproc.workflow.template.list',
select = ['ID', 'NAME','PARAMETERS'],
filter = {"ID": 29}))
"""
