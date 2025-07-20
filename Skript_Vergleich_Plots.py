

# ==================================================================================================
# Script:            Skript_Vergleich_Plots.py
# Author:            Mohamad Wehbi
# Martikelnummer:    5235487 
# ==================================================================================================


import pandas as pd
import matplotlib.pyplot as plt

# === Dateien einlesen ===
df1 = pd.read_csv("E:/Mohamad Wehbi/HSB/6 Semester/ANS/simulation/Q10_messwerte.csv")
df2 = pd.read_csv("E:/Mohamad Wehbi/HSB/6 Semester/ANS/simulation/Q10_messwerte.csv")
df3 = pd.read_csv("E:/Mohamad Wehbi/HSB/6 Semester/ANS/simulation/Q10_messwerte.csv")
df4 = pd.read_csv("E:/Mohamad Wehbi/HSB/6 Semester/ANS/simulation/Q10_messwerte.csv")

# Spaltennamen bereinigen
df1.columns = [col.strip() for col in df1.columns]
df2.columns = [col.strip() for col in df2.columns]
df3.columns = [col.strip() for col in df3.columns]
df4.columns = [col.strip() for col in df4.columns]

# Daten extrahieren
f1, amp1, phase1 = df1["frequency"], df1["V(BPF) (Verstärkung)"], df1["V(BPF) (Phase)"]
f2, amp2, phase2 = df2["frequency"], df2["V(BSF) (Verstärkung)"], df2["V(BSF) (Phase)"]
f3, amp3, phase3 = df3["frequency"], df3["V(HPF) (Verstärkung)"], df3["V(HPF) (Phase)"]
f4, amp4, phase4 = df4["frequency"], df4["V(LPF) (Verstärkung)"], df4["V(LPF) (Phase)"]

# === Plot erstellen ===
fig, ax1 = plt.subplots(figsize=(10, 6))

# Amplituden-Plot
ax1.semilogx(f1, amp1, label="Amplitude Bandpass", color="blue")
ax1.semilogx(f2, amp2, label="Amplitude Bandstop", color="red")
ax1.semilogx(f3, amp3, label="Amplitude Hochpass", color="darkorange")
ax1.semilogx(f4, amp4, label="Amplitude Tiefpass", color="darkgreen")
ax1.set_xlabel("Frequenz in Hz")
ax1.set_ylabel("Amplitude in dB", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(True, which="both", linestyle="--")

# Phase-Plot auf rechter Y-Achse
ax2 = ax1.twinx()
ax2.semilogx(f1, phase1, label="Phase Bandpass", color="blue", linestyle="--")
ax2.semilogx(f2, phase2, label="Phase Bandstop", color="red", linestyle="--")
ax2.semilogx(f3, phase3, label="Phase Hochpass", color="darkorange", linestyle="--")
ax2.semilogx(f4, phase4, label="Phase Tiefpass", color="darkgreen", linestyle="--")
ax2.set_ylabel("Phase in °", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Legenden kombinieren
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="lower left")

# Titel & Anzeige
plt.title("Bode-Plot der simulierten Biquad-Schaltung für Q=10")
plt.tight_layout()
plt.show()
