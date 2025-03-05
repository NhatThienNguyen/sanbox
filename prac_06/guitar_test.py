"""
Estimate time: 20 minutes
Actual time: 40 minutes
"""
from prac_06.guitar import Guitar

guitar = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)
another_guitar = Guitar(name="Gibson L-5 CES", year=2013, cost=16035.40)
print(guitar.get_age()) #Expect 103. Got 103
print(another_guitar.get_age()) #expect 12. Got 12
print(guitar.is_vintage()) #Expect True. Got True
print(another_guitar.is_vintage()) #Expect False. Got False