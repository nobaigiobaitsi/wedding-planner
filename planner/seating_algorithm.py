from planner.models import Guest, Relationship

# Ok, so here we take the guest prefferably as an array of objects, and then we
# take the relationships as an array of objects, and then we return the seating.
# We have to declare first the maximum table seating, and then the number of tables.
# The algorithm will then try to seat the guests in a way that maximizes the
# number of positive relationships and minimizes the number of negative relationships.
# It should return an array of tables, where each table is an array of guests.

# Pull data from Models (DB) -> Apply the rules -> Return the seating arrangement

max_table_seating = 10  # Maximum number of guests per table
number_of_tables = 22  # Number of tables to be arranged
guests = list(Guest.objects.all())
relationships = list(Relationship.objects.all())

relationship_map = {}

for r in relationships:
    score = 1 if r.relationship == "positive" else -1
    relationship_map.setdefault(r.from_guest.id, {})[r.to_guest.id] = score
    relationship_map.setdefault(r.to_guest.id, {})[r.from_guest.id] = score
