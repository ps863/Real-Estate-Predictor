
import click
import numpy as np

"""
Coefficients used are derived from the analysis conducted in Real Estate Analysis.ipynb
For updating read the README on Github
"""




@click.command()
@click.option('--d_to_mrt',prompt='How far is the MRT station? (In Meter)',type=click.FLOAT)
@click.option('--houseage',prompt='How old is the house? (Convert to years)',type=click.FLOAT)
@click.option('--no_of_stores',prompt='How many stores are in the proximity of this property?',type=click.INT)
@click.option('--latitude',prompt='Latitude of the house?',type=click.FLOAT)
@click.option('--longitude',prompt='Longitude the house?',type=click.FLOAT)



def getHomePrice (houseage , d_to_mrt , no_of_stores , latitude , longitude) :
    """Predicts the House Price in Hong Kong using precalculated coefficients found via sample dataset"""

    betacoeff = np.array([[-4.94559479e+03],
                          [-2.68916833e-01],
                          [-4.25908902e-03],
                          [1.16302048e+00],
                          [2.37767190e+02],
                          [-7.80545518e+00]])

    homePrice = 0
    homePrice += betacoeff[1] * houseage
    homePrice += betacoeff[2] * d_to_mrt
    homePrice += betacoeff[3] * no_of_stores
    homePrice += betacoeff[4] * latitude
    homePrice += betacoeff[5] * longitude
    homePrice += betacoeff[0]

    print( "Home Price per unit area based on parameters and sample data = " + str(homePrice[0]))




if __name__ =="__main__":
    print ("This program uses set Beta Regression coefficients. If you wish to update, please see README on Github to see how")
    getHomePrice()

