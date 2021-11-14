from UserModels import *


class MessageBoards(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    CourseName = models.CharField(max_length=30)
    Rate = models.CharField(max_length=1, choices=range(1-5), default=3)


class Messages(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    MessageBoard = models.ForeignKey(MessageBoards, on_delete=models.RESTRICT, related_name='%(class)s_Forum')
    Users = models.ForeignKey(Users, on_delete=models.RESTRICT, related_name='%(class)s_author')
    MsgDate = models.DateField()
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='%(class)s_tag')


class MessageTags(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    Message = models.ForeignKey(Messages, on_delete=models.RESTRICT, related_name='%(class)s_tag')
    Users = models.ForeignKey(Users, on_delete=models.RESTRICT, related_name='%(class)s_author')
