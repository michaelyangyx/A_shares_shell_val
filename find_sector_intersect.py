import numpy

##### The following code finds the intersect between all stocks and specific
##### sector

def find_sector_intersect(sector_code, total_stocks):
    # sector input as a string, specified in the Rice Quant database

    sector_stocks = sector(sector_code)

    sector_stocks = numpy.array(sector_stocks)
    sector_stocks = sector_stocks.astype(object)

    intersection = numpy.intersect1d(sector_stocks, stocks)
    intersection_list = intersection.tolist()

    # The final return is as a list of strings
    return intersection_list
