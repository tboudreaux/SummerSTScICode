from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[211.223667,12.74125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_140453.68+124428.5/sdB_SDSSJ_140453.68+124428.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_140453.68+124428.5/sdB_SDSSJ_140453.68+124428.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
