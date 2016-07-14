from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[231.784625,0.552306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_152708.31+003308.3/sdB_sdssj_152708.31+003308.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_152708.31+003308.3/sdB_sdssj_152708.31+003308.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
