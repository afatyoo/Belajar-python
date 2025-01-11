import matplotlib.pyplot as plt

def fcfs_with_arrival(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    completion_time = [0] * n
    gantt_chart = []
    times = []

    # Mengurutkan proses berdasarkan arrival time
    sorted_data = sorted(zip(arrival_time, burst_time, processes))
    arrival_time = [x[0] for x in sorted_data]
    burst_time = [x[1] for x in sorted_data]
    processes = [x[2] for x in sorted_data]

    # Hitung Completion Time dan Waiting Time
    time = 0
    for i in range(n):
        if time < arrival_time[i]:
            time = arrival_time[i]  # Tunggu sampai proses tersedia
        gantt_chart.append(processes[i])
        times.append(time)  # Catat waktu mulai proses
        completion_time[i] = time + burst_time[i]
        time += burst_time[i]
        waiting_time[i] = time - arrival_time[i] - burst_time[i]
    times.append(time)

    # Hitung rata-rata waktu tunggu
    avg_waiting_time = sum(waiting_time) / n

    return gantt_chart, times, waiting_time, avg_waiting_time


def plot_gantt_chart(gantt_chart, times):
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_ylim(0, 1)
    ax.set_xlim(0, times[-1])
    ax.set_yticks([])
    ax.set_xticks(times)
    ax.grid(True, axis="x", linestyle="--", alpha=0.6)
    
    start_time = times[0]
    for i, process in enumerate(gantt_chart):
        ax.text((start_time + times[i + 1]) / 2, 0.5, process, ha='center', va='center', color='white')
        ax.barh(0.5, times[i + 1] - start_time, left=start_time, height=0.5, color="skyblue", edgecolor="black")
        start_time = times[i + 1]

    ax.set_title("Gantt Chart - FCFS Scheduling with Arrival Time")
    plt.show()


# Input dari pengguna
num_processes = int(input("Masukkan jumlah proses: "))
processes = []
arrival_time = []
burst_time = []

for i in range(num_processes):
    process = f"P{i + 1}"
    processes.append(process)
    at = int(input(f"Masukkan Arrival Time untuk {process}: "))
    bt = int(input(f"Masukkan Burst Time untuk {process}: "))
    arrival_time.append(at)
    burst_time.append(bt)

# Jalankan Algoritma FCFS
gantt_chart, times, waiting_time, avg_waiting_time = fcfs_with_arrival(processes, arrival_time, burst_time)

# Print Hasil
print("\nHasil FCFS:")
print("Gantt Chart:", gantt_chart)
print("Time Intervals:", times)
print("Waiting Times:")
for i in range(len(processes)):
    print(f"{processes[i]} - Waiting Time: {waiting_time[i]}")
print(f"\nAverage Waiting Time (AWT): {avg_waiting_time:.2f}")

# Plot Gantt Chart
plot_gantt_chart(gantt_chart, times)
