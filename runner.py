#from models import Factors
from re import A
from loader import Loader
from activity import Activty
from models import Exercises

loader = Loader()
activity = Activty()
#exercise = Exercises()

print(loader.load_factors())
#print(loader.load_exercises())
#print(loader.load_categories())

#for exercise in activity.search_exercises('up'):
#    print(exercise)

#print(activity.parse_cadence('2x(5,3,2)+2x(1,3)'))
#results = activity.get_categories()
#activities = {}
#for item in results:
#    activities[item.id] = item.category_name
#
#print(activities)
