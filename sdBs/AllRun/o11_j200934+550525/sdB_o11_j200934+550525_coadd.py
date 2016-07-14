from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[302.391667,55.090278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j200934+550525/sdB_o11_j200934+550525_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j200934+550525/sdB_o11_j200934+550525_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
