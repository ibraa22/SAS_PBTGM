from datetime import datetime, timedelta

class Habit:
    def __init__(self, name):
        self.name = name
        self.log = []
    
    def mark_done(self, date=None):
        date = date or datetime.now().date()
        if date not in self.log:
            self.log.append(date)
            return f"Kebiasaan '{self.name}' berhasil ditandai untuk {date}."
        return f"Kebiasaan '{self.name}' sudah ditandai untuk {date}."
    
    def get_weekly_progress(self):
        today = datetime.now().date()
        one_week_ago = today - timedelta(days=7)
        return [date for date in self.log if one_week_ago <= date <= today]

class HabitTracker:
    def __init__(self):
        self.habits = []
    
    def add_habit(self, habit_name):
        if any(habit.name == habit_name for habit in self.habits):
            return f"Kebiasaan '{habit_name}' sudah ada."
        habit = Habit(habit_name)
        self.habits.append(habit)
        return f"Kebiasaan '{habit_name}' berhasil ditambahkan."
    
    def mark_habit_done(self, habit_name, date=None):
        for habit in self.habits:
            if habit.name == habit_name:
                return habit.mark_done(date)
        return f"Kebiasaan '{habit_name}' tidak ditemukan."
    
    def show_weekly_report(self):
        report = "\nLaporan Mingguan:\n"
        today = datetime.now().date()
        if not self.habits:
            return "Belum ada kebiasaan yang ditambahkan."
        
        for habit in self.habits:
            weekly_log = habit.get_weekly_progress()
            done_days = len(weekly_log)
            report += f"- {habit.name}: {done_days} hari dari 7 hari terakhir.\n"
            for date in weekly_log:
                report += f"  ✔ {date}\n"
        return report


def main():
    tracker = HabitTracker()
    
    while True:
        print("\nAplikasi Manajemen Kebiasaan")
        print("1. Tambahkan kebiasaan baru")
        print("2. Tandai kebiasaan selesai")
        print("3. Tampilkan laporan mingguan")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1-4): ").strip()
        
        if choice == "1":
            habit_name = input("Masukkan nama kebiasaan: ").strip()
            print(tracker.add_habit(habit_name))
        
        elif choice == "2":
            habit_name = input("Masukkan nama kebiasaan: ").strip()
            date_input = input("Masukkan tanggal (YYYY-MM-DD) atau kosong untuk hari ini: ").strip()
            date = None
            if date_input:
                try:
                    date = datetime.strptime(date_input, "%Y-%m-%d").date()
                except ValueError:
                    print("Format tanggal salah. Harap gunakan format YYYY-MM-DD.")
                    continue
            print(tracker.mark_habit_done(habit_name, date))
        
        elif choice == "3":
            print(tracker.show_weekly_report())
        
        elif choice == "4":
            print("Terima kasih telah menggunakan Aplikasi Manajemen Kebiasaan!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
