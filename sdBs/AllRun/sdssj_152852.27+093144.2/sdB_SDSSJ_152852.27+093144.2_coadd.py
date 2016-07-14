from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[232.217792,9.528944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_152852.27+093144.2/sdB_SDSSJ_152852.27+093144.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_152852.27+093144.2/sdB_SDSSJ_152852.27+093144.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
