class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine = { food:cuisines[index] for index, food in enumerate(foods) }
        self.food_rating = {food: ratings[index] for index, food in enumerate(foods)}
        self.cuisines = { cuisine: [] for cuisine in set(cuisines) }

        for index, rate in enumerate(ratings):
            self.changeRating(foods[index], rate)

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        heappush(self.cuisines[self.food_cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisines[cuisine]:
            rating, food = self.cuisines[cuisine][0]
            current_rating = -self.food_rating[food]
            
            if rating == current_rating:
                return food
            
            heappop(self.cuisines[cuisine])

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
