class Polygon:
     def __init__ (self, array):
          self.__points = array
          self.__centroid = None
     
     @property
     def centroid(self):
          return self.__centroid

     def teziste(self):
          x_sum =0
          y_sum =0
          pocet = len(self.__points)   #počítá počet bodů
          for item in self.__points:
               pole = item.split(",")
               x = pole[0]             #souřadnice x
               y = pole[1]             #souřadnice x
               x_sum += float(x)       #součty hodnot souřadnic
               y_sum += float(y)

          teziste_x = x_sum/pocet      #vážený průměr
          teziste_y = y_sum/pocet
          self.__centroid = (teziste_x, teziste_y)

try:
     with open ("souradnice.txt", "r", encoding="utf-8") as input,\
          open("teziste.txt", "w", encoding="utf-8") as out: 
          file = input.readlines()
          objekt_1 = Polygon(file)
          objekt_1.teziste()
          out.write(f"Souřadnice těžiště: {objekt_1.centroid[0]}, {objekt_1.centroid[1]}")
          
except FileNotFoundError:
     print("Vstupní soubor neexistuje")
     exit()
except PermissionError:
     print("Program nemá právo číst vstupní soubor")
     exit()
except ValueError:
     print("Vstupní soubor obsahuje jiné znaky než číslice")
     exit()
except IndexError:
     print("Vstupní data nenjsou ve správném formátu")
     exit()
except UnboundLocalError:
     print("Vstupní soubor je prázdný")
     exit()
