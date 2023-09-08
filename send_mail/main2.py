
import openpyxl

wb=openpyxl.Workbook()
ws=wb.active

# test_results=Customer.objects.all()

test_results={
    "Ram":40,
    "Raju":50,
}

for k,v in test_results.items():
    ws.append([k,v])
    
wb.save('send_mail/media/new_excel.xlsx')
print("successfully created")
