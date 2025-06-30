
import streamlit as st
import matplotlib.pyplot as plt

def plot_dive_profile_with_pg(dive1_time, dive1_depth, pg1, surface_interval, pg2, dive2_time, dive2_depth, pg_final):
    # Time positions
    t1 = 1
    t2 = t1 + dive1_time
    t3 = t2 + 1
    t4 = t3 + surface_interval
    t5 = t4 + 1
    t6 = t5 + dive2_time
    t7 = t6 + 1

    x = [0, t1, t2, t3, t4, t5, t6, t7]
    y = [0, dive1_depth, dive1_depth, 0, 0, dive2_depth, dive2_depth, 0]

    # Seabed polygon coordinates
    seabed_upper_x = [t1, t2, t4, t5, t6]
    seabed_upper_y = [dive1_depth, dive1_depth,
                      dive1_depth + (dive2_depth - dive1_depth) * (t4 - t2) / (t5 - t2),
                      dive2_depth, dive2_depth]
    seabed_lower_y = [max(dive1_depth, dive2_depth) + 20] * len(seabed_upper_x)

    seabed_poly_x = seabed_upper_x + seabed_upper_x[::-1]
    seabed_poly_y = seabed_upper_y + seabed_lower_y[::-1]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.axhspan(0, -5, facecolor='skyblue', alpha=0.5, zorder=0)
    ax.axhspan(-5, max(dive1_depth, dive2_depth) + 25, facecolor='midnightblue', alpha=0.6, zorder=0)

    ax.plot(x, y, marker='o', color='red', linewidth=2, label="Dive Path")
    ax.fill(seabed_poly_x, seabed_poly_y, facecolor='wheat', alpha=0.6)

    ax.annotate(f"PG: {pg1}", xy=(t2, 0), xytext=(t2, 2), ha='center',
                arrowprops=dict(arrowstyle="->", color='black'), fontsize=10, color='black')
    ax.annotate(f"PG: {pg2}", xy=(t4, 0), xytext=(t4, 2), ha='center',
                arrowprops=dict(arrowstyle="->", color='black'), fontsize=10, color='black')
    ax.annotate(f"PG: {pg_final}", xy=(t6, 0), xytext=(t6, 2), ha='center',
                arrowprops=dict(arrowstyle="->", color='black'), fontsize=10, color='black')

    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Depth (m)")
    ax.set_title("Dive Profile Chart")
    ax.invert_yaxis()
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

# === Streamlit UI and example ===

st.title("Recreational Dive Profile Chart Demo")

# Example values (replace with real logic or inputs)
dive1_time = 34
dive1_depth = 18
pg1 = "M"

surface_interval = 60
pg2 = "G"

dive2_time = 35
dive2_depth = 15
pg_final = "T"

plot_dive_profile_with_pg(dive1_time, dive1_depth, pg1, surface_interval, pg2, dive2_time, dive2_depth, pg_final)

