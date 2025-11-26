routes = ["New A", "New B", "New C", "New D", "New E", "Blue F", "Bypass G", "Express H", "Highway I", "Southern J"]
print("Delivery Routes are:", routes)

routes.append("Avenue")
routes.remove("New B")
print("\n2. After changes:", routes)

routes.sort()
print("\n3a. After sort in alphabetical:", routes)
routes.reverse()
print("3b. Reversed routes:", routes)

n_routes = sum(1 for route in routes if route.startswith("N"))
print("\n4. Rotes starting with 'N':", n_routes)

long_routes = [route for route in routes if len(route)>6]
print("\n5. Rotes longer than 6 chars:", long_routes)