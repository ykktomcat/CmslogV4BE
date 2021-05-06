
from django.db.models import Q
#{'inputStr': '哈药', 'inputBegdate': '2020-07-01', 'inputEnddate': '2021-03-18', 'handler': '袁柯柯', 'admin': '00'}
# 1.固定条件的或查询
# >>> User.objects.filter(Q(is_staff=True) | Q(username__contains='123'))
# [<User: staff_a>, <User: 123>, <User: staff_b>]
#
# 2.对于动态可变条件的或查询
# 代码示例：
# >>> di = {'username__contains': '123', 'is_staff': True}  # 条件不固定
# >>> di = {'username': '123', 'age': 18, 'is_staff': True}  # 条件不固定
# >>> q = Q()
# >>> for i in di:
# ...     q.add(Q(**{i: di[i]}), Q.OR)
# ...
# <django.db.models.query_utils.Q object at 0x103a84bd0>
# <django.db.models.query_utils.Q object at 0x103af1110>
# >>> print q
# (OR: (AND: ), (AND: ('username', '123')), ('is_staff', True))
# >>> User.objects.filter(q)
# [<User: staff_a>, <User: 123>, <User: staff_b>]
def query_q(dict):

    enddict1 ={}
    enddict2 ={}
    #dict ={'inputStr': '11', 'inputBegdate': '1', 'inputEnddate': '1', 'handler': '袁柯柯', 'admin': '00'}
    if dict['inputStr'] :
        enddict1['ownername__icontains'] = dict['inputStr']
        enddict1['deptname__icontains'] = dict['inputStr']
        enddict1['event_system__icontains'] = dict['inputStr']
        enddict1['event_mark__icontains'] = dict['inputStr']
        enddict1['resolvent__icontains'] = dict['inputStr']
        enddict1['event_from__icontains'] = dict['inputStr']
        enddict1['proposer__icontains'] = dict['inputStr']
        enddict1['status__icontains'] = dict['inputStr']
        enddict1['mark__icontains'] = dict['inputStr']



    #
    #
    if dict['handler'] :
        enddict2['handler'] = dict['handler']

    if dict['admin'] =='10':
        del enddict2['handler']
    else:
        enddict2['handler'] = dict['handler']

    #
    #
    if dict['inputBegdate']:
        enddict2['createdate__gte'] = dict['inputBegdate']


    if dict['inputEnddate']:
        enddict2['createdate__lte'] = dict['inputEnddate']



    #
    #
    # for keys,values in enddict1.items():
    #     pass
    #     print(keys+':'+values)

    # (OR: ('id', 1), ('id', 2), ('id', 3))
    # (OR: ('status', '在线'))
    # (AND: (OR: ('id', 1), ('id', 2), ('id', 3)), ('status', '在线'))

    # >>> di = {'username': '123', 'age': 18, 'is_staff': True}  # 条件不固定
    # >>> q = Q()
    # >>> for i in di:
    # ...     q.add(Q(**{i: di[i]}), Q.OR)

    con = Q()
    q1 = Q()
    # q1.connector = 'OR'
    for i in enddict1:
        q1.add(Q(**{i: enddict1[i]}), Q.OR)
        # q1.children.append(**{i: enddict1[i]})
    # q.add(Q(**{i: di[i]}), Q.OR)
    print(q1)


    q2 = Q()
    q2.connector = 'AND'
    for i in enddict2:

        q2.children.append({i: enddict2[i]})

    #print(q2)



    con.add(q1, 'AND')
    #print(con)
    con.add(q2, 'AND')

    return  con



# q1 = Q()
# q1.connector = 'OR'
# q1.children.append(('id', 1))
# q1.children.append(('id', 2))
# q1.children.append(('id', 3))
#
#
#
# con = Q()
#
# q1 = Q()
# q1.connector = 'OR'
# q1.children.append(('id', 1))
# q1.children.append(('id', 2))
# q1.children.append(('id', 3))
#
# print(q1)
#
# q2 = Q()
# q2.connector = 'OR'
# q2.children.append(('status', '在线'))
#
# print(q2)
# con.add(q1, 'AND')
# con.add(q2, 'AND')
# print(con)


   # Q(createdate__gte=data['inputBegdate'])  # gte：大于等于某个时间
    #                                                 # lte：小于等于
    #                                                 & Q(createdate__lte=data['inputEnddate']),
    #                                                 Q(id__icontains=data['inputStr'])
    #                                                 | Q(ownername__icontains=data['inputStr'])
    #                                                 | Q(deptname__icontains=data['inputStr'])
    #                                                 | Q(event_system__icontains=data['inputStr'])
    #                                                 | Q(event_mark__icontains=data['inputStr'])
    #                                                 | Q(event_type__icontains=data['inputStr'])
    #                                                 | Q(resolvent__icontains=data['inputStr'])
    #                                                 | Q(event_from__icontains=data['inputStr'])
    #                                                 | Q(handler__icontains=data['inputStr'])
    #                                                 | Q(proposer__icontains=data['inputStr'])
    #                                                 | Q(status__icontains=data['inputStr'])
    #                                                 | Q(mark__icontains=data['inputStr'])).values()