import csv

from api.models import User


def ExportData():
    result = []
    data = open('csv/users.csv')
    rows = csv.reader(data)
    for row in rows:
        result.append(row)

    for row in result:
        info = {
            'username':row[0],
            'first_name':row[1],
            'last_name':row[2],
            'email':row[3],
            'is_admin':int(row[4]),
            'is_verify':int(row[5]),
            'password':row[6]
        }
        user= User.objects.create_user(**info)
        print(user)


