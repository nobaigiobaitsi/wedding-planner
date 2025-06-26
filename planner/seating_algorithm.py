import Guest
import Relationship

# Ok, so here we take the guest prefferably as an array of objects, and then we
# take the relationships as an array of objects, and then we return the seating.
# We have to declare first the maximum table seating, and then the number of tables.
# The algorithm will then try to seat the guests in a way that maximizes the
# number of positive relationships and minimizes the number of negative relationships.
# It should return an array of tables, where each table is an array of guests.

# Pull data from Models (DB) -> Apply the rules -> Return the seating arrangement

max_table_seating = 10  # Maximum number of guests per table
number_of_tables = 22  # Number of tables to be arranged

field = Guest._meta.get_field("name", "group")
for field in field:
    print(field.name)


relate = Relationship._meta.get_field("from_guest", "to_guest")
for relate in relate:
    print(relate.name, relate.relationship_type)
