from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.981583,0.877806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_223955.58-005240.1/sdB_sdssj_223955.58-005240.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_223955.58-005240.1/sdB_sdssj_223955.58-005240.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
