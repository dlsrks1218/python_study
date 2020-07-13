from typing import List, Any

class Country:
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area
    
    def population_density(self) -> float:
        return self.population / self.area
    
    def __repr__(self):
        return "{}('{}', {}, {})".format(self.name, self.name, self.population, self.area)

class Continent():
    def __init__(self,  name: str, countries: List[Country]):
        self.name = name
        self.countries = countries

    def print(self):
        print(self.name)
        for country in self.countries:
            print('{} has a population of ~~~~')


if __name__ == '__main__':
    canada = Country('Canada', 34482779, 9984760)
    # print(canada.population_density())
    # print(canada.__repr__())
    
    usa = Country('United States of America', 313914040, 9826675)
    mexico = Country('Mexico', 112336538, 1943950)

    countries = [canada, usa, mexico]

    north_america = Continent('North America', countries)
    print(north_america.name)

    for country in north_america.countries:
        print(country)