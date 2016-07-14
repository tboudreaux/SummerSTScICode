from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[210.750417,-18.804544],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_14002-1833/sdB_ec_14002-1833_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_14002-1833/sdB_ec_14002-1833_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
