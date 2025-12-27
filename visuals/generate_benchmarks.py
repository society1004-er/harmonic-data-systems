# generate_benchmarks.py
import matplotlib.pyplot as plt

def create_hds_performance_chart():
    """
    Generates a comparison chart showing HDS efficiency.
    Targets: 38.5% Occupancy vs 85.0% Standard.
    """
    labels = ['Standard AI', 'HDS Architecture']
    occupancy = [85.0, 38.5]
    speed_factor = [1.0, 2.4]

    fig, ax1 = plt.subplots()

    # Bar chart for Occupancy (Lower is better)
    ax1.set_xlabel('Architecture Type')
    ax1.set_ylabel('System Occupancy (%)', color='tab:blue')
    ax1.bar(labels, occupancy, color=['#d3d3d3', '#4CAF50'], alpha=0.6, label='Occupancy')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Line chart for Speed Factor (Higher is better)
    ax2 = ax1.twinx()
    ax2.set_ylabel('Acceleration Factor (x)', color='tab:red')
    ax2.plot(labels, speed_factor, color='tab:red', marker='o', linewidth=3, label='Speed')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title('HDS Efficiency Benchmark: The Power of Emptiness')
    plt.tight_layout()
    plt.savefig('hds_performance_chart.png') # This image goes to assets/
    print("Benchmark chart generated successfully.")

if __name__ == "__main__":
    create_hds_performance_chart()
