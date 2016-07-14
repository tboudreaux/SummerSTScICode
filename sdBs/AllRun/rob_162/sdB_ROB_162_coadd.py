from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.16025,-53.642028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ROB_162/sdB_ROB_162_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ROB_162/sdB_ROB_162_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
