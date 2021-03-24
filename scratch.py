from database.model import SavedTrip, Park, create_db

create_db()

new_park = Park(park_id= '1234', park_name= 'a park', park_city= 'city', park_state= 'MN', park_description= 'some description', latitude= 12.1234, longitude= 23.3453)
new_park.save()


parks = Park.select()
for p in parks:
    print(p)

# new_trip = SavedTrip(month= 'random month', park= new_park)
# new_trip.save()


# trips = SavedTrip.select()
# for t in trips:
#     print(t)



#json_data = (json.dumps([p.dump() for p in parks]))

