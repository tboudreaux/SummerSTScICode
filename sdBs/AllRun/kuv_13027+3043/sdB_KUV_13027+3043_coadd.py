from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[196.268792,30.454919],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_13027+3043/sdB_KUV_13027+3043_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_13027+3043/sdB_KUV_13027+3043_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
