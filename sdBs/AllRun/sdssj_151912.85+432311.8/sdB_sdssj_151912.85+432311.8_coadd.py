from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[229.803542,43.386611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_151912.85+432311.8/sdB_sdssj_151912.85+432311.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_151912.85+432311.8/sdB_sdssj_151912.85+432311.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
