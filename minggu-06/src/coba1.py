while True:
    try:
        x = int(input("Tolong isi dengan angka : "))
        break
    except ValueError:
        print ("Ooops!, itu bukan angka. coba lagi ...")
