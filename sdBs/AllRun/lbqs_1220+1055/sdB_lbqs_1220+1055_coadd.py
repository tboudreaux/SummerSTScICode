from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[185.765208,10.644339],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lbqs_1220+1055/sdB_lbqs_1220+1055_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lbqs_1220+1055/sdB_lbqs_1220+1055_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
