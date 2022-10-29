from django.db import models
from django.utils import timezone

class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    def images(self):
        return TopicImage.objects.filter(topic=self.id).order_by("dt")   #上から順に 123456

    def __str__(self):
        return self.comment


class TopicImage(models.Model):
    
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    topic       = models.ForeignKey(Topic,verbose_name="トピック",on_delete=models.CASCADE)
    image       = models.ImageField(verbose_name="画像",upload_to="testapp/topic_image/comment")

    def __str__(self):
        return self.topic.comment