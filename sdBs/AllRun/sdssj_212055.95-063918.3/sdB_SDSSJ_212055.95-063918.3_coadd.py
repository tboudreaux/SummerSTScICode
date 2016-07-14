from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.233125,-6.655083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_212055.95-063918.3/sdB_SDSSJ_212055.95-063918.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_212055.95-063918.3/sdB_SDSSJ_212055.95-063918.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
