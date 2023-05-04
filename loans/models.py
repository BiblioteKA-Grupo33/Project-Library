from django.db import models


class Loans(models.Model):
    borrowed_date  = models.DateTimeField(null=True)
    devolution_date  = models.DateTimeField(null=True)
    is_devoluted = models.BooleanField(null=True, default=False)

    copy = models.ForeignKey(
        "copys.Copy",
        on_delete=models.CASCADE,
        related_name="loans_copys",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans_users",
    )

    def __repr__(self) -> str:
        return f"<Loans {self.id}>"
