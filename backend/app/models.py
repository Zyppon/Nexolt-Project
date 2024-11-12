from django.db import models
from django.contrib.auth.models import User  # Dacă vrei să asociezi un utilizator cu mesajul

class Message(models.Model):
    content = models.TextField()  # Textul mesajului
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilizatorul care trimite mesajul
    created_at = models.DateTimeField(auto_now_add=True)  # Data și ora creării mesajului

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}..."  # Reprezentare scurtă a mesajului
