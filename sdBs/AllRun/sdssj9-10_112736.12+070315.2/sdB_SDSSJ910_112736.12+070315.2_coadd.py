from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[171.9005,7.054222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_112736.12+070315.2/sdB_SDSSJ910_112736.12+070315.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_112736.12+070315.2/sdB_SDSSJ910_112736.12+070315.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
