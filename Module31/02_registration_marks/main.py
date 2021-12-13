import re
letter = ""
pattern_person = r"\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]\d{3}[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]{2}\d{2,3}"
pattern_taxi = r"\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]{2}\d{5,6}"
text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

print("Список номеров частных автомобилей:", re.findall(pattern_person, text))
print("Список номеров такси:", re.findall(pattern_taxi, text))