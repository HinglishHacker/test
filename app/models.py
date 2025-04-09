from django.db import models

class TestBox(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.title}"


class Test(models.Model):
    question = models.CharField(max_length=100)
    test_box = models.ForeignKey(TestBox, on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return f"{self.title} by {self.author}"
