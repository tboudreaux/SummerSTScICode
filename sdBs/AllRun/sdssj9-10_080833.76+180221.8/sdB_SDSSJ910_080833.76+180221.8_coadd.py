from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.140667,18.039389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_080833.76+180221.8/sdB_SDSSJ910_080833.76+180221.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_080833.76+180221.8/sdB_SDSSJ910_080833.76+180221.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
