from bitrix24 import Bitrix24

bx24 = Bitrix24('WebHookURL')

                
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
