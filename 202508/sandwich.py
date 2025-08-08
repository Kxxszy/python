sandwich_orders=['s1','s2','s3','s4']
finished_sandwiches=[]
while sandwich_orders:
    temp=sandwich_orders.pop()
    print(f'i made your {temp}')
    finished_sandwiches.append(temp)
print(f'finished_sandwiches:{finished_sandwiches}')
#aaaaaaaaa