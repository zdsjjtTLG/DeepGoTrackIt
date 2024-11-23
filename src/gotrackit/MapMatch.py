class SpreadPortfolio:
    """
    The spread strategy is:
    On start date, we borrow a bond(bond_short) and sell it. At the same time, we spend the cash received to buy    another bond(bond_long). We expect the ytm spread of two bonds will increase or decrease.
    On end date, we sell the bond_long. We spend the cash received to buy the bond_short and return it to the lender.    If the ytm spread increases or decreases as we expected, we should get some profit at the end.
    Cash flows during the period are considered. Extra cash generates profit at a risk-free rate(rf), and short of cash    decreases profit at the same risk-free rate(rf).
    All yields or risk-free p/l are calculated assuming 365 days per year.
    Yields' units are exact float numbers, eg. 0.05 for 5.0%.
    """

    def profit(self, bond_short: float,
               bond_long: float,
               ytm_open_short: float,
               ytm_open_long: float,
               ytm_close_short: float,
               ytm_close_long: float,
               lend_rate: float,
               start_date: float,
               end_date: float,
               rf: float = 0.0):
        """
        Core function to calculate strategy profit and yield. It's designed to deal with different scenarios.

        Args:
            bond_short:  A FinancePy Bond to short(expects its ytm to increase), optional.
            bond_long:  A FinancePy Bond to short(expects its ytm to increase).
            ytm_open_short:  A FinancePy Bond to short(expects its ytm to increase).
            ytm_open_long:  A FinancePy Bond to short(expects its ytm to increase).
            ytm_close_short:  A FinancePy Bond to short(expects its ytm to increase).
            ytm_close_long:  A FinancePy Bond to short(expects its ytm to increase).
            lend_rate:  A FinancePy Bond to short(expects its ytm to increase).
            start_date:  A FinancePy Bond to short(expects its ytm to increase).
            end_date:  A FinancePy Bond to short(expects its ytm to increase).
            rf:  A FinancePy Bond to short(expects its ytm to increase).

        Returns:
            profit(float): profit or loss of the portfolio at the end.
            profit_yield(float): profit / bond_long._face_amount * 365 / (end_date - start_date)
        """
