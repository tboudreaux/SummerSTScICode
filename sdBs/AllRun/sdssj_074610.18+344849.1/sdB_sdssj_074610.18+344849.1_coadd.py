from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[116.542417,34.813639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_074610.18+344849.1/sdB_sdssj_074610.18+344849.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_074610.18+344849.1/sdB_sdssj_074610.18+344849.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
