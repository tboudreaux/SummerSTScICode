from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[189.589542,-2.203167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_123821.49-021211.4/sdB_sdssj_123821.49-021211.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_123821.49-021211.4/sdB_sdssj_123821.49-021211.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
