from django.db import models

# Create your models here.

class Cms_log(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True, null=False)
    ownername = models.CharField(db_column="ownername",max_length=20)
    deptname = models.CharField(db_column="deptname",max_length=20)
    event_system = models.CharField(db_column="event_system",max_length=20)
    event_mark = models.CharField(db_column="event_mark",max_length=1000)
    event_type = models.CharField(db_column="event_type",max_length=20)
    resolvent = models.CharField(db_column="resolvent",max_length=1000)
    event_from = models.CharField(db_column="event_from",max_length=20)
    handler = models.CharField(db_column="handler",max_length=20)
    proposer = models.CharField(db_column="proposer",max_length=20)
    createdate = models.DateTimeField(db_column="createdate",blank=True, null=True,max_length=20)
    resolventdate = models.DateTimeField(db_column="resolventdate",blank=True, null=True,max_length=20)
    status = models.CharField(db_column="status",max_length=20)
    mark = models.CharField(db_column="mark",max_length=1000)

    # 在默认情况下，生成的表名：App_class, 如果要自定义 ，需要使用Class Meta来自定义
    class Meta:
        managed = True
        db_table = "CMS_LOG_HDR"
        ordering = ['-id']

    # __str__方法
    def __str__(self):
        return "日志id:%s\t描述:%s\t备注:%s" %(self.id,self.event_mark,self.mark)


class Cms_users(models.Model):
    #id = models.IntegerField(db_column="id", primary_key=True, null=False)
    username = models.CharField(db_column="username",primary_key=True, null=False, max_length=20)
    password = models.CharField(db_column="password", max_length=20)
    admin = models.CharField(db_column="admin", max_length=20)

    # 在默认情况下，生成的表名：App_class, 如果要自定义 ，需要使用Class Meta来自定义

    class Meta:
        #managed = True
        db_table = "CMS_USERS"
