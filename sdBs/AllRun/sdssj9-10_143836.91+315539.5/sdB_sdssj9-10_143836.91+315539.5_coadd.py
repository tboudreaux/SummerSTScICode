from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[219.653792,31.927639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_143836.91+315539.5/sdB_sdssj9-10_143836.91+315539.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_143836.91+315539.5/sdB_sdssj9-10_143836.91+315539.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
