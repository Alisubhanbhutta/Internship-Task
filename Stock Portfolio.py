import yfinance as yf


portfolio = {}

def add_stock():
    """Add stock to the portfolio"""
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {symbol}: "))

    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity

    print(f"✅ Added {quantity} shares of {symbol} to your portfolio!\n")

def remove_stock():
    """Remove stock from the portfolio"""
    symbol = input("Enter stock symbol to remove: ").upper()

    if symbol not in portfolio:
        print(f"⚠️ {symbol} is not in your portfolio!\n")
        return

    quantity = int(input(f"Enter quantity to remove (you own {portfolio[symbol]} shares): "))

    if quantity >= portfolio[symbol]:
        del portfolio[symbol]
        print(f"❌ Removed all shares of {symbol} from your portfolio.\n")
    else:
        portfolio[symbol] -= quantity
        print(f"✅ Removed {quantity} shares of {symbol}, remaining: {portfolio[symbol]}.\n")

def get_stock_price(symbol):
    """Get real-time stock price"""
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"][-1]  
        return round(price, 2)
    except Exception:
        return None

def show_portfolio():
    """Display portfolio with real-time prices"""
    if not portfolio:
        print("📭 Your portfolio is empty!\n")
        return

    total_value = 0
    print("\n📊 Your Stock Portfolio:")
    print("Symbol  |  Shares  |  Price  |  Total Value")
    print("-" * 40)

    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            stock_value = price * quantity
            total_value += stock_value
            print(f"{symbol}    |   {quantity}     |  ${price}  |  ${stock_value}")
        else:
            print(f"{symbol}    |   {quantity}     |  ⚠️ Price Unavailable")

    print("-" * 40)
    print(f"💰 Total Portfolio Value: ${total_value}\n")

def menu():
    """Display menu for user interaction"""
    while True:
        print("📈 Stock Portfolio Tracker")
        print("1️⃣ Add Stock")
        print("2️⃣ Remove Stock")
        print("3️⃣ Show Portfolio")
        print("4️⃣ Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            print("🚀 Exiting Stock Portfolio Tracker. Have a great day!")
            break
        else:
            print("❌ Invalid option, please try again!\n")

# Run the menu
menu()
