from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[181.814,10.893456],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_1204+1110/sdB_LBQS_1204+1110_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_1204+1110/sdB_LBQS_1204+1110_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
