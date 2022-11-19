class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

class Race:
  def __init__(self, name, driver_limit):
    self.name = name
    self.driver_limit = driver_limit
    self.drivers = []

  def add_driver(self, driver):
    if len(self.drivers) < self.driver_limit:
      self.drivers.append(driver)
      return f"Added driver: {driver}"
    return f"Number of drivers exceeded: {self.driver_limit}"

  def get_average_ranking(self):
    if len(self.drivers) > 0:
      sum_rank = 0
      for driver in self.drivers:
        sum_rank += driver.ranking
  
      return sum_rank / len(self.drivers)
    return 0

class Driver:
  number_of_drivers = 0
  def __init__(self, name, age, ranking):
    self.name = name
    self.age = age
    self.ranking = ranking
    Driver.number_of_drivers += 1

  def get_ranking(self):
    return self.ranking

driver_1 = Driver('Lewis Hamilton', 36, 83)
driver_2 = Driver('Eliud Kipchoge', 36, 95)
driver_3 = Driver('Sebastian Vettel', 34, 76)
driver_4 = Driver('Ayrton Senna', 34, 99)
driver_5 = Driver('Dale Earnhardt', 29, 100)

seattle_race = Race('Seattle 500', 4)

seattle_race.add_driver(driver_1)
seattle_race.add_driver(driver_2)
seattle_race.add_driver(driver_3)
seattle_race.add_driver(driver_4)
seattle_race.add_driver(driver_5)

print(seattle_race.get_average_ranking())