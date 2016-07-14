from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[246.123875,33.568917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_162429.73+333408.1/sdB_SDSSJ_162429.73+333408.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_162429.73+333408.1/sdB_SDSSJ_162429.73+333408.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
