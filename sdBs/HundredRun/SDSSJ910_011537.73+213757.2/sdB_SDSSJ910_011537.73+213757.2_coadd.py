from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[283.60812,21.632556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_011537.73+213757.2/sdB_SDSSJ910_011537.73+213757.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_011537.73+213757.2/sdB_SDSSJ910_011537.73+213757.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
