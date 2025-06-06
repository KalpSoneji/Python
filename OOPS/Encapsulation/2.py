class City:

    def printCityName(self, name):
        print("City name = ", name)
        # print("Self City Name = ", self.name)

    def displayCity(self):
        self.cityName = "Ahmedabad"
        print(self.cityName)

ahm = City()
ahm.printCityName("Ahmedabad")

mumbai = City()
mumbai.displayCity()