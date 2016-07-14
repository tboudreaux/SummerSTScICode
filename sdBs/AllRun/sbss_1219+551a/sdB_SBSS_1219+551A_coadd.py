from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[185.475792,54.846639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_1219+551A/sdB_SBSS_1219+551A_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_1219+551A/sdB_SBSS_1219+551A_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
