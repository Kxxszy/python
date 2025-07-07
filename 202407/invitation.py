dinner_invitation=[]
dinner_invitation.append('zjh')
dinner_invitation.append('hwj')
dinner_invitation.append('syc')
invitation=f'Sgt want to invite {dinner_invitation[0].title()} {dinner_invitation[1].title()} {dinner_invitation[2].title()} to come and have dinner together.'
absent=dinner_invitation.pop()
situation=f'{absent.title()} is unable to come because he is travelling'
print(situation)
dinner_invitation.insert(2,'jzy')
dinner_invitation.insert(0,'wly')
dinner_invitation.insert(2,'ywd')
dinner_invitation.append('cxr')
new_invitation=f"{dinner_invitation[0].title()} {dinner_invitation[2].title()} {dinner_invitation[-1].title()},hello you're now invited because we have a big table."
print(new_invitation)
situation="Sorry,but the table's dilvery is delayed."
a=dinner_invitation.pop()
sorry=f"{a.title()},I'm sorry I can't invite you.\n"
print(sorry)
b=dinner_invitation.pop()
sorry=f"{b.title()},I'm sorry I can't invite you.\n"
print(sorry)
c=dinner_invitation.pop()
sorry=f"{c.title()},I'm sorry I can't invite you.\n"
print(sorry)
d=dinner_invitation.pop()
sorry=f"{d.title()},I'm sorry I can't invite you.\n"
print(sorry)
final_invitation=dinner_invitation
message=f"{final_invitation[1].title()} ,{final_invitation[0].title()},welcome to my party"
print(message)
del final_invitation[0]
del final_invitation[0]
print(final_invitation)