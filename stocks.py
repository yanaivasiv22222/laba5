import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

def load_history_data(fname: str) -> np.ndarray:
    from_strdate = lambda x: datetime.strptime(x.strip('"'), '%d.%m.%Y')
    from_strnum = lambda x: float(x.replace(".", "").replace(",", "."))
    def from_strnumm(x):
        x = x.strip('"')
        if x.endswith('M'):
            return float(x.strip('M')) * 1_000_000
        elif x.endswith('K'):
            return float(x.strip('K')) * 1_000
        else:
            return float(x)
    from_strpcnt = lambda x: float(x.strip('"').strip('%')) / 100
    names = ("date", "price", "open", "high", "low", "volume", "change")
    data = np.genfromtxt(fname, delimiter=",", encoding="utf-8", skip_header=1, names=names,
                         dtype=[("date", datetime),
                                ("price", np.float64),
                                ("open", np.float64),
                                ("high", np.float64),
                                ("low", np.float64),
                                ("volume", np.float64),
                                ("change", np.float64)],
                         converters={
                             "date": from_strdate,
                             "price": from_strnum,
                             "open": from_strnum,
                             "high": from_strnum,
                             "low": from_strnum,
                             "volume": from_strnumm,
                             "change": from_strpcnt})
    return data

def plot_history_data(data: np.ndarray, n=100) -> None:
    plt.style.use('dark_background')
    
    fig, ax = plt.subplots()
    date, highs, lows = data['date'][:n], data['high'][:n], data['low'][:n]
    ax.plot(date, highs, c='red', alpha=0.5)
    ax.plot(date, lows, c='blue', alpha=0.5)
    plt.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

    plt.title(f"Stock high and low prices per {n} days", fontsize=18)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Price (USD)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.grid()
    plt.show()

def main() -> None:
    fname_dax = 'DAX.csv'
    fname_ipc = 'S&P_BMV IPC.csv'
    data_dax = load_history_data(fname_dax)
    print(data_dax)
    data_ipc = load_history_data(fname_ipc)

    plot_history_data(data_dax)
    plot_history_data(data_ipc)

if __name__ == "__main__":
    main()