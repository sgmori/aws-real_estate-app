import boto3
import csv

dynamodb = boto3.resource('dynamodb', 'us-west-2')


def batch_writer(table_name, rows):
    table = dynamodb.Table(table_name)
    
    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(Item=row)
    return True
    
    
def read_csv(csv_file, list):
    rows = csv.DictReader(open(csv_file))
    
    for row in rows:
        list.append(row)
        
        
if __name__ == '__main__':
    
    table_name = 'maricopa-sales-data'
    file_name = '/data/MaricopaPropertySales_Jan.csv'
    items = []
    
    read_csv(file_name, items)
    status = batch_writer(table_name, items)
    
    if(status):
        print('Data is saved')
    else:
        print('Error while inserting data')