from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[5.849958,0.498139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_002323.99-002953.3/sdB_SDSSJ_002323.99-002953.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_002323.99-002953.3/sdB_SDSSJ_002323.99-002953.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
