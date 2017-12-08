User.objects.all()
User.objects.last()

>>> User.objects.create(first_name='Dick', last_name='Dale', email_address='dick@gmail.com', age=69)
<User: User object>
>>> User.objects.create(first_name='Dale', last_name='Dick', email_address='dale@gmail.com', age=69)
<User: User object>
>>> User.objects.create(first_name='Dirk', last_name='Daring', email_address='daring@gmail.com', age=69)
<User: User object>

User.objects.first()
User.objects.all().order_by('-first_name')
<QuerySet [<User: User object>, <User: User object>, <User: User object>]>

>>> b = User.objects.get(id=3)
>>> b.last_name="Davenport"
>>> b.save()

>>> b = User.objects.get(id=4)
>>> b.delete()
(1, {u'users1.User': 1})



