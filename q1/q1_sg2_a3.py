birth_year = int(input("Enter your birth year: ")

if birth_year < 1900:
                 print("Invalid Year, it should not be earlier than 1900")

except ValueError:
                 exit()

zodiac_sign = (birth_year - 1900) % 12

if zodiac sign == 0:
  print("Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")

if zodiac_sign == 1:
  print("Your Chinese Zodiac Sign is : Ox (牛 / Niú)")

if zodiac_sign == 2:
  print("Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")

if zodiac_sign == 3:
  print("Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")

if zodiac_sign == 4:
  print("Your Chinese Zodiac Sign is : Dragon (龙 / Lóng)")

if zodiac_sign == 5:
  print("Your Chinese Zodiac Sign is : Snake (蛇 / Shé)")

if zodiac_sign == 6:
  print("Your Chinese Zodiac Sign is : Horse (马 / Mǎ)")

if zodiac_sign == 7:
  print("Your Chinese Zodiac Sign is : Goat (羊 / Yáng)")

if zodiac_sign == 8:
  print("Your Chinese Zodiac Sign is : Monkey (猴 / Hóu)")

if zodiac_sign == 9:
  print("Your Chinese Zodiac Sign is : Rooster (鸡 / Jī)")

if zodiac_sign == 10:
  print("Your Chinese Zodiac Sign is : Dog (狗 / Gǒu)")

if zodiac_sign == 11:
  print("Your Chinese Zodiac Sign is : Pig (猪 / Zhū)")


  
