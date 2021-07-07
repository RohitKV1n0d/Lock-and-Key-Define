import xlrd

from app import db,User
import temp_data


db.create_all()
AdminUsername = 'Admin@user'
AdminPassword = 'Admin@user123'
def admin_status(Astatus):
    status = Astatus
    if status == 1:
        return True
    else:
        return False 
admin_status(0)
    

check_admin = User.query.filter_by(username='Admin@user').first()
if check_admin== None :
    admin_user = User(username=AdminUsername,role='admin', password=AdminPassword,hints=5,penalty='0',email='admin@user.com',unlock='1',
                         r1h1=temp_data.r1_hint1, r1h2=temp_data.r1_hint2, r1h3=temp_data.r1_hint3,
                         r2h1=temp_data.r2_hint1, r2h2=temp_data.r2_hint2, r2h3=temp_data.r2_hint3,
                         r3h1=temp_data.r3_hint1, r3h2=temp_data.r3_hint2, r3h3=temp_data.r3_hint3,
                         r4h1=temp_data.r4_hint1, r4h2=temp_data.r4_hint2, r4h3=temp_data.r4_hint3,
                         r5h1=temp_data.r5_hint1, r5h2=temp_data.r5_hint2, r5h3=temp_data.r5_hint3,
                         r6h1=temp_data.r6_hint1, r6h2=temp_data.r6_hint2, r6h3=temp_data.r6_hint3,
                         r7h1=temp_data.r7_hint1, r7h2=temp_data.r7_hint2, r7h3=temp_data.r7_hint3,
                         r8h1=temp_data.r8_hint1, r8h2=temp_data.r8_hint2, r8h3=temp_data.r8_hint3,
                         r9h1=temp_data.r9_hint1, r9h2=temp_data.r9_hint2, r9h3=temp_data.r9_hint3)              
    db.session.add(admin_user)
    db.session.commit()

admin_user = User(username='kv123',role='player', password='testuser',hints=5,penalty='0', email='test@user.com',
                         r1h1=temp_data.r1_hint1, r1h2=temp_data.r1_hint2, r1h3=temp_data.r1_hint3,
                         r2h1=temp_data.r2_hint1, r2h2=temp_data.r2_hint2, r2h3=temp_data.r2_hint3,
                         r3h1=temp_data.r3_hint1, r3h2=temp_data.r3_hint2, r3h3=temp_data.r3_hint3,
                         r4h1=temp_data.r4_hint1, r4h2=temp_data.r4_hint2, r4h3=temp_data.r4_hint3,
                         r5h1=temp_data.r5_hint1, r5h2=temp_data.r5_hint2, r5h3=temp_data.r5_hint3,
                         r6h1=temp_data.r6_hint1, r6h2=temp_data.r6_hint2, r6h3=temp_data.r6_hint3,
                         r7h1=temp_data.r7_hint1, r7h2=temp_data.r7_hint2, r7h3=temp_data.r7_hint3,
                         r8h1=temp_data.r8_hint1, r8h2=temp_data.r8_hint2, r8h3=temp_data.r8_hint3,
                         r9h1=temp_data.r9_hint1, r9h2=temp_data.r9_hint2, r9h3=temp_data.r9_hint3)              
db.session.add(admin_user)
db.session.commit()




loc = ("event-attendee-list.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)



for i in range(1,202):
    addUser =   User(username=sheet.cell_value(i, 2),role='player',email=sheet.cell_value(i, 3) , password=sheet.cell_value(i, 1),hints=5,penalty='0',booking_id =sheet.cell_value(i, 1),
                         r1h1=temp_data.r1_hint1, r1h2=temp_data.r1_hint2, r1h3=temp_data.r1_hint3,
                         r2h1=temp_data.r2_hint1, r2h2=temp_data.r2_hint2, r2h3=temp_data.r2_hint3,
                         r3h1=temp_data.r3_hint1, r3h2=temp_data.r3_hint2, r3h3=temp_data.r3_hint3,
                         r4h1=temp_data.r4_hint1, r4h2=temp_data.r4_hint2, r4h3=temp_data.r4_hint3,
                         r5h1=temp_data.r5_hint1, r5h2=temp_data.r5_hint2, r5h3=temp_data.r5_hint3,
                         r6h1=temp_data.r6_hint1, r6h2=temp_data.r6_hint2, r6h3=temp_data.r6_hint3,
                         r7h1=temp_data.r7_hint1, r7h2=temp_data.r7_hint2, r7h3=temp_data.r7_hint3,
                         r8h1=temp_data.r8_hint1, r8h2=temp_data.r8_hint2, r8h3=temp_data.r8_hint3,
                         r9h1=temp_data.r9_hint1, r9h2=temp_data.r9_hint2, r9h3=temp_data.r9_hint3)             
    db.session.add(addUser)
    db.session.commit()
    
    


