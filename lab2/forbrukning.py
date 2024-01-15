km = float(input("Ange körsträcka i km: "))
l = float(input("Ange förbrukat bränsle i liter: "))
lpkm = (100  * l) / (km)
print("Bränsleförbrukningen för bilen är", round(lpkm , 3) , "l/100 km")

#enkla förklaringar till valet av namn till variablerna, svårt att blanda ihop med annat, km, l , lpkm
