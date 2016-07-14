from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[123.330917,52.951864],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j08133+5257/sdB_galex_j08133+5257_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j08133+5257/sdB_galex_j08133+5257_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
