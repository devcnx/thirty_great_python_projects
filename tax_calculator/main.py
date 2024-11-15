import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        self.padding = {"padx": 20, "pady": 10}

        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(
            self.window, placeholder_text="Enter Your Income", justify="center"
        )
        self.income_entry.grid(row=0, column=1, **self.padding)

        self.tax_rate_label = ctk.CTkLabel(self.window, text="Tax Rate:")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(
            self.window, placeholder_text="Enter Tax Rate", justify="center"
        )
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        self.result_label = ctk.CTkLabel(self.window, text="Tax:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(
            self.window, placeholder_text="Tax", justify="center"
        )
        self.result_entry.grid(row=2, column=1, **self.padding)

        self.calculate_button = ctk.CTkButton(
            self.window, text="Calculate", command=self.calculate_tax
        )
        self.calculate_button.grid(row=3, column=0, columnspan=2, **self.padding)

    def update_result(self, text: str) -> None:
        self.result_entry.delete(0, "end")
        self.result_entry.insert(0, text)

    def clear_input(self) -> None:
        self.income_entry.delete(0, "end")
        self.tax_rate_entry.delete(0, "end")
        self.result_entry.delete(0, "end")

    def calculate_tax(self) -> None:
        try:
            income = float(self.income_entry.get())
            tax_rate = float(self.tax_rate_entry.get())
            self.update_result(f"${income * (tax_rate / 100):,.2f}")
        except ValueError:
            self.clear_input()
            self.update_result("Invalid Input")

    def run(self) -> None:
        self.window.mainloop()


if __name__ == "__main__":
    calculator = TaxCalculator()
    calculator.run()
