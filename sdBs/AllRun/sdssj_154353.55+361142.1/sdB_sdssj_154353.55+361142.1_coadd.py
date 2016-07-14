from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[235.973125,36.195028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_154353.55+361142.1/sdB_sdssj_154353.55+361142.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_154353.55+361142.1/sdB_sdssj_154353.55+361142.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
