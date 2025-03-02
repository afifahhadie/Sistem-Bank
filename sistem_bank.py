class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Berhasil menambahkan Rp{amount:.2f}. Saldo saat ini: Rp{self.balance:.2f}")
        else:
            print("Jumlah deposit harus lebih dari 0!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Berhasil menarik Rp{amount:.2f}. Saldo saat ini: Rp{self.balance:.2f}")
        elif amount > self.balance:
            print("Saldo tidak cukup!")
        else:
            print("Jumlah penarikan harus lebih dari 0!")
    
    def check_balance(self):
        print(f"Saldo saat ini: Rp{self.balance:.2f}")

# Contoh penggunaan
if __name__ == "__main__":
    name = input("Masukkan nama pemilik akun: ")
    account = BankAccount(name)
    
    while True:
        print("\nMenu:")
        print("1. Cek Saldo")
        print("2. Deposit")
        print("3. Tarik Uang")
        print("4. Keluar")
        
        choice = input("Pilih menu (1-4): ")
        
        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Masukkan jumlah deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Masukkan jumlah penarikan: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Terima kasih telah menggunakan layanan bank!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
