from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[144.311083,49.278556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_093714.66+491642.8/sdB_SDSSJ_093714.66+491642.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_093714.66+491642.8/sdB_SDSSJ_093714.66+491642.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
