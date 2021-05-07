file=open("inventory.txt","a")
while True:
    tanya = input("Input Data Inventory Baru ?(Yes/No) ?")
    if tanya == "Yes" or tanya == "yes":
       newItem = input("Masukkan Nama Perangkat : ")
       newItem2 = input("Masukkan Lokasi : ")
       print('----------------------------------')
    elif tanya == "No" or tanya == "no":
        print("All done!")
        print('----------------------------------')
        break
    if newItem == "exit":
        print("All done!")
        print('----------------------------------')
        break
    file.write("Nama Perangkat : "+ newItem + ",Lokasi : "+newItem2 )
    
file.close()

inventory=[]
file=open("inventory.txt","r")
for item in file:
    item=item.strip()
    inventory.append(item)
file.close()

print(inventory)
