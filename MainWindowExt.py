from PyQt6.QtWidgets import QInputDialog, QTableWidgetItem
from Chapter6.Ex_127.MainWindow import Ui_MainWindow
import pandas as pd


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.data = self.load_data()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.refresh_data(self.data)
        self.pushButtonRefresh.clicked.connect(lambda: self.refresh_data(self.data))
        self.pushButtonSort.clicked.connect(self.sort_by_price)
        self.pushButtonGenerate.clicked.connect(self.search_symbol_and_reduce)
        self.pushButtonAddUSD.clicked.connect(self.add_usd_column)
        self.pushButtonAdd.clicked.connect(self.add_new_row)
        self.pushButtonGbyG.clicked.connect(self.group_and_statistics)
        self.pushButtonDelete.clicked.connect(self.delete_by_symbol)

    def load_data(self):
        file_path = "SampleData2.csv"
        return pd.read_csv(file_path)

    def refresh_data(self, df):
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.tableWidget.setItem(row, col, item)

    def sort_by_price(self):
        sorted_df = self.data.sort_values(by='Price', ascending=True)
        self.refresh_data(sorted_df)

    def search_symbol_and_reduce(self):
        symbol, ok = QInputDialog.getText(self.MainWindow, "Input Symbol", "Enter Symbol to reduce price:")
        if ok and symbol:
            self.data.loc[self.data['Symbol'] == symbol, 'Price'] /= 2
            self.refresh_data(self.data)

    def add_usd_column(self):
        self.data['USD'] = self.data['Price'] / 23
        self.refresh_data(self.data)

    def add_new_row(self):
        symbol, ok1 = QInputDialog.getText(self.MainWindow, "Input Symbol", "Enter Symbol:")
        price, ok2 = QInputDialog.getDouble(self.MainWindow, "Input Price", "Enter Price:")
        pe, ok3 = QInputDialog.getDouble(self.MainWindow, "Input PE", "Enter PE:")
        if ok1 and ok2 and ok3:
            usd = price / 23
            new_row = pd.DataFrame({'Symbol': [symbol], 'Price': [price], 'PE': [pe], 'USD': [usd]})
            self.data = pd.concat([self.data, new_row], ignore_index=True)
            self.refresh_data(self.data)

    def group_and_statistics(self):
        grouped = self.data.groupby('Group').agg({'Price': ['mean', 'sum', 'count']})
        grouped.columns = ['_'.join(col) for col in grouped.columns]
        grouped = grouped.reset_index()
        self.refresh_data(grouped)

    def delete_by_symbol(self):
        symbol, ok = QInputDialog.getText(self.MainWindow, "Input Symbol", "Enter Symbol to delete:")
        if ok and symbol:
            self.data = self.data[self.data['Symbol'] != symbol]
            self.refresh_data(self.data)

    def show(self):
        self.MainWindow.show()
