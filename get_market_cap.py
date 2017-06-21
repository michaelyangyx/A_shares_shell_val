import scipy
import scipy.stats as stats

def get_market_cap(stock_list, date):
    # stock list can be either industry or a list of stocks
    # date should be input as a string

    # market cap
    # use A-share Market Valuation
    # therefore ignore the effect of foreign markets on valuation
    mc = get_fundamentals(query(
            fundamentals.eod_derivative_indicator.a_share_market_val).filter(
            fundamentals.stockcode.in_(stock_list)),
            entry_date = date, interval = '8q')

    mc_spec = numpy.array(mc.major_xs(date))
    # give a specific date, pull out the mc and te data of all companies

    mc_arr = mc_spec[0][0];
    mc_data = mc_arr.astype(float);
    #data structure change, into float arrays

    return numpy.mean(mc_data)
