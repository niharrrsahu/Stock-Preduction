import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample stock data (you should replace this with real data)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Close': [100, 102, 105, 103, 107]
}


# Function to analyze stock data and update the GUI
def analyze_stock():
    # Fetch stock data from an API or database here
    # Perform your analysis (e.g., calculate moving averages)
    # Replace the sample data and analysis with your own logic

    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)

    # Calculate a 5-day Simple Moving Average (SMA)
    df['SMA_5'] = df['Close'].rolling(window=5).mean()

    # Display the stock data and SMA in a text box

    output_text.delete('1.0', tk.END)  # Clear existing text
    output_text.insert(tk.END, df.to_string(index=False))

    # Create a plot of the stock data and SMA
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(df['Date'], df['Close'], label='Close Price')
    ax.plot(df['Date'], df['SMA_5'], label='5-Day SMA')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    # Embed the plot in the GUI
    canvas = FigureCanvasTkAgg(fig, master=analysis_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()


# Create the main application window
app = tk.Tk()
app.title("Stock Analysis Tool")

# Create a frame for the stock analysis
analysis_frame = ttk.Frame(app)
analysis_frame.pack(padx=10, pady=10)

# Create a button to trigger the analysis
analyze_button = ttk.Button(analysis_frame, text="Analyze Stock", command=analyze_stock)
analyze_button.pack()

# Create a text box to display analysis results
output_text = tk.Text(analysis_frame, wrap=tk.WORD, height=10, width=40, background="blue")
output_text.pack()

app.mainloop()