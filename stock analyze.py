import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Unique stock data for your project
your_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Close': [110, 108, 115, 113, 120]  # Your friend can have different data
}

# Function to analyze stock data and update the GUI
def analyze_stock():
    # Your analysis logic here (e.g., different indicators or strategies)
    df = pd.DataFrame(your_data)

    # Calculate a 7-day Exponential Moving Average (EMA)
    df['EMA_7'] = df['Close'].ewm(span=7, adjust=False).mean()

    # Update output text and plot with your analysis results
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, df.to_string(index=False))

    fig = Figure(figsize=(6, 5), dpi=100, facecolor='#000000')  # Black background
    ax = fig.add_subplot(111)
    ax.plot(df['Date'], df['Close'], color='green', label='Close Price')  # Dark green text
    ax.plot(df['Date'], df['EMA_7'], color='blue', linestyle='--', label='7-Day EMA')  # Blue dashed line
    ax.set_xlabel('Date', color='lightgreen')  # Dark green text
    ax.set_ylabel('Price', color='lightgreen')  # Dark green text
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=analysis_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Create the main application window
app = tk.Tk()
app.title("Your Unique Stock Analysis Tool")

# Create a frame for the stock analysis
analysis_frame = ttk.Frame(app, padding=10, style="Analysis.TFrame")  # Apply custom style
analysis_frame.pack()

# Create a button to trigger the analysis
analyze_button = ttk.Button(analysis_frame, text="Analyze Stock", command=analyze_stock)
analyze_button.pack()

# Create a custom style for the frame
style = ttk.Style()
style.configure("Analysis.TFrame", background="black")

# Create a text box to display analysis results
output_text = tk.Text(analysis_frame, wrap=tk.WORD, height=10, width=40, bg="black", fg="lightgreen")  # Black background, dark green text
output_text.pack()

app.mainloop()
