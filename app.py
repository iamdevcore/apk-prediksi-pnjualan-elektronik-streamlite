import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Dashboard Penjualan",
    page_icon="📊",
    layout="wide"
)

# ======================================================
# KONSTANTA BULAN
# ======================================================
bulan_order = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Agu","Sep","Okt","Nov","Des"]
bulan_map = {
    1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"Mei",6:"Jun",
    7:"Jul",8:"Agu",9:"Sep",10:"Okt",11:"Nov",12:"Des",
    "januari":"Jan","februari":"Feb","maret":"Mar","april":"Apr",
    "mei":"Mei","juni":"Jun","juli":"Jul","agustus":"Agu",
    "september":"Sep","oktober":"Okt","november":"Nov","desember":"Des",
    "jan":"Jan","feb":"Feb","mar":"Mar","apr":"Apr",
    "jun":"Jun","jul":"Jul","agu":"Agu","sep":"Sep",
    "okt":"Okt","nov":"Nov","des":"Des"
}

def norm_bulan(x):
    if pd.isna(x):
        return None
    if isinstance(x,(int,float)):
        return bulan_map.get(int(x))
    return bulan_map.get(str(x).lower().strip())

# ======================================================
# SIDEBAR – UPLOAD
# ======================================================
st.sidebar.header("📂 Upload Data Penjualan")
file = st.sidebar.file_uploader("Upload Excel / CSV", type=["xlsx","csv"])

# ======================================================
# INPUT MANUAL
# ======================================================
st.sidebar.divider()
st.sidebar.subheader("✍️ Input Manual (Opsional)")
manual_mode = st.sidebar.checkbox("Aktifkan Input Manual")

manual_year = None
manual_data = {}

if manual_mode:
    manual_year = st.sidebar.number_input("Tahun Manual", min_value=1500, value=2025)
    st.sidebar.markdown("### Penjualan & Target Bulanan")
    for b in bulan_order:
        c1, c2 = st.sidebar.columns(2)
        with c1:
            manual_data[f"penjualan_{b}"] = st.number_input(f"Penjualan {b}", min_value=0, value=0)
        with c2:
            manual_data[f"target_{b}"] = st.number_input(f"Target {b}", min_value=1, value=60)

# ======================================================
# LOAD DATA
# ======================================================
if not file:
    st.warning("Silakan upload file Excel / CSV")
    st.stop()

df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
df.columns = df.columns.str.lower().str.strip()

required = {"tahun","bulan","penjualan","target"}
if not required.issubset(df.columns):
    st.error("File harus memiliki kolom: tahun, bulan, penjualan, target")
    st.stop()

df["bulan"] = df["bulan"].apply(norm_bulan)
df = df.dropna(subset=["bulan"])
df["bulan"] = pd.Categorical(df["bulan"], categories=bulan_order, ordered=True)
df = df.sort_values(["tahun","bulan"])

# ======================================================
# OVERRIDE MANUAL
# ======================================================
if manual_mode:
    df = df[df["tahun"] != manual_year]
    rows = []
    for b in bulan_order:
        rows.append({
            "tahun": manual_year,
            "bulan": b,
            "penjualan": manual_data[f"penjualan_{b}"],
            "target": manual_data[f"target_{b}"]
        })
    df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

# ======================================================
# HITUNG KPI + PERSENTASE
# ======================================================
df["selisih"] = df["penjualan"] - df["target"]
df["persentase"] = (df["penjualan"] / df["target"]) * 100
df["status"] = df["persentase"].apply(lambda x: "Tercapai" if x >= 100 else "Tidak Tercapai")

# ======================================================
# FILTER STATUS
# ======================================================
st.sidebar.divider()
st.sidebar.subheader("🔎 Filter Status")
status_pilih = st.sidebar.multiselect(
    "Pilih Status",
    df["status"].unique(),
    default=df["status"].unique()
)
df_view = df[df["status"].isin(status_pilih)]

# ======================================================
# BULAN & TAHUN TERBAIK
# ======================================================
best_month = df_view.loc[df_view["selisih"].idxmax()]
bulan_terbaik = f'{best_month["bulan"]} {best_month["tahun"]}'
nilai_bulan_terbaik = best_month["selisih"]

tahun_best = (
    df_view.groupby("tahun")["selisih"]
    .mean()
    .reset_index()
    .sort_values("selisih", ascending=False)
)
tahun_terbaik = int(tahun_best.iloc[0]["tahun"])
nilai_tahun_terbaik = round(tahun_best.iloc[0]["selisih"], 2)

# ======================================================
# TABS
# ======================================================
tab1, tab2, tab3 = st.tabs(["📊 Dashboard","📈 Grafik","📋 Evaluasi"])

# ======================================================
# DASHBOARD
# ======================================================
with tab1:
    st.header("📊 Ringkasan KPI Penjualan")
    c1,c2,c3,c4,c5,c6,c7 = st.columns(7)

    c1.metric("Rata-rata Penjualan", round(df_view["penjualan"].mean(),2))
    c2.metric("Rata-rata Selisih", round(df_view["selisih"].mean(),2))
    c3.metric("Rata-rata Pencapaian", f'{round(df_view["persentase"].mean(),2)}%')
    c4.metric("Tercapai", (df_view["status"]=="Tercapai").sum())
    c5.metric("Tidak Tercapai", (df_view["status"]=="Tidak Tercapai").sum())
    c6.metric("🏆 Bulan Terbaik", bulan_terbaik, f'{nilai_bulan_terbaik:+}')
    c7.metric("🥇 Tahun Terbaik", tahun_terbaik, f'Avg {nilai_tahun_terbaik:+}')

    st.dataframe(
        df_view[["tahun","bulan","penjualan","target","selisih","persentase","status"]],
        use_container_width=True
    )

# ======================================================
# GRAFIK
# ======================================================
with tab2:
    st.header("📈 Grafik Penjualan & Evaluasi")

    tahun_pilih = st.selectbox("Pilih Tahun", sorted(df_view["tahun"].unique()))
    dfg = df_view[df_view["tahun"] == tahun_pilih]

    fig1 = go.Figure()
    fig1.add_scatter(x=dfg["bulan"], y=dfg["penjualan"], mode="lines+markers", name="Penjualan")
    fig1.add_scatter(x=dfg["bulan"], y=dfg["target"], mode="lines", name="Target", line=dict(dash="dash"))
    st.plotly_chart(fig1, use_container_width=True)

    status_count = dfg["status"].value_counts()

    fig2 = go.Figure([
        go.Bar(
            x=status_count.index,
            y=status_count.values,
            text=status_count.values,
            textposition="auto"
        )
    ])
    fig2.update_layout(title="Grafik Tercapai vs Tidak Tercapai")
    st.plotly_chart(fig2, use_container_width=True)

# ======================================================
# EVALUASI
# ======================================================
with tab3:
    st.header("📋 Detail Evaluasi Bulanan")
    st.dataframe(df_view.sort_values(["tahun","bulan"]), use_container_width=True)

st.caption("© 2025 | Dashboard Penjualan – FINAL + Persentase & Grafik")
