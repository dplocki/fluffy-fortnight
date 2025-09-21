class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rented = set()
        self.movies_shop = defaultdict(list)
        self.movies_price = []

        for shop, movie, price in entries:
            self.movies_shop[movie].append((price, shop))
            self.movies_price.append((price, shop, movie)) 

        for shops in self.movies_shop.values():
            shops.sort()

        self.movies_price.sort()


    def search(self, movie: int) -> List[int]:
        result = []
        count = 0

        for price, shop in self.movies_shop[movie]:
            if count >= 5:
                break

            if (shop, movie) not in self.rented:
                result.append(shop)
                count += 1

        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.remove((shop, movie))

    def report(self) -> List[List[int]]:
        result = []
        count = 0
        
        for price, shop, movie in self.movies_price:
            if count >= 5:
                break
            if (shop, movie) in self.rented:
                result.append((shop, movie))
                count += 1

        return result

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
