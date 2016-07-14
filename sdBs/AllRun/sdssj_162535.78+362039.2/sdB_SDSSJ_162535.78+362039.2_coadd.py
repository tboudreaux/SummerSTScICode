from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[246.399083,36.344222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_162535.78+362039.2/sdB_SDSSJ_162535.78+362039.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_162535.78+362039.2/sdB_SDSSJ_162535.78+362039.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
