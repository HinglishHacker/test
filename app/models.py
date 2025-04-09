from django.db import models


class TestBox(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class Test(models.Model):
    ANSWER_CHOICES = [
        ("FI", "First Choice"),
        ("SE", "Second Choice"),
        ("TH", "Third Choice"),
        ("FO", "Fourth Choice"),
    ]

    test_box = models.ForeignKey(
        TestBox, on_delete=models.CASCADE, related_name="tests"
    )
    question = models.CharField(max_length=255)

    first = models.CharField(max_length=100)
    second = models.CharField(max_length=100)
    third = models.CharField(max_length=100)
    fourth = models.CharField(max_length=100)

    correct_answer = models.CharField(max_length=2, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.question

    def get_correct_text(self):
        return self[self.correct_answer]
