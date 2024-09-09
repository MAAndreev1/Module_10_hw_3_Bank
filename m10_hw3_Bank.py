import threading, random, time


class Bank:
    balance = int(0)
    lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_int = random.randint(50, 500)
            self.balance += random_int
            print(f"Пополнение: {random_int}. Баланс: {self.balance}. Lock={self.lock.locked()}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_int = random.randint(50, 500)
            print(f"Запрос на {random_int}")
            if random_int <= self.balance:
                self.balance -= random_int
                print(f"Снятие: {random_int}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств. Lock={self.lock.locked()}")
                self.lock.acquire()


Bank_self = Bank

t1 = threading.Thread(target=Bank_self.deposit, args=(Bank_self,))
t2 = threading.Thread(target=Bank_self.take, args=(Bank_self,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Итоговый баланс: {Bank_self.balance}")
