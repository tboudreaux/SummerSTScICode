from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[6.949292,34.674206],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0025+3423/sdB_hs_0025+3423_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0025+3423/sdB_hs_0025+3423_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
