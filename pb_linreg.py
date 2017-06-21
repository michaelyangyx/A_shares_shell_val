import scipy
import scipy.stats as stats

def lin_reg_pbratio(stock_list, date):
    # stock list can be either industry or a list of stocks
    # date should be input as a string

    # market cap
    # use A-share Market Valuation
    # therefore ignore the effect of foreign markets on valuation

    df = get_fundamentals(query(
            fundamentals.eod_derivative_indicator.a_share_market_val,
            fundamentals.eod_derivative_indicator.pb_ratio).filter(
            fundamentals.stockcode.in_(stock_list)),
            entry_date = date, interval = '2d')
    df = df.dropna(axis=2)

    mc = df['a_share_market_val']

    # book value
    # use public p/b ratio to calculate corresponding book value
    pb = df['pb_ratio']

    mc_arr = numpy.array(mc[date])
    pb_arr = numpy.array(pb[date])
    # give a specific date, pull out the mc and te data of all companies

    mc_data = mc_arr.astype(float);
    pb_data = pb_arr.astype(float);
    #data structure change, into float arrays

    bv_data = mc_arr/pb_arr;
    bv_data = bv_data.astype(float);
    # use element-wise division to calculate corresponding book value

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(bv_data, mc_data)

    return slope, intercept
