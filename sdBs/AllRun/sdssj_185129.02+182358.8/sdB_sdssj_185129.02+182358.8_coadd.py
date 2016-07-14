from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[282.870917,18.399667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_185129.02+182358.8/sdB_sdssj_185129.02+182358.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_185129.02+182358.8/sdB_sdssj_185129.02+182358.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
