from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[123.724667,28.1895],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_081453.92+281122.2/sdB_SDSSJ_081453.92+281122.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_081453.92+281122.2/sdB_SDSSJ_081453.92+281122.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
