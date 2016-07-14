from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[318.128833,-15.402881],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j211230.92-152410.37/sdB_galex_j211230.92-152410.37_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j211230.92-152410.37/sdB_galex_j211230.92-152410.37_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
