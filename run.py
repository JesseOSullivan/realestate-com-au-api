from realestate_com_au import RealestateComAu

api = RealestateComAu()

# Get property listings
listings = api.search(locations=["41/7 Juliet Road, Coolbellup, WA 6163"])
