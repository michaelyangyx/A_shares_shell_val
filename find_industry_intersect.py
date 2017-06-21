import numpy

##### The following code finds the intersect between all stocks and specific
##### industry

def find_industry_intersect(industry_code, total_stocks):
    # industry input as a string, specified in the Rice Quant database

    industry_stocks = industry(industry_code)

    industry_stocks = numpy.array(industry_stocks)
    industry_stocks = industry_stocks.astype(object)

    intersection = numpy.intersect1d(industry_stocks, stocks)
    intersection_list = intersection.tolist()

    # The final return is as a list of strings
    return intersection_list
