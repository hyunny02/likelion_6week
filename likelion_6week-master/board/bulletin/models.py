from django.db import models
from django.urls import reverse

class Bulletin(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    #게시물 작성되는 시간을 자동으로 설정하도록 함.최초시간 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 게시물이 업데이트될때 마다 시간 다시 저장
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # 본문보여주기 전에 간략하게 보여주기
    def summary(self):
        return self.content[:20]

    def get_absolute_url(self):
        return reverse('bulletin:detail', args=[str(self.id)])

