from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[290.954583,62.598083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_192349.10+623553.1/sdB_sdssj_192349.10+623553.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_192349.10+623553.1/sdB_sdssj_192349.10+623553.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
