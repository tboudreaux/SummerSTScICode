from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[242.042375,42.979167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_160810.17+425845.0/sdB_SDSSJ_160810.17+425845.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_160810.17+425845.0/sdB_SDSSJ_160810.17+425845.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
