from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)

    def __str__(self):
        return f"Answer to {self.question.title} by {self.author.username}"

    def like_count(self):
        return self.likes.count()

    def get_likers(self):
        likers = self.likes.all()
        if likers.count() > 0:
            if likers.count() == 1:
                return f"{likers.first().username} likes this"
            elif likers.count() == 2:
                return f"{likers.first().username} and {likers.last().username} like this"
            elif likers.count() == 3:
                return f"{likers[0].username}, {likers[1].username}, and {likers[2].username} like this"
            else:
                return f"{likers[0].username}, {likers[1].username}, {likers[2].username}, and {likers.count() - 3} others like this"
        return ""

    class Meta:
        ordering = ['-created_at']
