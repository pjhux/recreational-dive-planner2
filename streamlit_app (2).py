
import streamlit as st
from dive_chart import plot_dive_profile_with_pg

# Placeholder dive planner logic - replace these with real calculations
depth1 = 18
time1 = 34
pg_after_first_dive = "M"
surface_interval_minutes = 60
new_pg_after_interval = "G"
depth2 = 15
time2 = 35
pg_after_second_dive = "T"

st.title("Recreational Dive Planner")

st.markdown("### Dive Profile Summary")
st.write(f"**Dive 1:** Depth = {depth1}m, Bottom Time = {time1} min → Pressure Group = {pg_after_first_dive}")
st.write(f"**Surface Interval:** {surface_interval_minutes} minutes → Pressure Group = {new_pg_after_interval}")
st.write(f"**Dive 2:** Depth = {depth2}m, Bottom Time = {time2} min → Pressure Group = {pg_after_second_dive}")

plot_dive_profile_with_pg(
    dive1_time=time1,
    dive1_depth=depth1,
    pg1=pg_after_first_dive,
    surface_interval=surface_interval_minutes,
    pg2=new_pg_after_interval,
    dive2_time=time2,
    dive2_depth=depth2,
    pg_final=pg_after_second_dive
)
