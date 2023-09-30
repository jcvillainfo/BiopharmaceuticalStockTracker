import yfinance as yf
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# List of biopharmaceutical company symbols
company_symbols = [
    "AMPE", "SNGX", "CRMD", "TNXP", "ADMP", "CLSN", "CERC",
    "NVCN", "DFFN", "GLMD", "INO", "NOVN", "IOVA", "SNSS", "CATB", "ONCY"
]

# Function to fetch and plot stock prices
def plot_stock_prices():
    selected_symbol = symbol_var.get()
    
    # Fetch stock price data for the selected company
    stock = yf.Ticker(selected_symbol)
    data = stock.history(period="1y")
    
    # Clear previous plot
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Create a new plot
    fig = Figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax.plot(data.index, data["Close"], label=selected_symbol)
    ax.set_xlabel("Date")
    ax.set_ylabel("Stock Price (USD)")
    ax.set_title(f"Stock Price for {selected_symbol}")
    ax.legend()
    
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.draw()

# Create the main window
app = tk.Tk()
app.title("Stock Price Tracker")

# Create a frame for the GUI components
frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

# Dropdown for selecting a company
symbol_var = tk.StringVar()
symbol_label = tk.Label(frame, text="Select a Company:")
symbol_label.pack()
symbol_dropdown = tk.OptionMenu(frame, symbol_var, *company_symbols)
symbol_dropdown.pack()

# Button to fetch and plot stock prices
plot_button = tk.Button(frame, text="Plot Stock Prices", command=plot_stock_prices)
plot_button.pack()

# Frame for displaying the plot
graph_frame = tk.Frame(app)
graph_frame.pack(fill=tk.BOTH, expand=True)

# Start the GUI application
app.mainloop()
