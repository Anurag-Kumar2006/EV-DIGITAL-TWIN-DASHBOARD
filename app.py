import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    
    page_title="EV Digital Twin Dashboard",
    page_icon="🚗",
    layout="wide"
)
st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(
        135deg,
        #0F172A,
        #111827,
        #1E293B
    );
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background:#1E293B;
    padding:18px;
    border-radius:18px;
    border:1px solid #334155;
    box-shadow:0px 4px 15px rgba(0,0,0,0.35);
}

/* Metric Labels */
div[data-testid="stMetricLabel"]{
    color:#CBD5E1 !important;
}

/* Metric Values */
div[data-testid="stMetricValue"]{
    color:#22C55E !important;
    font-weight:bold;
}

/* Headers */
h1{
    color:#38BDF8 !important;
}

h2,h3{
    color:#F8FAFC !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

/* Buttons */
.stButton button{
    border-radius:12px;
    background:#2563EB;
    color:white;
    border:none;
}

/* Success Box */
div[data-testid="stAlert"]{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;color:#1565C0;'>
🚗 Tata Nexon EV Digital Twin Platform
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style='text-align:center;color:#1565C0;'>
</h1>
""", unsafe_allow_html=True)
st.image(
"https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tata_Nexon_EV.jpg/640px-Tata_Nexon_EV.jpg",
use_container_width=True
)

# ==========================================
# SIDEBAR
# ==========================================

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "My EV",
        "Analytics",
        "Battery Intelligence",
        "AI Center",
        "Sustainability",
        "Maintenance",
        "Reports"
    ]
)

# ==========================================
# DEFAULT DATA
# ==========================================

VEHICLE_NAME = "Tata Nexon EV"

SOC = 92
SOH = 96
VOLTAGE = 398
TEMPERATURE = 31

RANGE_LEFT = 287
BATTERY_CAPACITY = "40 kWh"

DISTANCE = 25000

# ==========================================
# DASHBOARD
# ==========================================

if menu == "Dashboard":

    st.title("🚗 EV Digital Twin Dashboard")

    st.subheader(VEHICLE_NAME)

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🔋 Battery",
        f"{SOC}%"
    )

    c2.metric(
        "❤️ Battery Health",
        f"{SOH}%"
    )

    c3.metric(
        "⚡ Voltage",
        f"{VOLTAGE} V"
    )

    c4.metric(
        "🌡 Temperature",
        f"{TEMPERATURE} °C"
    )

    st.markdown("---")

    c5, c6, c7, c8 = st.columns(4)

    c5.metric(
        "🚗 Range Left",
        f"{RANGE_LEFT} km"
    )

    c6.metric(
        "🔋 Capacity",
        BATTERY_CAPACITY
    )

    c7.metric(
        "🛣 Distance",
        f"{DISTANCE:,} km"
    )

    c8.metric(
        "⭐ Vehicle Score",
        "95/100"
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=SOH,
            title={"text": "Battery Health"},
            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        ))

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with right:

        st.success(
            """
            Vehicle Status : Healthy

            Battery Condition : Excellent

            Estimated Battery Life : 6+ Years

            No Critical Issues Detected
            """
        )

    st.markdown("---")

    st.subheader("🤖 AI Recommendation")

    st.info(
        """
        Battery operating normally.

        No overheating detected.

        Battery degradation within safe limits.

        Vehicle ready for normal operation.
        """
    )
    st.image(
"https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tata_Nexon_EV.jpg/640px-Tata_Nexon_EV.jpg",
use_container_width=True
)
    st.success(
"🟢 Vehicle Online | AI Monitoring Active | Battery Healthy"
)
    # ==========================================
# MY EV DIGITAL TWIN
# ==========================================

elif menu == "My EV":

    st.title("🚗 My EV Digital Twin")

    if "running" not in st.session_state:
        st.session_state.running = False

    if "soc_live" not in st.session_state:
        st.session_state.soc_live = 92.0

    if "temp_live" not in st.session_state:
        st.session_state.temp_live = 31.0

    if "voltage_live" not in st.session_state:
        st.session_state.voltage_live = 398.0

    if "distance_live" not in st.session_state:
        st.session_state.distance_live = 0.0

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if not st.session_state.running:

            if st.button("▶ START VEHICLE"):
                st.session_state.running = True
                st.rerun()

        st.success(
            "Vehicle Ready"
            if not st.session_state.running
            else "Vehicle Running"
        )

    with col2:

        if st.session_state.running:

            if st.button("⏹ STOP VEHICLE"):
                st.session_state.running = False
                st.rerun()

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        mode = st.selectbox(
            "Driving Mode",
            [
                "Eco",
                "Normal",
                "Sport"
            ]
        )

        speed = st.slider(
            "Speed (km/h)",
            0,
            120,
            40
        )

    with right:

        weather = st.selectbox(
            "Weather",
            [
                "Sunny",
                "Rainy",
                "Cold"
            ]
        )

        passengers = st.slider(
            "Passengers",
            1,
            5,
            1
        )

    regen = st.checkbox(
        "Enable Regenerative Braking"
    )

    # ---------------------------
    # Simulation
    # ---------------------------

    if st.session_state.running:

        drain = 0.10

        if mode == "Eco":
            drain = 0.05

        elif mode == "Sport":
            drain = 0.15

        st.session_state.soc_live = max(
            st.session_state.soc_live - drain,
            0
        )

        st.session_state.temp_live = min(
            st.session_state.temp_live + 0.05,
            70
        )

        st.session_state.voltage_live = max(
            st.session_state.voltage_live - 0.02,
            350
        )

        st.session_state.distance_live += (
            speed / 500
        )

        if regen and speed < 30:

            st.session_state.soc_live = min(
                st.session_state.soc_live + 0.03,
                100
            )

    soc_live = round(
        st.session_state.soc_live,
        1
    )

    temp_live = round(
        st.session_state.temp_live,
        1
    )

    voltage_live = round(
        st.session_state.voltage_live,
        1
    )

    range_live = int(
        (soc_live / 100) * 325
    )

    if weather == "Rainy":
        range_live -= 15

    elif weather == "Cold":
        range_live -= 25

    range_live -= (
        passengers - 1
    ) * 5

    st.markdown("---")

    a, b, c, d = st.columns(4)

    a.metric(
        "⚡ Speed",
        f"{speed} km/h"
    )

    b.metric(
        "🔋 SOC",
        f"{soc_live}%"
    )

    c.metric(
        "🌡 Temperature",
        f"{temp_live} °C"
    )

    d.metric(
        "🔌 Voltage",
        f"{voltage_live} V"
    )

    st.markdown("---")

    e, f, g = st.columns(3)

    e.metric(
        "🚗 Range Left",
        f"{range_live} km"
    )

    f.metric(
        "🛣 Distance Travelled",
        f"{round(st.session_state.distance_live,2)} km"
    )

    g.metric(
        "❤️ Battery Health",
        "96%"
    )

    st.markdown("---")

    driver_score = 100

    if speed > 90:
        driver_score -= 20

    if temp_live > 50:
        driver_score -= 15

    if soc_live < 20:
        driver_score -= 15

    st.metric(
        "🏆 Driver Score",
        f"{driver_score}/100"
    )

    st.markdown("---")

    st.subheader("🤖 AI Recommendation")

    if temp_live > 50:

        st.error(
            "Battery temperature high. Reduce speed."
        )

    elif soc_live < 20:

        st.warning(
            "Battery low. Charging recommended."
        )

    elif speed > 90:

        st.warning(
            "High speed reducing efficiency."
        )

    else:

        st.success(
            "Vehicle operating normally."
        )

    if st.session_state.running:

        time.sleep(1)

        st.rerun()
        # ==========================================
# ANALYTICS CENTER
# ==========================================

elif menu == "Analytics":

    st.title("📊 EV Analytics Center")

    st.subheader(
        "Battery Performance & Energy Analytics"
    )

    st.markdown("---")

    speed_data = [0, 20, 40, 60, 80, 100, 120]

    soc_data = [100, 97, 94, 88, 80, 70, 58]

    temp_data = [30, 31, 33, 36, 40, 45, 52]

    voltage_data = [
        400,
        398,
        395,
        392,
        388,
        382,
        375
    ]

    range_data = [
        325,
        315,
        300,
        270,
        230,
        180,
        140
    ]

    df = pd.DataFrame({

        "Speed": speed_data,
        "SOC": soc_data,
        "Temperature": temp_data,
        "Voltage": voltage_data,
        "Range": range_data

    })

    st.markdown("## 🔋 Battery Overview")

    a, b, c, d = st.columns(4)

    a.metric(
        "Battery Health",
        "96%"
    )

    b.metric(
        "Battery Score",
        "95/100"
    )

    c.metric(
        "Charge Cycles",
        "425"
    )

    d.metric(
        "Life Remaining",
        "6 Years"
    )

    st.markdown("---")

    st.subheader("📉 SOC vs Speed")

    fig1 = px.line(
        df,
        x="Speed",
        y="SOC",
        markers=True,
        title="SOC Reduction Trend"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader("🌡 Temperature vs Speed")

    fig2 = px.line(
        df,
        x="Speed",
        y="Temperature",
        markers=True,
        title="Temperature Rise Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("⚡ Voltage vs Speed")

    fig3 = px.line(
        df,
        x="Speed",
        y="Voltage",
        markers=True,
        title="Voltage Drop Trend"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.subheader("🚗 Range vs Speed")

    fig4 = px.line(
        df,
        x="Speed",
        y="Range",
        markers=True,
        title="Range Prediction"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🔋 Battery Degradation Forecast"
    )

    years = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    soh_prediction = [
        100,
        97,
        94,
        91,
        87,
        83,
        79,
        74,
        70
    ]

    degradation_df = pd.DataFrame({

        "Year": years,
        "SOH": soh_prediction

    })

    fig5 = px.area(
        degradation_df,
        x="Year",
        y="SOH",
        title="Battery Health Forecast"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "⚙ Energy Consumption"
    )

    consumption_df = pd.DataFrame({

        "Mode": [
            "Eco",
            "Normal",
            "Sport"
        ],

        "Consumption": [
            12,
            16,
            22
        ]

    })

    fig6 = px.bar(
        consumption_df,
        x="Mode",
        y="Consumption",
        title="Energy Consumption (kWh/100km)"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🤖 Analytics AI Insights"
    )

    st.success(
        """
        Battery degradation is within safe limits.

        Expected battery life:
        6+ Years

        No abnormal temperature spikes detected.

        Energy consumption is optimal in Eco mode.

        Vehicle efficiency is above average.
        """
    )
    # ==========================================
# BATTERY INTELLIGENCE CENTER
# ==========================================

elif menu == "Battery Intelligence":

    st.title("🔋 Battery Intelligence Center")

    st.subheader(
        "Advanced Battery Diagnostics & Prediction"
    )

    st.markdown("---")

    a, b, c, d = st.columns(4)

    a.metric(
        "Battery Health",
        "96%"
    )

    b.metric(
        "Battery Score",
        "95/100"
    )

    c.metric(
        "Charge Cycles",
        "425"
    )

    d.metric(
        "Risk Level",
        "LOW"
    )

    st.markdown("---")

    st.subheader(
        "🔋 SOH Forecast"
    )

    years = [
        2026,
        2027,
        2028,
        2029,
        2030,
        2031,
        2032
    ]

    soh_values = [
        96,
        94,
        91,
        88,
        84,
        79,
        74
    ]

    soh_df = pd.DataFrame({

        "Year": years,
        "SOH": soh_values

    })

    fig1 = px.line(
        soh_df,
        x="Year",
        y="SOH",
        markers=True,
        title="Battery Health Prediction"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "⚠ Battery Replacement Prediction"
    )

    st.warning(
        """
        Estimated Replacement Year: 2033

        Expected SOH at Replacement:
        68%

        Current degradation rate:
        Normal
        """
    )

    st.markdown("---")

    st.subheader(
        "⚡ Charging Pattern Analysis"
    )

    charging_df = pd.DataFrame({

        "Method": [
            "Fast Charging",
            "Slow Charging"
        ],

        "Battery Stress": [
            75,
            25
        ]

    })

    fig2 = px.bar(
        charging_df,
        x="Method",
        y="Battery Stress",
        title="Charging Stress Analysis"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🌡 Cell Temperature Monitoring"
    )

    temp_df = pd.DataFrame({

        "Cell": [
            "C1",
            "C2",
            "C3",
            "C4",
            "C5",
            "C6"
        ],

        "Temperature": [
            30,
            31,
            30,
            32,
            31,
            30
        ]

    })

    fig3 = px.bar(
        temp_df,
        x="Cell",
        y="Temperature",
        title="Battery Cell Temperature"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🔌 Cell Voltage Balance"
    )

    voltage_df = pd.DataFrame({

        "Cell": [
            "C1",
            "C2",
            "C3",
            "C4",
            "C5",
            "C6"
        ],

        "Voltage": [
            3.95,
            3.96,
            3.94,
            3.95,
            3.96,
            3.95
        ]

    })

    fig4 = px.line(
        voltage_df,
        x="Cell",
        y="Voltage",
        markers=True,
        title="Cell Voltage Balancing"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🤖 Battery AI Recommendation"
    )

    st.success(
        """
        Battery Pack Status : HEALTHY

        No abnormal degradation detected.

        No overheating detected.

        No cell imbalance detected.

        Predicted Remaining Life:
        6+ Years

        Battery operating within safe limits.
        """
    )

    st.markdown("---")

    st.subheader(
        "🏆 Battery Intelligence Score"
    )

    fig5 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=95,
        title={
            "text": "Battery Intelligence Score"
        },
        gauge={
            "axis": {
                "range": [0, 100]
            }
        }
    ))

    st.plotly_chart(
        fig5,
        use_container_width=True
    )
    # ==========================================
# AI CENTER
# ==========================================

elif menu == "AI Center":

    st.title("🤖 AI Command Center")

    st.subheader(
        "Artificial Intelligence Powered EV Insights"
    )

    st.markdown("---")

    a, b, c, d = st.columns(4)

    a.metric(
        "AI Confidence",
        "97%"
    )

    b.metric(
        "Battery Risk",
        "LOW"
    )

    c.metric(
        "Driving Score",
        "92/100"
    )

    d.metric(
        "Fault Risk",
        "LOW"
    )

    st.markdown("---")

    st.subheader(
        "🧠 AI Health Assessment"
    )

    st.success(
        """
        Vehicle operating within safe limits.

        No abnormal battery degradation detected.

        No thermal runaway risk detected.

        AI confidence level extremely high.
        """
    )

    st.markdown("---")

    st.subheader(
        "⚠ Fault Prediction Engine"
    )

    fault_df = pd.DataFrame({

        "Component": [
            "Battery Pack",
            "Motor",
            "Cooling System",
            "Controller",
            "Brakes"
        ],

        "Risk": [
            4,
            3,
            6,
            2,
            5
        ]

    })

    fig1 = px.bar(
        fault_df,
        x="Component",
        y="Risk",
        title="Predicted Failure Risk (%)"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🔋 Smart Charging AI"
    )

    st.info(
        """
        Recommended Charging Window:
        11 PM – 6 AM

        Estimated Electricity Cost Reduction:
        18%

        Recommended Maximum Charge:
        90%
        """
    )

    st.markdown("---")

    st.subheader(
        "🚗 Driving Pattern Analysis"
    )

    driving_df = pd.DataFrame({

        "Category": [
            "Acceleration",
            "Braking",
            "Cornering",
            "Efficiency"
        ],

        "Score": [
            88,
            93,
            90,
            95
        ]

    })

    fig2 = px.bar(
        driving_df,
        x="Category",
        y="Score",
        title="Driving Pattern Score"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🛣 Route Efficiency AI"
    )

    route_df = pd.DataFrame({

        "Route": [
            "Route A",
            "Route B",
            "Route C"
        ],

        "Efficiency": [
            88,
            95,
            82
        ]

    })

    fig3 = px.bar(
        route_df,
        x="Route",
        y="Efficiency",
        title="Route Efficiency Analysis"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.success(
        """
        Best Route Identified:
        Route B

        Estimated Energy Saving:
        12%
        """
    )

    st.markdown("---")

    st.subheader(
        "🌡 Thermal Risk Forecast"
    )

    thermal_df = pd.DataFrame({

        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        "Risk": [
            2,
            3,
            4,
            6,
            9,
            12
        ]

    })

    fig4 = px.line(
        thermal_df,
        x="Month",
        y="Risk",
        markers=True,
        title="Thermal Stress Prediction"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🔮 AI Future Forecast"
    )

    st.success(
        """
        Expected Battery Life:
        6+ Years

        Expected Motor Life:
        10+ Years

        Predicted Reliability:
        94%

        Vehicle Health Outlook:
        EXCELLENT
        """
    )

    st.markdown("---")

    st.subheader(
        "🏆 AI Intelligence Score"
    )

    fig5 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=97,
        title={
            "text": "AI Intelligence Score"
        },
        gauge={
            "axis": {
                "range": [0, 100]
            }
        }
    ))

    st.plotly_chart(
        fig5,
        use_container_width=True
    )
    # ==========================================
# SUSTAINABILITY CENTER
# ==========================================

elif menu == "Sustainability":

    st.title("🌍 Sustainability Center")

    st.subheader(
        "Environmental & Economic Impact Analysis"
    )

    st.markdown("---")

    total_distance = 25000
    petrol_cost = 200000
    ev_cost = 55000

    savings = petrol_cost - ev_cost

    co2_saved = 2.8
    trees_equivalent = 43

    a, b, c, d = st.columns(4)

    a.metric(
        "🌍 CO₂ Saved",
        f"{co2_saved} Tons"
    )

    b.metric(
        "🌳 Trees Equivalent",
        trees_equivalent
    )

    c.metric(
        "⛽ Fuel Cost Saved",
        f"₹{savings:,}"
    )

    d.metric(
        "🛣 Distance",
        f"{total_distance:,} km"
    )

    st.markdown("---")

    st.subheader(
        "⛽ EV vs Petrol Cost Comparison"
    )

    cost_df = pd.DataFrame({

        "Vehicle": [
            "Petrol Vehicle",
            "EV Vehicle"
        ],

        "Cost": [
            petrol_cost,
            ev_cost
        ]

    })

    fig1 = px.bar(
        cost_df,
        x="Vehicle",
        y="Cost",
        title="Running Cost Comparison"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🌍 Carbon Emission Comparison"
    )

    carbon_df = pd.DataFrame({

        "Vehicle": [
            "Petrol",
            "EV"
        ],

        "CO2": [
            8.5,
            2.1
        ]

    })

    fig2 = px.bar(
        carbon_df,
        x="Vehicle",
        y="CO2",
        title="Carbon Emission Comparison"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🌳 Environmental Contribution"
    )

    contribution_df = pd.DataFrame({

        "Category": [
            "CO₂ Reduction",
            "Fuel Saving",
            "Clean Energy",
            "Noise Reduction"
        ],

        "Score": [
            95,
            90,
            88,
            92
        ]

    })

    fig3 = px.pie(
        contribution_df,
        values="Score",
        names="Category",
        title="Environmental Contribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "📈 Lifetime Savings Forecast"
    )

    forecast_df = pd.DataFrame({

        "Year": [
            1,2,3,4,5,6,7,8
        ],

        "Savings": [
            50000,
            100000,
            150000,
            200000,
            250000,
            300000,
            350000,
            400000
        ]

    })

    fig4 = px.line(
        forecast_df,
        x="Year",
        y="Savings",
        markers=True,
        title="Lifetime Cost Savings Forecast"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🏆 Sustainability Score"
    )

    fig5 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=93,
        title={
            "text": "Sustainability Score"
        },
        gauge={
            "axis": {
                "range": [0, 100]
            }
        }
    ))

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🤖 Sustainability AI Insights"
    )

    st.success(
        """
        Environmental Performance : Excellent

        CO₂ reduction significantly higher
        than traditional petrol vehicles.

        Estimated fuel savings exceed ₹1.4 lakh.

        Sustainability rating above industry average.

        EV ownership contributes positively
        to long-term environmental goals.
        """
    )
    # ==========================================
# MAINTENANCE CENTER
# ==========================================

elif menu == "Maintenance":

    st.title("🔧 Predictive Maintenance Center")

    st.subheader(
        "Vehicle Health & Maintenance Intelligence"
    )

    st.markdown("---")

    a, b, c, d = st.columns(4)

    a.metric(
        "🚗 Vehicle Health",
        "94%"
    )

    b.metric(
        "⚙ Motor Health",
        "96%"
    )

    c.metric(
        "🛞 Tire Health",
        "88%"
    )

    d.metric(
        "🛑 Brake Health",
        "91%"
    )

    st.markdown("---")

    st.subheader(
        "📅 Service Due Prediction"
    )

    st.info(
        """
        Next Service Due:
        4,200 km Remaining

        Estimated Service Date:
        December 2026

        Maintenance Risk:
        LOW
        """
    )

    st.markdown("---")

    st.subheader(
        "⚙ Motor Performance Analysis"
    )

    motor_df = pd.DataFrame({

        "Parameter": [
            "Efficiency",
            "Temperature",
            "Power Output",
            "Torque Stability"
        ],

        "Score": [
            96,
            92,
            95,
            94
        ]

    })

    fig1 = px.bar(
        motor_df,
        x="Parameter",
        y="Score",
        title="Motor Performance"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🛞 Tire Wear Monitoring"
    )

    tire_df = pd.DataFrame({

        "Tire": [
            "Front Left",
            "Front Right",
            "Rear Left",
            "Rear Right"
        ],

        "Health": [
            88,
            90,
            86,
            89
        ]

    })

    fig2 = px.bar(
        tire_df,
        x="Tire",
        y="Health",
        title="Tire Condition"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🛑 Brake Health Analysis"
    )

    brake_df = pd.DataFrame({

        "Component": [
            "Front Brake",
            "Rear Brake"
        ],

        "Health": [
            91,
            93
        ]

    })

    fig3 = px.pie(
        brake_df,
        values="Health",
        names="Component",
        title="Brake Health Distribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "💰 Maintenance Cost Forecast"
    )

    cost_df = pd.DataFrame({

        "Year": [
            2026,
            2027,
            2028,
            2029,
            2030
        ],

        "Cost": [
            6000,
            8000,
            10000,
            12000,
            14000
        ]

    })

    fig4 = px.line(
        cost_df,
        x="Year",
        y="Cost",
        markers=True,
        title="Maintenance Cost Forecast"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🤖 Fault Detection AI"
    )

    st.success(
        """
        No Critical Faults Detected

        Motor Operating Normally

        Battery Cooling System Healthy

        Tire Wear Within Limits

        Brake System Healthy
        """
    )

    st.markdown("---")

    st.subheader(
        "🔮 Remaining Useful Life"
    )

    rul_df = pd.DataFrame({

        "Component": [
            "Battery",
            "Motor",
            "Brakes",
            "Tires"
        ],

        "Remaining Years": [
            6,
            10,
            4,
            3
        ]

    })

    fig5 = px.bar(
        rul_df,
        x="Component",
        y="Remaining Years",
        title="Remaining Useful Life Prediction"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🏆 Vehicle Health Score"
    )

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=94,
        title={
            "text": "Vehicle Health Score"
        },
        gauge={
            "axis": {
                "range": [0, 100]
            }
        }
    ))

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    st.success(
        """
        Overall Vehicle Condition:
        EXCELLENT

        Predicted Reliable Operation:
        6+ Years

        Maintenance Risk:
        LOW
        """
    )
    # ==========================================
# EXECUTIVE REPORT CENTER
# ==========================================

elif menu == "Reports":

    st.title("📄 Executive Report Center")

    st.subheader(
        "Complete EV Digital Twin Summary"
    )

    st.markdown("---")

    a, b, c, d = st.columns(4)

    a.metric(
        "Vehicle Score",
        "95/100"
    )

    b.metric(
        "Battery Score",
        "96/100"
    )

    c.metric(
        "AI Score",
        "97/100"
    )

    d.metric(
        "Sustainability",
        "93/100"
    )

    st.markdown("---")

    st.subheader(
        "🚗 Vehicle Executive Summary"
    )

    st.success(
        """
        Vehicle : Tata Nexon EV

        Vehicle Health : Excellent

        Battery Health : 96%

        Predicted Battery Life : 6+ Years

        Reliability Score : 94%

        Overall Status : HEALTHY
        """
    )

    st.markdown("---")

    st.subheader(
        "🔋 Battery Report"
    )

    battery_report = pd.DataFrame({

        "Parameter": [
            "SOC",
            "SOH",
            "Voltage",
            "Temperature",
            "Charge Cycles"
        ],

        "Value": [
            "92%",
            "96%",
            "398V",
            "31°C",
            "425"
        ]

    })

    st.dataframe(
        battery_report,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🔧 Maintenance Report"
    )

    maintenance_report = pd.DataFrame({

        "Component": [
            "Battery",
            "Motor",
            "Brakes",
            "Tires",
            "Cooling System"
        ],

        "Health": [
            "96%",
            "96%",
            "91%",
            "88%",
            "94%"
        ]

    })

    st.dataframe(
        maintenance_report,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🌍 Sustainability Report"
    )

    sustainability_report = pd.DataFrame({

        "Metric": [
            "CO₂ Saved",
            "Trees Equivalent",
            "Fuel Savings",
            "Distance Covered"
        ],

        "Value": [
            "2.8 Tons",
            "43 Trees",
            "₹1,45,000",
            "25,000 km"
        ]

    })

    st.dataframe(
        sustainability_report,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "📊 Overall Performance"
    )

    score_df = pd.DataFrame({

        "Category": [
            "Battery",
            "AI",
            "Maintenance",
            "Efficiency",
            "Sustainability"
        ],

        "Score": [
            96,
            97,
            94,
            92,
            93
        ]

    })

    fig1 = px.bar(
        score_df,
        x="Category",
        y="Score",
        title="Overall Performance Score"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🏆 Final Vehicle Health Score"
    )

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=95,
        title={
            "text": "Final Vehicle Score"
        },
        gauge={
            "axis": {
                "range": [0, 100]
            }
        }
    ))

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "📥 Export Report"
    )

    export_df = pd.DataFrame({

        "Metric": [
            "Battery Health",
            "Vehicle Health",
            "AI Score",
            "CO₂ Saved"
        ],

        "Value": [
            "96%",
            "95%",
            "97%",
            "2.8 Tons"
        ]

    })

    csv = export_df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download CSV Report",
        data=csv,
        file_name="EV_Digital_Twin_Report.csv",
        mime="text/csv"
    )

    st.markdown("---")

    st.subheader(
        "🤖 Executive AI Recommendation"
    )

    st.success(
        """
        Vehicle Condition : Excellent

        Battery Health Above Industry Average

        Maintenance Risk : Low

        Sustainability Impact : High

        Continue Current Driving Pattern

        Recommended Action:
        Annual Preventive Checkup
        """
    )

    st.markdown("---")

    st.success(
        """
        EV Digital Twin Analysis Completed Successfully

        ⭐⭐⭐⭐⭐

        Project Status:
        READY FOR DEMONSTRATION
        """
    )
    # ==========================================
# PART 9
# TRIP PERFORMANCE & FUTURE PREDICTION
# ==========================================

st.markdown("---")

if menu == "My EV":

    if not st.session_state.running:

        st.header("📊 Trip Performance Review")

        used_battery = round(
            92 - st.session_state.soc_live,
            2
        )

        temp_rise = round(
            st.session_state.temp_live - 31,
            2
        )

        range_used = round(
            st.session_state.distance_live,
            2
        )

        efficiency_score = 100

        if used_battery > 20:
            efficiency_score -= 15

        if temp_rise > 10:
            efficiency_score -= 10

        if range_used > 100:
            efficiency_score -= 5

        a, b, c, d = st.columns(4)

        a.metric(
            "🔋 Battery Used",
            f"{used_battery}%"
        )

        b.metric(
            "🌡 Temp Increase",
            f"{temp_rise} °C"
        )

        c.metric(
            "🛣 Distance Travelled",
            f"{range_used} km"
        )

        d.metric(
            "🏆 Efficiency",
            f"{efficiency_score}/100"
        )

        st.markdown("---")

        st.subheader("🔮 Future Prediction")

        remaining_life = round(
            6 - (used_battery / 500),
            2
        )

        predicted_range = round(
            st.session_state.soc_live * 3.25,
            0
        )

        col1, col2 = st.columns(2)

        col1.info(
            f"""
            🔋 Predicted Battery Life

            {remaining_life} Years

            Current SOH Healthy
            """
        )

        col2.info(
            f"""
            🚗 Predicted Remaining Range

            {predicted_range} km

            Based on Current Usage
            """
        )

        st.markdown("---")

        st.subheader("🤖 AI Driving Advice")

        if efficiency_score >= 90:

            st.success(
                """
                Excellent Driving Pattern.

                Battery stress very low.

                Vehicle health preserved.
                """
            )

        elif efficiency_score >= 75:

            st.warning(
                """
                Average Driving Pattern.

                Reduce aggressive acceleration.

                Use Eco Mode more often.
                """
            )

        else:

            st.error(
                """
                Aggressive Driving Detected.

                Battery degradation may increase.

                Reduce speed and temperature load.
                """
            )

        st.markdown("---")

        st.subheader("📈 Next Trip Recommendation")

        if st.session_state.soc_live > 70:

            st.success(
                "Battery sufficient for long-distance travel."
            )

        elif st.session_state.soc_live > 40:

            st.warning(
                "Medium trip recommended. Charge before long journeys."
            )

        else:

            st.error(
                "Charging recommended before next trip."
            )
            # ==========================================
# PART 10
# SMART RANGE PREDICTOR
# ==========================================

if menu == "My EV":

    st.markdown("---")
    st.header("🧠 Smart Range Prediction Engine")

    current_soc = round(st.session_state.soc_live, 1)

    base_range = current_soc * 3.25

    eco_range = round(base_range * 1.12, 0)
    normal_range = round(base_range, 0)
    sport_range = round(base_range * 0.82, 0)

    ac_range = round(base_range * 0.94, 0)
    cold_range = round(base_range * 0.88, 0)

    soh_factor = 96 / 100
    health_adjusted = round(base_range * soh_factor, 0)

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🌱 Eco Mode Range",
        f"{eco_range} km"
    )

    c2.metric(
        "🚗 Normal Mode Range",
        f"{normal_range} km"
    )

    c3.metric(
        "🏁 Sport Mode Range",
        f"{sport_range} km"
    )

    st.markdown("---")

    d1, d2, d3 = st.columns(3)

    d1.metric(
        "❄ Cold Weather Range",
        f"{cold_range} km"
    )

    d2.metric(
        "❄ AC ON Range",
        f"{ac_range} km"
    )

    d3.metric(
        "🔋 SOH Adjusted Range",
        f"{health_adjusted} km"
    )

    st.markdown("---")

    st.subheader("🛣 Trip Feasibility Check")

    trip_distance = st.number_input(
        "Enter Trip Distance (km)",
        min_value=1,
        value=150
    )

    if trip_distance <= health_adjusted:

        st.success(
            f"""
            Trip Possible ✅

            Required Distance:
            {trip_distance} km

            Predicted Remaining Range:
            {health_adjusted} km
            """
        )

    else:

        st.error(
            f"""
            Charging Required ⚠

            Required Distance:
            {trip_distance} km

            Available Range:
            {health_adjusted} km
            """
        )

    st.markdown("---")

    st.subheader("🤖 AI Range Recommendation")

    if health_adjusted > 250:

        st.success(
            """
            Long Distance Travel Recommended.

            Battery Condition Excellent.

            Range Anxiety Risk Low.
            """
        )

    elif health_adjusted > 120:

        st.warning(
            """
            Medium Distance Travel Recommended.

            Consider charging before long trips.
            """
        )

    else:

        st.error(
            """
            Battery Low.

            Charging Recommended Before Travel.
            """
        )
st.markdown("---")

st.caption(
"Developed by Anurag Kumar | EV Digital Twin Project"
)