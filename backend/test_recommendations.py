from app.models.recomendations import RecommendationsEngine
from app.schemas.currect_preferences import CurrentPreferences, Activities
from app.schemas.global_preferences import GlobalPreferenceSimple
from app.schemas.journey import Journey

global_pref = GlobalPreferenceSimple(
    food=["Кафе", "Фастфуд"],
    walk=["Парк"],
    foodStyle=["Европейская кухня"],
    fun=["Бар"],
    style=["Шумный"]
)

curr_pref = CurrentPreferences(
    point={"lat": 54.97763635724782, "lon": 82.89782317789228},
    averageCheck=1500,
    totalTime=120,
    wayType='Пешком',
    activities=[Activities.food, Activities.fun],
    wantSomethingNew=False
)

engine = RecommendationsEngine(global_pref, curr_pref)

journey: Journey = engine.generateJourney()

print("Generated Journey:")
for place in journey.places:
    print(f"Place Type: {place.type}, Name: {place.name}, Address: {place.address}, Rating: {place.rating}, Coordinates: {place.point}")