from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[345.501292,52.089442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_2259+5149/sdB_KPD_2259+5149_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_2259+5149/sdB_KPD_2259+5149_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
