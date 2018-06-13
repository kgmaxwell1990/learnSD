from django.db import models

# Create your models here.
class Modules(models.Model):
    name = models.CharField(max_length=256, blank=False, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
    
class Sections(models.Model):
    module = models.ForeignKey(Modules,on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=256, blank=False, default='')
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Lessons(models.Model):
    module = models.ForeignKey(Modules,on_delete=models.CASCADE, related_name='lessons')
    section = models.ForeignKey(Sections,on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=256, blank=False, default='')
    description = models.TextField()
    vid_link = models.CharField(max_length=256, blank=False, default='')
    lesson_number = models.IntegerField(default="1", blank=False)
    free = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return self.name + "-" + str(self.lesson_number)