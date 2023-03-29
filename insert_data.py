import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

company_list = []
with open ("DATA/company.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        company_list.append(tuple([int(item[0]), item[1]]))
# print(company_list) # [(1, 'ASUS'), (2, 'ACER'), (3, 'AGB'), (4, 'IBALL'), (5, 'HP')]


cursor.executemany("INSERT INTO Company (id, company) VALUES(?,?);", company_list)
conn.commit()

cursor.close()
conn.close()