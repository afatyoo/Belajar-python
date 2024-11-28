import matplotlib.pyplot as plt

def round_robin_with_details(processes, burst_time, quantum):
    n = len(processes)
    remaining_time = burst_time[:]
    time = 0
    gantt_chart = []
    times = []
    waiting_time = [0] * n
    completion_time = [0] * n

    # Proses Round Robin
    while any(rt > 0 for rt in remaining_time):
        for i in range(n):
            if remaining_time[i] > 0:
                gantt_chart.append(processes[i])
                times.append(time)
                if remaining_time[i] > quantum:
                    time += quantum
                    remaining_time[i] -= quantum
                else:
                    time += remaining_time[i]
                    completion_time[i] = time
                    remaining_time[i] = 0
    times.append(time)

    # Hitung Turnaround Time dan Waiting Time
    turnaround_time = [completion_time[i] for i in range(n)]
    waiting_time = [turnaround_time[i] - burst_time[i] for i in range(n)]

    # Rata-rata waktu tunggu
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

    ax.set_title("Gantt Chart - Round Robin Scheduling")
    plt.show()


# Input
num_processes = int(input(" Masukan Jumlah proses: "))
processes = [f" p{i+1}" for i in range(num_processes)]
burst_time = []

for i in range(num_processes):
    bt = int(input(f" Masukan burst time untuk {processes[i]}: "))
    burst_time.append(bt)


quantum = int(input("Masukan Quantum Time: "))

# Jalankan Algoritma Round Robin
gantt_chart, times, waiting_time, avg_waiting_time = round_robin_with_details(processes, burst_time, quantum)

# Print Hasil
print("Gantt Chart:", gantt_chart)
print("Time Intervals:", times)
print("Waiting Times:")
for i in range(len(processes)):
    print(f"{processes[i]}: {waiting_time[i]}")
print(f"Average Waiting Time (AWT): {avg_waiting_time:.2f}")

# Plot Gantt Chart
plot_gantt_chart(gantt_chart, times)
