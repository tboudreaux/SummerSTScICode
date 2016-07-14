from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[105.392708,-67.294631],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j07015-6717/sdB_galex_j07015-6717_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j07015-6717/sdB_galex_j07015-6717_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
