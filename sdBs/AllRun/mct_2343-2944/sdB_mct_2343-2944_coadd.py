from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[356.573917,-29.463858],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_mct_2343-2944/sdB_mct_2343-2944_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_mct_2343-2944/sdB_mct_2343-2944_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
