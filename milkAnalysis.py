import pandas as pd
import matplotlib.pyplot as plt 

def main_menu():
    print("\n📋 Main Menu:")
    print("1. Show summary statistics")
    print("2. Plot sales trends over time")
    print("3. Compare milk type sales for a specific month")
    print("4. Exit")



def load_data(file_path):
    """
    Loads milk sales data from a CSV file.
    """
    df = pd.read_csv(file_path)

    if "Month" in df.columns:
        df.rename(columns={"Month": "Date"}, inplace=True)

    df["Date"] = pd.to_datetime(df["Date"], format="%Y %B", errors='coerce')

    return df



def show_summary(df):
    """
    Show average, max, min, and standard deviation for each milk type.
    """
    milk_types = df["Type of Milk"].unique()

    print("\n📈 Summary Statistics by Milk Type:\n")

    for milk in milk_types:
        filtered = df[df["Type of Milk"] == milk]
        values = filtered["VALUE"]

        mean_val = values.mean()
        max_val = values.max()
        min_val = values.min()
        std_val = values.std()

        print(f"🍼 {milk}")
        print(f"  ➤ Average: {mean_val:.2f}")
        print(f"  ➤ Max:     {max_val:.2f}")
        print(f"  ➤ Min:     {min_val:.2f}")
        print(f"  ➤ Std Dev: {std_val:.2f}\n")


def plot_sales_trend(df):
    """
    Plots sales trends over time for each milk type using a line chart.
    """
    milk_types = df["Type of Milk"].unique()

    print("\n📉 Generating sales trend line chart...\n")

    for milk in milk_types:
        filtered = df[df["Type of Milk"] == milk]
        plt.plot(filtered["Date"], filtered["VALUE"], label=milk)

    plt.title("Milk Sales Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales (Million Litres)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # Save the figure
    plt.savefig("milk_sales_trend.png")
    print("Line chart saved as 'milk_sales_trend.png'")
    plt.show()

def compare_monthly_sales(df, selected_month):
    """
    Plots a bar chart comparing milk type sales for a selected month.
    """
    # Convert selected_month string to datetime format
    try:
        selected_date = pd.to_datetime(selected_month, format="%Y %B")
    except ValueError:
        print("❌ Invalid date format. Please use 'YYYY Month' (e.g., '2022 January').")
        return

    # Filter data for that month
    filtered = df[df["Date"] == selected_date]

    if filtered.empty:
        print("⚠️ No data found for that month.")
        return

    # Extract milk types and their values
    milk_types = filtered["Type of Milk"]
    values = filtered["VALUE"]

    print(f"\n📊 Milk sales for {selected_month}:\n")

    # Create the bar chart
    plt.bar(milk_types, values)
    plt.title(f"Milk Sales by Type - {selected_month}")
    plt.xlabel("Type of Milk")
    plt.ylabel("Sales (Million Litres)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = f"milk_sales_{selected_month.replace(' ', '_')}.png"
    plt.savefig(filename)
    print(f"✅ Bar chart saved as '{filename}'")
    plt.show()

def main():
    print("📊 Retail Sales Analysis - Milk Products")
    file_path = "milkSales.csv"  
    df = load_data(file_path)

    print("\n✅ Data loaded successfully.")
    print("Preview of dataset:")
    print(df.head())

    while True:
        main_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            show_summary(df)
        elif choice == '2':
            plot_sales_trend(df)
        elif choice == '3':
            month_input = input("Enter a month (e.g., '2022 January'): ")
            compare_monthly_sales(df, month_input)
        elif choice == '4':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

# Run the main function
main()
