from cryptography.fernet import Fernet as fernet
import json
import os
import datetime

def enkrip(text):
    return keyuser.encrypt(text.encode()).decode()

def dekrip(text):
    return keyuser.decrypt(text.encode()).decode()

def inputcheck(prompt, min=-1, max=100):
	while True:
		try:
			userfunc = int(input(prompt))
			if userfunc not in range(min,max):
				print("input melebihi atau kurang dari yang diharapkan")
			else:
				return userfunc
		except ValueError:
			print("hanya masukan angka")

def tabledata(index):
	print(
		f"[{index}]", dekrip(data["teks"][index]["label"]),
		"\n\tusername :", dekrip(data["teks"][index]["username"]),
		"\n\tpassword :", dekrip(data["teks"][index]["password"]),
		"\n\tcreated  :", dekrip(data["teks"][index]["created"]), "\n"
	)

def liatdata(berhenti=None):
	print("\n","=" * 8, "password", "=" * 8)
	for i in range(0, len(data["teks"])):
		if berhenti is None:
			tabledata(i)
		else:
			if berhenti == i:
				tabledata(i)
				break
	print("=" * 8, "selesai", "=" * 8)

if os.path.exists("cryp.json"):
	with open("cryp.json", "r") as f:
		data = json.load(f)
		print("data berhasil di load")
else:
	data = {"tesvalid": "", "teks": []}
	key = fernet.generate_key()
	f = fernet(key)

	print("ini key anda:", key.decode())
	print("#" * 3, "simpen baik-baik kalo g, data kamu ilang selamanya", "#" * 3)
	enkrip_awal = f.encrypt(b"ini valid")
	utf_nkrip_awal = enkrip_awal.decode('utf-8')
	data["tesvalid"] = utf_nkrip_awal

print("=" * 8, "login", "=" * 8)
while True:
	try:
		user = input("masukan key anda: ")
		keyuser = fernet(bytes(user, "utf-8"))

		if dekrip(data["tesvalid"]) == b"ini valid":
			print("login berhasil")
			break
		else:
			break
	except Exception:
		print("password salah")


while True:
	while True:
		print("\n","=" * 8, "menu", "=" * 8)
		print(" 1. lihat password\n 2. hapus data\n 3. ubah data\n 4. tambah password\n 5. keluar")
		print("=" * 25)

		user = inputcheck("masukan pilihan anda: ",1 ,6)
		break

	if user in range(1,4):
		if not data["teks"]:
			print("#" * 3,"anda belum memasukan data sama sekali", "#" * 3)

		else:

			liatdata()

			if user == 2:
				while True:
					user_hapus = inputcheck("pilih sesuai index:")
					if user_hapus > len(data["teks"]) - 1:
						print("index melebihi batas")
					else:
						data["teks"].pop(user_hapus)
						break

			elif user == 3:
				while True:
					try:
						user_ganti = inputcheck("pilih sesuai index: ")
						if user_ganti > len(data["teks"]) - 1:
							print("index melebihi batas")
						else:
							break
					except ValueError:
						print("tolong hanya masukan angka")

				liatdata(user_ganti)
				print("\n","=" * 8, "ubah data", "=" * 8)

				while True:
					print("\n1.label \n2.username \n3.password")

					user_pilih = inputcheck("masukan input sesuai table: ", 1, 4)
					print("=" * 20)
					break

				lookup = {1: "label", 2: "username", 3: "password"}
				user_ubah = input(f"masukan data ({lookup.get(user_pilih)}) yang baru pada index no {user_ganti}: ")

				data["teks"][int(user_ganti)][lookup.get(user_pilih)] = enkrip(user_ubah)

	if user == 4:
		print("\n","=" * 10, "tambah password", "=" * 10)
		user_label = input("masukan nama aplikasi/web: ").upper()
		user_nama = input("masukan username anda: ")
		user_pass = input("masukan password yang ingin disimpan: ")

		tanggal = datetime.datetime.now()
		format_tanggal = f"{tanggal.strftime('%d')} {tanggal.strftime('%B')} {tanggal.strftime('%Y')}"

		data["teks"].append({
			"username" : enkrip(user_nama), 
			"label"    : enkrip(user_label), 
			"password" : enkrip(user_pass),
			"created"  : enkrip(format_tanggal),
		})
		print("password berhasil di simpan")
		print(data)

	if user == 5:
		print("dadahhh")
		break

with open('cryp.json', 'w') as f:
    f.write(json.dumps(data))
