# Mendefiniskan function dengan nama convertKelvinToCelcius dengan parameter suhu
def convertKelvinToCelcius(suhu):
    # Lakukan perhitungan dari kelvin ke celcius setelah itu hasilnya akan direturn
    return suhu - 273

# Mendefiniskan function dengan nama convertCelciusToKelvin dengan parameter suhu
def convertCelciusToKelvin(suhu):
    # Lakukan perhitungan dari celcius ke kelvin setelah itu hasilnya akan direturn
    return 273 + suhu

# Mendefiniskan function dengan nama convertToFahrenheit dengan parameter jenisSuhu dan suhu
def convertToFahrenheit(jenisSuhu,suhu):
    # Cek apakah jenisSuhu adalah Celcius
    if jenisSuhu == 'Celcius' : 
        # Lakukan perhitungan dari Celcius ke Fahrenheit setelah itu hasilnya akan direturn
        return(f'{(suhu * 1.8) + 32} Celcius')
    # Cek apakah jenisSuhu adalah Kelvin
    elif jenisSuhu == 'Kelvin' : 
        # Lakukan perhitungan dari Celcius ke Kelvin setelah itu hasilnya akan direturn
        return(f'{1.8 * (suhu - 273) + 32} Kelvin')
    # Cek apakah jenisSuhu bukan Celcius atau Kelvin
    else :
        # Return pesan jenis suhu tidak sesuai jika jenisSuhu bukan Celcius atau Kelvin
        return "Jenis suhu tidak sesuai"

# Mendefiniskan function dengan nama convertFromFahrenheit dengan parameter jenisSuhu dan suhu
def convertFromFahrenheit(jenisSuhu,suhu):
    # Cek apakah jenisSuhu adalah Celcius
    if jenisSuhu == 'Celcius' : 
        # Lakukan perhitungan dari Fahrenheit ke Celcius setelah itu hasilnya akan direturn
        return(f'{(suhu - 32) / 1.8} Celcius')
    # Cek apakah jenisSuhu adalah Kelvin
    elif jenisSuhu == 'Kelvin' : 
        # Lakukan perhitungan dari Fahrenheit ke Kelvin setelah itu hasilnya akan direturn
        return(f'{1.8 * (suhu - 273) + 32} Kelvin')
    # Cek apakah jenisSuhu bukan Celcius atau Kelvin
    else :
        # Return pesan jenis suhu tidak sesuai jika jenisSuhu bukan Celcius atau Kelvin
        return "Jenis suhu tidak sesuai"

# Mencetak hasil return dari fungsi converKelvinToCelcius dengan nilai parameter suhu 274
print(convertKelvinToCelcius(274))
# Mencetak hasil return dari fungsi converCelciusToKelvin dengan nilai parameter suhu 274
print(convertCelciusToKelvin(1))
# Mencetak hasil return dari fungsi convertToFahrenheit dengan paramter jenisSuhu Celcius dan nilai parameter suhu 274
print(convertToFahrenheit('Celcius',274))
# Mencetak hasil return dari fungsi convertToFahrenheit dengan paramter jenisSuhu Kelvin dan nilai parameter suhu 274
print(convertToFahrenheit('Kelvin',274))
# Mencetak hasil return dari fungsi convertToFahrenheit dengan paramter jenisSuhu Ice dan nilai parameter suhu 274
print(convertToFahrenheit('Ice',274))
# Mencetak hasil return dari fungsi convertFromFahrenheit dengan paramter jenisSuhu Celcius dan nilai parameter suhu 274
print(convertFromFahrenheit('Celcius',274))
# Mencetak hasil return dari fungsi convertFromFahrenheit dengan paramter jenisSuhu Kelvin dan nilai parameter suhu 274
print(convertFromFahrenheit('Kelvin',274))
# Mencetak hasil return dari fungsi convertFromFahrenheit dengan paramter jenisSuhu Ice dan nilai parameter suhu 274
print(convertFromFahrenheit('Ice',274))