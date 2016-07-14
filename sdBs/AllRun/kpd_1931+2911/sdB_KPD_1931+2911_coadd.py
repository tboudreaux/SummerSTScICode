from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[293.454917,29.296553],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_1931+2911/sdB_KPD_1931+2911_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_1931+2911/sdB_KPD_1931+2911_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
