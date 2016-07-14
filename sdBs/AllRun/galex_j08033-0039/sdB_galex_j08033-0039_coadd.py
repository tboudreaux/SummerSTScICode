from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.836417,0.660697],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j08033-0039/sdB_galex_j08033-0039_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j08033-0039/sdB_galex_j08033-0039_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
