from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[283.558792,17.866722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_185414.11+175200.2/sdB_sdssj_185414.11+175200.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_185414.11+175200.2/sdB_sdssj_185414.11+175200.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
