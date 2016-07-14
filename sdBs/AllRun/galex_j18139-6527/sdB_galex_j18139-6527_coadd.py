from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[273.487333,-65.463136],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j18139-6527/sdB_galex_j18139-6527_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j18139-6527/sdB_galex_j18139-6527_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
