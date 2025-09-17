class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_names = foods
        self.foods = { food:index for index, food in enumerate(foods) }
        self.cuisines = {}
        for index, cuisine in enumerate(cuisines):
            collection = self.cuisines.get(cuisine, [])
            collection.append(index)
            self.cuisines[cuisine] = collection

        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[self.foods[food]] = newRating

    def highestRated(self, cuisine: str) -> str:
        result_value = 0
        result_name = None

        for index in self.cuisines[cuisine]:
            food = self.food_names[index]
            if self.ratings[index] > result_value:
                result_value = self.ratings[index]
                result_name = food
            elif self.ratings[index] == result_value and food < result_name:
                result_value = self.ratings[index]
                result_name = food

        return result_name

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
