from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[183.848958,13.850806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lbqs_1212+1407/sdB_lbqs_1212+1407_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lbqs_1212+1407/sdB_lbqs_1212+1407_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
