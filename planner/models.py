from django.db import models


# These models represent the guests and their relationships. We make the guest model and
# then with the relationship model we can create relationships between guests.
# The relationship model has a foreign key to the guest model, which allows us to create
# relationships between guests.


class Guest(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Relationship(models.Model):
    RELATIONSHIP_TYPES = [
        ("like", "Like"),
        ("dislike", "Dislike"),
    ]

    from_guest = models.ForeignKey(
        Guest, related_name="relationships_from", on_delete=models.CASCADE
    )
    to_guest = models.ForeignKey(
        Guest, related_name="relationships_to", on_delete=models.CASCADE
    )
    relationship_type = models.CharField(max_length=10, choices=RELATIONSHIP_TYPES)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("from_guest", "to_guest")  # This is for duplicates.

    def __str__(self):
        return f"{self.from_guest} {self.relationship_type}s {self.to_guest}"
