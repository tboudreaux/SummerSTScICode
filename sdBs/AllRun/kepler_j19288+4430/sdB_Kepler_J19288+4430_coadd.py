from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[292.212917,44.503611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19288+4430/sdB_Kepler_J19288+4430_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19288+4430/sdB_Kepler_J19288+4430_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
